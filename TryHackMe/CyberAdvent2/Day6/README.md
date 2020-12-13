# Day 6 Challenge
## Be careful with what you wish on a Christmas night 

This challenge is all about Cross Site Scripting also known as XSS.

To do this challenge we need OWASP ZAP which comes by default in kali linux distro.

Once we deploy the machine. Open the webpage and have a look at the input fields and try to put something similar to this 

`<script>alert('Yo this field is vuln to XSS!!!')</script>`

And see if there is  any popup/alerts with 'Yo this is....' if it shows the alert then that respective input field in vulnerable to XSS attack.

We can see the input form of name "q" is vulnerable to XSS.

Now lets give the machine URL to OWASP ZAP it finds for vulnerabilities by fuzzing data.

### Quesitons

1. What vulnerability type was used to exploit the application?
	- Ans: Stored Cross-site Scripting

2. What query string can be abused to craft a reflected XSS?
	- Ans: q

3. Launch the OWASP ZAP Application
	- Ans: No answer needed

4. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?
	- Ans: 2

5. Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?
	- Ans: No answer needed
		- Try to give this as input `<script>alert("Make a wish")</script>` 