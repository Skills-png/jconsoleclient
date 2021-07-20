import sys, os
from socket import socket, AF_INET, SOCK_DGRAM
SERVER_IP   = sys.argv[1] #    172.16.51.14
PORT_NUMBER = sys.argv[2] #    5000
SIZE = 1024
print('[*] Metros Jconsole - Remote computer access.')
print('[*] Jconsole version 1.0.\n')
print('[*] Github client: https://github.com/Skills-png/jconsoleclient')
print('[*] Github server: https://github.com/Skills-png/jconsoleserver\n')
try:
    mySocket = socket(AF_INET, SOCK_DGRAM)
    print('[+] Ip '+SERVER_IP+' Port '+PORT_NUMBER)
except:
    print('[-] Ip '+SERVER_IP+' Port '+str(PORT_NUMBER))
while True:
    mySocket.sendto(input(' $ ').encode('utf8'),(str(SERVER_IP),int(PORT_NUMBER)))
sys.exit()
