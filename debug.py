import  json, re, os, sys
import pyttsx3
import speech_recognition as sr
import sys, os
from socket import socket, AF_INET, SOCK_DGRAM
tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-40)
volume = tts.getProperty('volume')
tts.setProperty('volume', volume+0.9)
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == '1':
        tts.setProperty('voice', voice.id)
def stop(var):

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
        mySocket.sendto(var.encode('utf8'),(str(SERVER_IP),int(PORT_NUMBER)))
    sys.exit()
def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        
        r.adjust_for_ambient_noise(source, duration=1) 
         
        audio = r.listen(source)
     
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(query.lower())
        
        if query.lower() == "о'кей а там включи spotify":
            stop('start C:\\Users\\Atom\AppData\\Roaming\\Spotify\\spotify.exe')
        if query.lower() == "о'кей а там выключи spotify":
            stop('taskkill /im spotify.exe /f>nul')
        if query.lower() == "о'кей а там выключи компьютер":
            stop('shutdown -s -t 0')
        if query.lower() == "о'кей а там заблокируй компьютер":
            stop('Rundll32.exe user32.dll,LockWorkStation')
        
    except:
        pass

def talk( text ):
    tts.say( text )
    tts.runAndWait()

 

while True:
    record_volume()
