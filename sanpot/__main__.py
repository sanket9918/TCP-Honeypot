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

# Validate Arguments
if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
    print(__doc__)
    sys.exit(1)

# Load configuration -  ports, log_file
config_filepath = sys.argv[1]
config = configparser.ConfigParser()
config.read(config)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info('test')

# Config file example
# config = 'sanpot.ini'

ports = config.get('default', 'ports', raw=True, fallback="4444,2222,5555")
host = config.get('default', 'host', raw=True, fallback="0.0.0.0")
logfile = config.get('default', 'logfile', raw=True,
                     fallback="sanpot.log")

logger.info("Ports : %s" % ports)
logger.info("Logfile: %s" % logfile)

try:
    ports = ports.split(',')
except Exception as e:
    logger.error("Error parsing ports: %s  \nExiting ", ports)
    sys.exit(1)

honeyport = Honeypot(host, ports, logfile)
honeyport.run()
