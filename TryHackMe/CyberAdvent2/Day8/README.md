# Day8 Challenge
## What's Under the Christmas Tree?
This challenge is on nmap basics and how to use it
`
nmap -sC -sV -A -O 10.10.84.163           
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-13 13:20 EST
Nmap scan report for 10.10.84.163
Host is up (0.16s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Hugo 0.78.2
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: TBFC&#39;s Internal Blog
2222/tcp open  ssh           OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 cf:c9:99:d0:5c:09:27:cd:a1:a8:1b:c2:b1:d5:ef:a6 (RSA)
|   256 4c:d4:f9:20:6b:ce:fc:62:99:54:7d:c2:b4:b2:f2:b2 (ECDSA)
|_  256 d0:e6:72:18:b5:20:89:75:d5:69:74:ac:cc:b8:3b:9b (ED25519)
3389/tcp open  ms-wbt-server xrdp
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/13%OT=80%CT=1%CU=37676%PV=Y%DS=2%DC=T%G=Y%TM=5FD65B
OS:88%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M505ST11NW6%O2=M505ST11NW6%O3=M505NNT11NW6%O4=M505ST11NW6%O5=M505ST
OS:11NW6%O6=M505ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)EC
OS:N(R=Y%DF=Y%T=40%W=F507%O=M505NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)`

`Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
HOP RTT       ADDRESS
1   158.74 ms 10.8.0.1
2   158.92 ms 10.10.84.163
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.21 seconds
`
## Questions
1. When was Snort created?
	- Ans: 1998 (simple google search)

2. Using Nmap on 10.10.84.163 , what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)
	- Ans: 80,2222,3389

3. Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up
	- Ans: No answer needed(Yes tho)

4. Experiment with different scan settings such as-A and -sV whilst comparing the outputs given
	- Ans: No answer needed(Above data for ref)

5. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?
	- Ans: Ubuntu

6. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?
	- Ans: Blog

7. Now use different scripts against the remaining services to discover any further information about them
	- Ans: No answer needed

Thank You!!!