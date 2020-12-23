# Day 23 - The Grinch strikes again! 

Let's deploy the machine.

now lets connect to the machine via remmina

Once you connect to the machine lets open the ransomeware note.txt and for bitcoin address it legit has a base64 encoded string xD so lets decode it using 

`echo 'bm9tb3JlYmVzdGZlc3RpdmFsY29tcGFueQ==' | base64 -d`

Gives us the the decoded string

LEts open TaskScheduler and look at the tasks that are scheduled.

After lookking into it we can see the needed answers 

Now open the disk management and assign a name to the backup partition to some name like random latter here I gave it U:

Go to View section in nav bar of File Explorer and check option to show hidden folders

Now we can see a hidden folder with name `confidential`

Now lets restore the previous version using properties tab and go to previous version and click restore for the pervious verison and have alook into it and we can find the password!!!

### Quesions

...

	1. Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?
		- Ans: nomorebestfestivalcompany
	2. At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?
		- Ans: .grinch
	3. Inspect the properties of the scheduled task. What is the location of the executable that is run at login?
		- Ans: C:\Users\Administrator\Desktop\opidsfsdf.exe
	4. There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?
		- Ans: 7a9eea15-0000-0000-0000-010000000000
	5. Assign the hidden partition a letter. What is the name of the hidden folder?
	 	- Ans: Confidential
	 6. Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?
	 	- Ans: m33pa55w0rdIZseecure!

...


Thank you <3