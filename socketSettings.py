# import socket
#
# HOST = 'localhost'  # Standard loopback interface address (localhost)
# PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# print("initialize server...")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     print("HERE1")
#     with conn:
#         print("HERE1.5")
#         print('Connected by', addr)
#         while True:
#             print("HERE2")
#             data = conn.recv(1024)
#             if not data:
#                 print("HERE3")
#                 break
#             conn.sendall(b"thank you")
#             print("HERE4")
import asyncore
import socket
import time
import logging
import json

#https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
class Server(asyncore.dispatcher):

    def __init__(self, host, port):

        self.logger = logging.getLogger('SERVER')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(confjson.get('SERVER_QUEUE_SIZE', None))
        self.logger.debug('binding to {}'.format(self.socket.getsockname()))

    def handle_accept(self):
        socket, address = self.accept()
        self.logger.debug('new connection accepted')
        EchoHandler(socket)


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):

        msg = self.recv(confjson.get('RATE', None))
        self.out_buffer = msg
        self.out_buffer += ' server recieve: {}'.format(time.time())
        if not self.out_buffer:
            self.close()


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )
    with open('config.json', 'r') as jfile:
        confjson = json.load(jfile)
    try:
        logging.debug('Server start')
        server = Server(confjson.get('HOST', None),
                        confjson.get('PORT', None))
        asyncore.loop()
    except:
        logging.error('Something happened,\n'
                      'if it was not a keyboard break...\n'
                      'check if address taken, '
                      'or another instance is running. Exit')
    finally:
        logging.debug('Goodbye')
