So the infamous Advent of Cybers Day 1 challenge is web exploitation. 

So once we deploy the machine.
We can open the site using the machine IP.

The questions we were given are.

1. Deploy your AttackBox (the blue "Start AttackBox" button) and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open FireFox on the AttackBox and copy/paste the machines IP into the browser search bar.
	
	-Ans: No need.

2. What is the name of the cookie used for authentication?
	-Once we register with new account here I regestered with username and Password 'Testing'.
	Now lets have a look at Inspect Elements and then to storage we can find the cookie that is being used.
	So the Cookie name is auth
	
	Ans: auth

3. In what format is the value of this cookie encoded?
	- When we see the value of the cookie mine is '7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2254657374696e67227d' hmm which looks alot like hexadecimal. 
	
	Ans: Hexadecimal

4. Having decoded the cookie, what format is the data stored in?
 	-Now lets decode to text form hexadecimal using online [tools](http://www.unit-conversion.info/texttools/hexadecimal/).
 	Once I decoded it gave me this string 
 		-{"company":"The Best Festival Company", "username":"Testing"} Which is in JSON format.

 	Ans: JSON.

5. What is the value of Santa's cookie?
 	- When we take a look at the decoded cookie it says username to be Testing which was our registered one. Now lets change it to santa and encode it again. Which gives us:
 		-7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d

 	Ans: 7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d

 	Now we can put this modified cookie value inplace of the original one and refreshing the page gives us the access to santa account. Now we can do what Santa can do. 

6. What is the flag you're given when the line is fully active?
 	- Now lets activate the full assembly line we get the flag to be THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}

 	Ans: THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}.


That's it! Try to participate in the Advent of Cyberchallenege all of the challeneges are moslty basic and they kinda teach you basic stuff about hacking and stuff :-)

