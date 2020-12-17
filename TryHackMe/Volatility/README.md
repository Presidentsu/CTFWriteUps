# Volatility

This challenge covers on how to analyze memory dumps using volatility tool

Lets start our challenge by downloading [volatility tools](https://github.com/volatilityfoundation/volatility)

After that download the memory dump sample.

Now lets unzip the file and we have a cridex.vmem

First lets try to find what image we were given.

This can be done using imageinfo plugin. 

`./volatility_2.6_lin64_standalone -f cridex.vmem imageinfo`

Gives us 
`
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/root/Desktop/volatility_2.6_lin64_standalone/cridex.vmem)
                      PAE type : PAE
                           DTB : 0x2fe000L
                          KDBG : 0x80545ae0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2012-07-22 02:45:08 UTC+0000
     Image local date and time : 2012-07-21 22:45:08 -0400                                                            
`

So the suggested profiles are  WinXPSP2x86, WinXPSP3x86

Now to determine the exact memory dump we can use `--proifle=<versions>` and use any plugin. If the there are no errors and the results show up then we can say that is the one indeed.

So I use pslist plugin to veirfy and it checks out.

So our image is from WinXPS2x86

Now lets have alook at the processes that were running during the time of memory dump for that we can use pslist plugin.

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 pslist > pslist.txt`

let us open pslist.txt and have a look at the processes running at the time image disk was taken.

So the process ID 584 isthe malicious one

We can view the active connections of the machine using plugin netscan but this OS doesnt support netscan but for windows 8 or more it supports netscan.

Now lets take a look at the hidden process that run (As malware tries to hide) using `psxview` plugin.

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 psxview > psxscan.txt`

lets have alook at the psxscan.txt to seeif there is any 'flase' condition set which can suggest that the process can be malicious.

We can see that PID 584 csrss.exe stands out.

Now you can use ldrmodule plugin to see if there is any process injection.

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 ldrmodules > ldrmodules.txt`

Now lets use apihooks plugin to find unexpected patches in the standard system DLLs Hooking module: unknown. (Note: this one take sometime but do have a look for better understanding).

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 apihooks > apihooks.txt`

After this process now lets try to find malicious injection using malfind plugin and lets dump it in our current directory  

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 malfind -D .`
 
So it dumped 12 process for to analyse.

Now lets try to dump the dll's related to the malicous dll ie PID 584.

For thisone we will use dlllist plugin to dump the dlls.

`./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 --pid=584 dlldump -D .`

Dumps us all the dll related to that process ID and lets upload these dll's to [virus total](virustotal.com) to find the malicious one out.

## Questions (Task 3-4)

### Task 3

1.  First, let's figure out what profile we need to use. Profiles determine how Volatility treats our memory image since every version of Windows is a little bit different. Let's see our options now with the command `volatility -f MEMORY_FILE.raw imageinfo`.
	- Ans: No answer needed.

2. Running the imageinfo command in Volatility will provide us with a number of profiles we can test with, however, only one will be correct. We can test these profiles using the pslist command, validating our profile selection by the sheer number of returned results. Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE pslist`. What profile is correct for this memory image?
	- Ans:  WinXPSP2x86

3. Take a look through the processes within our image. What is the process ID for the smss.exe process? If results are scrolling off-screen, try piping your output into less
	- Ans: 368

4. In addition to viewing active processes, we can also view active network connections at the time of image creation! Let's do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE netscan`. Unfortunately, something not great is going to happen here due to the sheer age of the target operating system as the command netscan doesn't support it.
	- Ans: No answer needed.

5. It's fairly common for malware to attempt to hide itself and the process associated with it. That being said, we can view intentionally hidden processes via the command `psxview`. What process has only one 'False' listed?
	- Ans: csrss.exe

6. In addition to viewing hidden processes via psxview, we can also check this with a greater focus via the command 'ldrmodules'. Three columns will appear here in the middle, InLoad, InInit, InMem. If any of these are false, that module has likely been injected which is a really bad thing. On a normal system the grep statement above should return no output. Which process has all three columns listed as 'False' (other than System)?
	- Ans: csrss.exe

7. Processes aren't the only area we're concerned with when we're examining a machine. Using the 'apihooks' command we can view unexpected patches in the standard system DLLs. If we see an instance where Hooking module: `<unknown>` that's really bad. This command will take a while to run, however, it will show you all of the extraneous code introduced by the malware.
	- Ans: No answer needed

8. Injected code can be a huge issue and is highly indicative of very very bad things. We can check for this with the command `malfind`. Using the full command `volatility -f MEMORY_FILE.raw --profile=PROFILE malfind -D <Destination Directory>` we can not only find this code, but also dump it to our specified directory. Let's do this now! We'll use this dump later for more analysis. How many files does this generate?
	- Ans: 12

9. Last but certainly not least we can view all of the DLLs loaded into memory. DLLs are shared system libraries utilized in system processes. These are commonly subjected to hijacking and other side-loading attacks, making them a key target for forensics. Let's list all of the DLLs in memory now with the command `dlllist`
	- Ans: No answer needed

10. Now that we've seen all of the DLLs running in memory, let's go a step further and pull them out! Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE --pid=PID dlldump -D <Destination Directory>` where the PID is the process ID of the infected process we identified earlier (questions five and six). How many DLLs does this end up pulling?
	- Ans: 12

## Task 4

1. Upload the extracted files to VirusTotal for examination.
	- Ans: No answer needed

2. Upload the extracted files to Hybrid Analysis for examination - Note, this will also upload to VirusTotal but for the sake of demonstration we have done this separately. 
	- Ans: No answer needed.

3. What malware has our sample been infected with? You can find this in the results of VirusTotal and Hybrid Anaylsis.
	- Ans: Cridex


All in all this was nice challenge helps you understand how we can use volatility for forensic analysis.

Thank you <3
