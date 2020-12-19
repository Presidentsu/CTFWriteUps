# Day 19

## The Naughty or Nice List 

This challenge is about Server-Side Request Forgery

Now lets fireup the machine

Try to put anything in the search and see how URL changes

It gave me this

`http://10.10.28.168/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3Dggg`

And when URL Decode it it gives us...

`http://list.hohoho:8080/search.php?name=ggg`

Now let to change list.hohoho to something like example.com

It gives us security error hmm lets try localhost...

Same error Lets try to change it to lists.hohoho same error

Let try to change it to list.hohohoho Oh it shows server can't resolve the host!!! So the bypassmechanisim that is going right now is it's checking for URL to start with list thats it.

So we need a way to RD a link that starts its subdomain with list to 127.0.0.1

So to make our work easy TryHackMe have us list.localhost.me which RD's to 127.0.0.1

So if we paste `http%3A%2F%2Flist.hohoho.localtest.me` after 
`proxy=`

We get the list that santa wants now lets try to login.

Which was mentioned in the text (Alert !!!!)

Now login with username Santa and the password given by Elf

### Questions

...

	1. What is Santa's password?
		- Ans: Be good for goodness sake!
	2. What is the challenge flag?
		-Ans: THM{EVERYONE_GETS_PRESENTS}
...

Thank You <3