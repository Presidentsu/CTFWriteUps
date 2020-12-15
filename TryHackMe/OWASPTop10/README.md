# OWASP Top 10

This challenge consists information about OWASP(Open Web Application Security Project) Top 10 web vulnerabilites.

Which are

1. Injection
2. Broken Authentication.
3. Sensitive Data Exposure
4. XML Extrenal Entity
5. Broken Access Control
6. Security Misconfiguration
7. Cross-site Scripting
8. Insecure Deserialization
9. Components with known vulnerabilities
10. Insufficient Logging & Monitoring

### Task 1-4 

Has information about command injections and how these can be leverrages DO HAVE A LOOK at it.

### Task 5 - CMD Injection Practical

Deploy the machine and navigate to http://IPaddress/evilshell.php

And we will be invited with EvilShell input form where we can do our command injection.

#### Questions

...

	1. What strange text file is in the website root directory?
		- Ans: drpepper.txt (input -> ls)
	2. How many non-root/non-service/non-daemon users are there?
		- Ans: 0 (input -> cat /etc/passwd)
	3. What user is this app running as?
		- Ans: www-data (input -> whoami)
	4. What is the user's shell set as?
		- Ans: /usr/sbin/nologin (input -> cat /etc/passwd)
	5. What version of Ubuntu is running?
		- Ans: 18.0.4 (input -> lsb_release -a)
	6. Print out the MOTD. What favorite beverage is shown
		- Ans: Dr pepper (input -> cat /etc/update-motd.d/00-header)
...

### Task 6-7 Broken Authentication

Aye Yo give the description a read tho!!!

Deploy the machine and go to http://IPaddress:8888

And try to login with username as Darren. You can see that it shows there is an account with that username.

Now try to register with same Username with a space at the end and random email and password it shows no error so now proceed to login with darren with space at end with the password that you gave during registration.

Now you have darren's account.

#### Questions

...

	1. What is the flag that you found in darren's account?
		- Ans: fe86079416a21a3c99937fea8874b667
	2. Now try to do the same trick and see if you can login as arthur?
		- Ans: No answer needed (repeat the same for arthur)
	3. What is the flag that you found in arthur's account?
		- Ans: d9ac0f7db4fda460ac3edeb75d75e16e
...


### Task 8-11 Sensitive Data Expoure

Deploy the machine. Open the web page and have a look at it it says nothing interesting.

Now lets use gobuster to find any pages.

`gobuster dir -u http://10.10.151.201/ -w /usr/share/dirb/wordlists/common.txt`

Gave us

...

	/.hta (Status: 403)
	/.htaccess (Status: 403)
	/.htpasswd (Status: 403)
	/api (Status: 301) -> Endpoint doesnt exist
	/assets (Status: 301) -> the one
	/console (Status: 301) -> Unauthorized
	/favicon.ico (Status: 200)
	/index.php (Status: 200)	
	/login (Status: 301)
	/server-status (Status: 403)
...

If open /assets/ we have a file with name webapp.db 

`
sqlite3                                                                 
SQLite version 3.33.0 2020-08-14 13:23:32
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open webapp.db
sqlite> .tables
sessions  users   
sqlite> select * from users;
4413096d9c933359b898b6202288a650|admin|6eea9b7ef19179a06954edd0f6c05ceb|1
23023b67a32488588db1e28579ced7ec|Bob|ad0234829205b9033196ba818f7a872b|1
4e8423b514eef575394ff78caed3254d|Alice|268b38ca7b84f44fa0a6cdc86e6301e0|0
`

Now lets crack the passwords using crackstion or something

we get passwords

admin: qwertyuiop
Alice: test2

Now login with the admin credentials.

#### Questions 

...

	1. What is the name of the mentioned directory?
		- Ans: /assets
	2.	Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?
		- Ans: webapp.db
	3. Use the supporting material to access the sensitive data. What is the password of the hash of the admin user?
		- Ans: 6eea9b7ef19179a06954edd0f6c05ceb
	4. What is the admin's plaintext password?
		- Ans: qwertyuiop
	5. Login as the admin. What is the flag?
		- Ans: THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}

...

### Task 12- [Will update it later :-( ]