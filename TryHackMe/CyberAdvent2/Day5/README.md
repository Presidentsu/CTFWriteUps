# Challenge 5!!!
## Someone stole Santa's gift list!!!

This challenge is all baout sql injection which allows account access with out their password.

Generally we can find the sqlinjection with a simple string as `1' OR 1=1 --#`

For this challeneg we need sqlmap. we can install sqlmap using `apt install sqlmap`

sqlmap does all our hardwork and gives us the entire database if the fields are vulnerable to SQLi

### Steps

Deploy the machine and open the IP.

We were given clue as /s**t***l

Now lets try /santapanel (cuz of the word 'panel' means admin access page) 

Now we can see there is a page /santapanel


We can see the login form which we can bypass using

Username: Santa' OR 1=1 --
Password: /Some random chars/

Setup brupsuite and intercept the request while you try to input random data into it and save the file. 

Now we can use this saved request for sqlmap and dump all the database.

#### command for sqlmap

sqlmap -r <Filename>--tamper=space2comment --dump-all --dbms sqlite

Dumps us the data table.

## Quesitons
1. Without using directory brute forcing, what's Santa's secret login panel?
	-Ans: /santapanel

2. Visit Santa's secret login panel and bypass the login using SQLi
	-Ans: Not needed (but do it!!! mentioned above how to do it!!!)

3. How many entries are there in the gift database?
	-Ans: 22

4. What did Paul ask for?
	-Ans: Github Ownership

5. What is the flag?
	-Ans: thmfox{All_I_Want_for_Christmas_Is_You}

6. What is admin's password?
	-Ans: EhCNSWzzFP6sc7gB

### Conclusion

ALWAYS DO PROPER INPUT VALIDATION!!!!