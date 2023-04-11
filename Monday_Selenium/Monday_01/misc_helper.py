import time

from interface import Interface

result = ''
def send_result(result):
    if (result != ''):
        print('Sending result: ' + result)
        print('Pausing here for analysis before the UI closes.')
        interface = Interface()
        interface.display_result(result)
        time.sleep(30)