# Day 18 Challenge

This challenge is also about reverse engineering.

Deploy the machine and connect to its RDP using remmina(linux) or RDP on windows

Now lets see what the app TBC using dot as ILSpy is not opening :-( 

Now once you open the application using dotpeek expand all the branches and try to find the application password.

Once you load iit go to 

-> Crackme -> Mainform -> textBoxKey_TextChanged(... function and have a look at the disassembled function.

You can see both the password and flag with loging in xD


### Questions

...

	1. Open the "TBFC_APP" application in ILspy and begin decompiling the code.
		- Ans: No answer needed
	2. What is Santa's password?
		- Ans: santapassword321
	3. Now that you've retrieved this passwor, try to login...What is the flag?
		- Ans: thm{046af}
...

Thank you <3