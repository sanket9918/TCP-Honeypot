import logging
from socket import socket
import threading
BIND_IP = '0.0.0.0'


class Honeypot(object):
    def __init__(self, ports, logfile):
        self.ports = ports
        self.logfile = logfile
        self.listeners = {}

        if len(ports) < 1:
            raise Exception("Port error")

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m %d %H:%M:%s',
                            filename=logfile,
                            filemode='w')
        self.logger = logging.getLogger(__name__)
        self.logger.info("Honeypot starting up...")
        self.logger.info("Ports: %s" % self.ports)
        self.logger.info("Log file path : %s" % self.logfile)

    def handle_connection(self, client_socket, ip, remote_port):
        while True:
            req = client_socket.recv(64)
            self.logger.info("Connection from %s:%d : %s" %
                             (ip, remote_port, req))

            if not req:
                break
            elif req == 'b\'killsrv\\n\'':
                client_socket.close()
                sys.exit()
            else:
                client_socket.send("Access denied.\n".encode('utf8'))
            # client_socket.close()

    def start_listening_thread(self, port):
        listener = socket()
        listener.bind((BIND_IP, int(port)))
        listener.listen(5)

        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(
                target=self.handle_connection, args=(client, addr[0], addr[1]))
            client_handler.start()

    def start_listening(self):
        for port in self.ports:
            self.listeners[port] = threading.Thread(
                target=self.start_listening_thread, args=(port,))
            # self.start_new_listener_theard(port)
            self.listeners[port].start()

    def run(self):
        self.start_listening()
