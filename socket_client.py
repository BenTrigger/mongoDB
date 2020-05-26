# import socket
#
# HOST = 'localhost'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
#     print("1")
#     s.sendall(b'Hello, world')
#     data2 = s.recv(1024)
#     print("2")
#
# print('Received', repr(data))
# print('Received', repr(data2))
import asyncore
import socket
import time
import logging
import json

#https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message, pk):
        self.logger = logging.getLogger('CLIENT')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.connect((host, port))
        self.out_buffer = message
        self.clientID = pk
        self.logger.debug('Connected #{}'.format(self.clientID))

    def handle_close(self):
        self.close()

    def handle_read(self):
        rec_msg = self.recv(confjson.get('RATE', None))
        self.logger.debug('#{}, {} back at client {}'.format(self.clientID, rec_msg, time.time()))
        self.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s',)
    with open('config.json', 'r') as jfile:
        confjson = json.load(jfile)
    clients = []
    for idx in range(confjson.get('SOCKET_AMOUNT', None)):
        msg = b'getting message now'
        clients.append(Client(confjson.get('HOST', None), confjson.get('PORT', None), msg, idx))
    start = time.time()
    logging.debug('Starting async loop for all connections, unix time {}'.format(start))
    asyncore.loop()
    logging.debug('{}'.format(time.time() - start))