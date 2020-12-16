# Day 16 Challenge
## Help! Where is Santa? 

Lets fire up the machine and start by doing nmap scan to find the open port as the challenge description says we have to find the port.

...

	>> nmap -Pn 10.10.159.88          
	Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
	Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-16 11:07 EST
	Nmap scan report for 10.10.159.88
	Host is up (0.21s latency).
	Not shown: 999 closed ports
	PORT     STATE SERVICE
	8000/tcp open  http-alt

...

Hmm so the site is hosted on port 8000

Lets try to enumerate hidden directories using gobuster.

It shows /static but it takes us to main index page but with some more css and stuff :-(

It gave me nothing more :-( 

So they said they are are using api key in /api/

But we now have an issue over here we dont know the api key 
so lets bruteforce it as they mentioned it is between 1-100 
and its an odd number

Lets do a python script to automate the boring stuff. 

...
	
	#!/usr/bin/env python3

	import requests

	#Loop

	for i in range(1, 100, 2) :

		url = requests.get(f'http://10.10.159.88:8000/api/{i}')

		print(url.text)
...


Now lets run the script and let the script bruteforce our key for us.

We get this in between our responses.

...

	{"item_id":53,"q":"Error. Key not valid!"}
	{"item_id":55,"q":"Error. Key not valid!"}
	{"item_id":57,"q":"Winter Wonderland, Hyde Park, London."}
	{"item_id":59,"q":"Error. Key not valid!"}

...

Naice right so the api key is 57.

### Questions

...
	
	1. What is the port number for the web server?
		- Ans: 8000
	2. What is the directory for the API, without the API key?
		- Ans: /api/
	3. Where is Santa right now?
		- Ans: Winter Wonderland, Hyde Park, London
	4. Api key?
		- Ans: 57

...


Thank you! <3 