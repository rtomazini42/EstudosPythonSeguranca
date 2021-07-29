import os
import time
print("." * 50)
os.system('color 0d')

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('_'*50)
        print('Verificando ip {}'.format(ip))
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(3)



print("." * 50)
