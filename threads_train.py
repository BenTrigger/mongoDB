import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def n(number):
    logging.debug('Starting')
    logging.debug('Exiting')
    logging.debug(number)

def d():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')


if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=d)
    d.setDaemon(False)
    d.start()
    threading.Thread(name='non-daemon', target=n, args=[16]).start()
