# Day 21 Challenge - Time for some ELForensics 

Deploy the machine

And lets connect to it via remmina

Lets open powershell and set our location to Documents folder,

`Set-Location .\Documnets\`

Now lets see the hash of the file in the text document present in there.

Now lets see the hash of the deebee.exe using the tools present in C:\Tools folder

`C:\Tools\strings64.exe -accepteula .\deebee.exe`

If we look close enough we can see the flag in the format THM{*************}

Now lets see the Stream name of this executable using the command

`Get-Item -Path .\deebee.exe -Stream *`

We get the Stream name: hidedb

Now lets see what happens we run this database connector file.

`wmic process call create $(Resolve-Path .\deebee.exe:hidedb)`

Gives us our final flag...


### Questions

...

	1. Read the contents of the text file within the Documents folder. What is the file hash for db.exe?
		- Ans: 596690FFC54AB6101932856E6A78E3A1
	2. What is the file hash of the mysterious executable within the Documents folder?
		- Ans: 5F037501FB542AD2D9B06EB12AED09F0
	3. Using Strings find the hidden flag within the executable?
		- Ans: THM{f6187e6cbeb1214139ef313e108cb6f9}
	4. What is the flag that is displayed when you run the database connector file?
		- Ans: THM{088731ddc7b9fdeccaed982b07c297c}
...

Thank you <3