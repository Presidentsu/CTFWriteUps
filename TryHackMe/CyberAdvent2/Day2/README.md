# Day2 Challenge
## The Elf Strikes Back! 

This one is about File Upload.

Once we deploy the machine we can access the upload pages using http://IP?id=ODIzODI5MTNiYmYw which allows us to upload images. Which generelay users upload only image files such as .jpg, .png or .bmp etc... And most of the times developers wont properly filter the files that to be uploaded onto servers. Now we exploit this lack of input validation to our use.

Now we take the [php-reverse-shell](https://github.com/pentestmonkey/php-reverse-shell) and change the IP addr to our system IP and proper port that you can listen on. I generally use port 4444(defualt).

Now lets rename the php file we created to something like .jpg.php or .png.php.

Now upload the image. 

To access the uploaded image we can try to find the hidden page using gobuster or dirbuster.

cmd: gobuster dir -u http://10.10.228.32/ -w /usr/share/dirb/wordlists/common.txt

Which gives us there is a page with /uploads/. Once we open the page we can see that out uploaded files are being stored in the that directory.

Before opening our reverse shell we need to set up netcat listener on port 4444(Or What ever port that you changed it to)

cmd: nc -lvp 4444

So to form the reverse shell we need to open the image.jpg.php file from the uploads 

After opening the link if we check our console we see that a reverse shell has been formed. 

1. What string of text needs adding to the URL to get access to the upload page?
	- Ans: ?id=ODIzODI5MTNiYmYw

2. What type of file is accepted by the site?
	- Ans: Image

3. In which directory are the uploaded files stored?
	- And: /uploads/

4. Activate your reverse shell and catch it in a netcat listener!
	- Ans: No answer needed.

5. What is the flag in /var/www/flag.txt?
	- Ans: THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}

### Conclusion:
Always keep a proper check on what files are allowed to be uploaded. By check keep a proper input validations and maintian WhiteLists.

Thank You! 