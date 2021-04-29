import logging
from socket import socket, timeout
import threading
# BIND_IP = '0.0.0.0'


class Honeypot(object):
    def __init__(self, bind_ip, ports, logfile):
        if len(ports) < 1:
            raise Exception("No port provided")

        self.bind_ip = bind_ip
        self.ports = ports
        self.logfile = logfile
        self.listeners = {}

        self.logger = self.configure_logging()

        self.logger.info("Honeypot starting up...")
        self.logger.info("Ports: %s" % self.ports)
        self.logger.info("Log file path : %s" % self.logfile)

        if len(ports) < 1:
            raise Exception("Port error")

    def handle_connection(self, client_socket, port, ip, remote_port):
        self.logger.info("Connection received: %s: %s:%d" %
                         (port, ip, remote_port))

        client_socket.settimeout(4)
        try:
            data = client_socket.recv(64)
            self.logger.info("Data received: %s: %s:%d: %s" %
                             (port, ip, remote_port, data))
            client_socket.send("Access denied.\n".encode('utf8'))
        except timeout:
            pass
        client_socket.close()
        # client_socket.close()

    def start_listening_thread(self, port):
        listener = socket()
        listener.bind((self.bind_ip, int(port)))
        listener.listen(5)

        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(
                target=self.handle_connection, args=(client, port, addr[0], addr[1]))
            client_handler.start()

    def start_listening(self):
        for port in self.ports:
            self.listeners[port] = threading.Thread(
                target=self.start_listening_thread, args=(port,))
            # self.start_new_listener_theard(port)
            self.listeners[port].start()

    def run(self):
        self.start_listening()

    def configure_logging(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m %d %H:%M:%s',
                            filename=self.logfile,
                            filemode='w')
        logger = logging.getLogger(__name__)
        # Console Handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        logger.addHandler(consoleHandler)
        return logger

    def run(self):
        self.start_listening()
