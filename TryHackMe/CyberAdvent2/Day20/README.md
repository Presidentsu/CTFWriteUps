# Day 20 - PowershELlF to the rescue 

This challenge is about PowerShell and blue teaming.

Lets deploy the machine and connect it to ssh

After getting into the shell

First lets move to Docmunets using 

`Set-Location Documents`

Now lets see any hidden files in the location using

`Get-ChildItem -File -Hidden`

And now lets read the contents on the file e1fone.txt using

`Get-Content -Path e1fone.txt`

Now lets go to Desktop 

`cd ..`
`Set-Location Desktop`

Now lets see the hidden folders using 

`Get-ChildItem -Directory -Hidden`

Nice we can see one hidden Directory lets go to that directory using

`Set-Location elf2wo`

lets see the files in the directory and if any thier contents.

`Get-Content -Path e70smsW10Y4k.txt`

Now lets go to Windows Files

`cd C:\Windows\`

`cd .\System32\`

Now lets find the hidden directory which has number 3 in it.

`Get-ChildItem -Directory -Hidden -Filter "*3*"`

Gives us our folder

Lets go to the folder and see the files using

`Get-ChildItem -File -Hidden`

It gives us 1.txt and 2.txt  which are huge ass files to sit and count lets use

`Get-Content 1.txt | Measure-Object -words`

To see the contents at a specified lines we can use the following command

(Get-Content 2.txt)[number of line we need]

At first glance for the last task I thought I have to see for the same strings but after looking at the hint as my answer was wrong it said we have to use pattern (Press F for me :-|).

`Get-Content 2.txt | Select-String -Pattern "redyryder"`

I dont why but this took so much time to exec :-( but hey PATIENCE <3

### Questions

...

	1. Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?
		- Ans: 2 front teeth
	2. Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?
		- Ans: Scrooged
	3. Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)
		- Ans: 3lfthr3e
	4. How many words does the first file contain?
		- Ans: 9999
	5. What 2 words are at index 551 and 6991 in the first file?
		- Ans: Red Ryder
	6. This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)
		- Ans: red ryder bb gun

...

#### Thank you <3 