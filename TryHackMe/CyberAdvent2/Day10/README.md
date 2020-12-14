# Day 11 Challenge
## Don't be sELFish!

This challenge is about smb(Samba) enumeration.

Deploy the machine and first we scan for open ports using nmap

`nmap -sC -sV -O -A <Machine IP addr>`

Now we can see that there is smb port open so we can go ahead and enumerate it using tools like enum4linux which comes by default on kali distro or you can install it using

`apt install enu4linux`

After installing the enum4linux we can run it against our machine to enumerate users.

`enum4linx -a <machine IP addr>`

Now give it 2 mins to run the script. 

We can then see details about smb shares that are available.

Now try to connect to the smbshares using `smbclient`.

`smbclient //IPaddr/*sharename*`

Try to connect and see if there is any smb share with no password protection.

### Questions

1. Using enum4linux, how many users are there on the Samba server (MACHINE_IP)?
	- Ans 3

2. Now how many "shares" are there on the Samba server?
	- Ans: 4

3. Use smbclient to try to login to the shares on the Samba server (MACHINE_IP). What share doesn't require a password?
	- Ans: tbfc-santa

4. Log in to this share, what directory did ElfMcSkidy leave for Santa?
	- Ans: jingle-tunes


Thank You!