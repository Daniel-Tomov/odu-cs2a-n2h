On Day 2 of N2H Linux, we did Bash Scripting.
# first.sh
A simple bash script to echo "Hello World!"
# arguments.sh
A bash script with lists the contents of the directory supplied by the first argument. Usage:
```bash
./arguments.sh <dir>
```
# nmap.sh
Using arguments in a Bash script can be useful when using a command multiple times. An example would be an nmap command. Most of the times, only the IP address changes in the nmap command and the rest can be reused. Why not put it into a bash script? Usage:
```bash
./nmap.sh <ip address>
```
# forloops.sh
A demonstration of **for loops** in bash
# autoexpect
The `autoexpect` command can be related to a macro. It records keyboard inputs to the terminal and enters them when specific text shows on the screen.
One example shown that day was committing changes to a [git](https://git-scm.com/) repository. Git requires a username and password when pushing changes to a repository. Entering the username and password can be time consuming. This is where `autoexpect` comes in. The username and password are recorded and saved into an `expect` script. This script functions as the macro which can be used later. 