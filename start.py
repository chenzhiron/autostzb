import threading
from st import stzb
from modules.web.web import ui

if __name__ == '__main__':
    new_thread = threading.Thread(target=ui.start)
    new_thread.setDaemon(True)
    new_thread.start()
    stzb.loop()
