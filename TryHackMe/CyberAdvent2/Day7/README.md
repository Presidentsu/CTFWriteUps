# Day 7 Challenge
## The Grinch Really Did Steal Christmas 

This challenge we were given a pcap file which has the captured packets in network and can be used too analyze in the future.

We can use wireshark or networkminer(for windows) to analyze pcap files.

Open the pcap file in wireshark.

## Questions

1. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
	- Ans: 10.11.3.2

2. If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?
	- Ans: http.request.method == GET

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?
	- Ans: reindeer-of-the-week

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?There's a lot of irrelevant data here - Using a filter here would be useful!
	- Ans: plaintext_password_fiasco

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?
	- Ans: SSH

6. What is on Elf McSkidy's wishlist that will be used to replace Elf McEager? (in pcap3)
	- Ans: Rubber ducky