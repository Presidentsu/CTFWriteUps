# Day 22 - Elf McEager becomes CyberElf 

Deploy the machine and connect it to via RDP/remmina(linux)

Now we can see the name of the folder and lets decode it using [cyberchef](https://gchq.github.io/CyberChef).

The encoding used here is Base64

So Use Recipe From Base64

We get the password for the KeyBase folder. Now lets opne the folder and see the rest of the passwords.

For server password we have something that looks like HEX so lets Decode it using Hex recipe in CyberChef.

We now have password of the server

Now lets take a look at the email password it looks like it is encoded in HTML Entities

So use the recipe From HTML Entities and now we have another password which is for email

Now for the final flag lets have a look at the Note as the password says nothing to look in here.

At the begining it says eval, string and Charcode. This is Charcode encoded so lets use From Charcode recipe

Wait, Now we have something similar to a scirpt with same charcode so lets decode that part once again 

This time we now have a URL to some github repository which gives us the final flag.


### Questions

...

	1. What is the password to the KeePass database?
		- Ans: thegrinchwashere
	2. What is the encoding method listed as the 'Matching ops'?
		- Ans: Base64
	3. What is the decoded password value of the Elf Server?
		- Ans: sn0wM4n!
	4. What is the decoded password value for ElfMail?
		- Ans: ic3Skating!
	5. Decode the last encoded value. What is the flag?
		- Ans: THM{657012dcf3d1318dca0ed864f0e70535}
...

Thank you <3