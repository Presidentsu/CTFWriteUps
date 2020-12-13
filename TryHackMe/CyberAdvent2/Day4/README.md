# Day 4 Challenge!!!
## Santa's Watching

This challnege is all about fuzzing of directories or a specific part of a URL to find any hidden directories. 

Before we start this challenege make sure you have any fuzzing tools Iuse wfuzz and gobuster which you can install it with

apt install wfuzz
apt install gobuster


We were given a wordlist dowload the word list given in the description for further usage.

Now lets get started with the challenge!!!

Deploy the machine first we find any hidden directories using gobuster.

gobuster dir -u http://IP/api/ -w /usr/share/dirb/wordlists/common.txt -x .php 

We can find page /site-log.php

Now lets fuzz the api/site-log.php with date parameter.

#### command
wfuzz -c -z file,wordlist\(1\) -u http://IP/api/site-log.php?date=FUZZ

Once the fuzzing is done we can find the date where we can get the flag.

1. Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)?
	- Ans: wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ

2. Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?
	- Ans: site-log.php

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
	- Ans: THM{D4t3_AP1}
