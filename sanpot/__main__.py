"""
SanPot

TCP Honeypot logger

Usage: 
    sanpot --config FILE

Options:
    -h --help    show this
    --config FILE    File with configurations

"""

import configparser
from sanpot import Honeypot
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info('test')
# Config file
config = 'sanpot.ini'

# ports, log_file
config = configparser.ConfigParser()
config.read(config)

ports = config.get('default', 'ports', raw=True, fallback="4444,2222,5555")

logfile = config.get('default', 'logfile', raw=True,
                     fallback="sanpot.log")

logger.info("Ports : %s" % ports)
logger.info("Logfile: %s" % logfile)

try:
    ports = ports.split(',')
except Exception as e:
    logger.error("Error parsing ports: %s  \nExiting ", ports)
    sys.exit(1)

honeyport = Honeypot(ports, logfile)
honeyport.run()
