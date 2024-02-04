On day 1 of N2H Linux, the group focused on the [Bandit wargames](https://overthewire.org/wargames/bandit/) from [OverTheWire](https://overthewire.org/wargames/). This game uses Linux commands to find flags on machines hosted by OverTheWire. The password to login into the next machine is found using the current user. For example, to login with the `bandit1` account, I must use the `bandit0` account to find the password for `bandit1`. This guide goes over the first 20 levels.
# Level 0
SSH into `bandit0` with password `bandit0`
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
There is a `readme` file in the home directory. Use `ls` to view the contents of the directory. 
```bash
ls
```
Then, use `cat` to view the contents of a file. Password for bandit1: `NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL`
# Level 1
SSH into `bandit1` with the text from the previous level.
```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```
The password is inside a file called `-`. View the contents of the `-` file with 
```bash
ls
cat ./-
```
Password for bandit2: `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi`
# Level 2
```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```
The password for the next level is stored in a file called `spaces in this filename`. To open it, use backslashes (`\`) to escape the spaces.
```bash
ls
cat spaces\ in\ this\ filename
```
Password for bandit3: `aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG`
# Level 3
```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```
The third level has a directory called `inhere`. Inside it, there is a file called `.hidden`. Files in Linux with a `.` in front of them are hidden from the file explorer and the `ls`. A user must use the `-a` flag to see all files.
```bash
cd inhere
ls -lah
cat .hidden
```
Password for bandit4: `2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe`
# Level 4
```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```
The `home` directory of `bandit4` has an `inhere` directory. There are 10 files inside it. One of them has human readable text. To find which file is human readable use the `find` command. Finally, `cat` the file with human readable text to get the password for `bandit5`. From the bandit5 page:
>The password for the next level is stored in the only human-readable file in the **inhere** directory

```bash
ls
cd inhere
ls
find . -type f -exec file {} +
```
The `find` command gave the following results:
```
./-file01: data
./-file02: data
./-file08: data
./-file06: data
./-file00: data
./-file04: data
./-file05: data
./-file07: ASCII text
./-file03: data
./-file09: data
```
```bash
cat ./-file07
```
The password for `bandit5` is `lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`.
Note: Finding the correct file through brute force is possible because there are 10 files in the directory. However, that is not the point of the challenge. 
# Level 5
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```
The OverTheWire page for bandit6 gives these instructions:
```
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
- human-readable
- 1033 bytes in size
- not executable
```
An online search for a command which searches for a file with those properties is
```bash
find . -type f -size 1033c ! -executable -exec file {} +
```
The result of the command:
```
./maybehere07/.file2: ASCII text, with very long lines (1000)
```
Only one file matches the criteria.
```bash
cat ./maybehere07/.file2
```
Password for `bandit6`: `P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU`
Note: Finding the correct file through brute force is possible because there are 20 directories with 6 files inside them. But it would take a long time and using the `find` command is the correct method to solve the challenge.
# Level 6
```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```
The website gives the instructions:
```
The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size
```
So the command
```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```
Explanation of the command:
- `find` - the find command.
- `/` - the root directory. Since the instructions say the file can be **somewhere on the server**, I need to start the search in the root directory.
- `-user bandit7` - search for files which the user `bandit7` is an owner of
- `-group bandit6` - search for files which the group `bandit6` is an owner of
- `-size 33c` - search for files which are 33 bytes in size
- `2>dev/null` - redirect `Permission denied` errors to `/dev/null`. Basically do not show errors.
There is one file which matches the criteria from the website
```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```
The password for `bandit7` is `z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`.
# Level 7
```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt** next to the word **millionth**

A command that will search the **data.txt** file for the word millionth is `grep`.
```bash
bandit7@bandit:~$ cat data.txt | grep "millionth"
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```
The password for `bandit8` is `TESKZC0XvTetK0S9xNwm25STk5iWrBvP`.
# Level 8
```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

This command will do what is required:
```bash
cat data.txt | sort | uniq -u
```
Explanation of the command:
- `cat data.txt` - print the data of **data.txt** to the screen
- `|` - the pipe symbol. The output of the command before the "pipe" (`|`) will be "piped" into the next command
- `sort` - sorts the output into alphabetical order. This is required for the next part.
- `uniq` - filters the output of the `sort` command for unique lines.
- `-u` - the `uniq` command by itself will output one line of every unique string from the file. The `-u` gives the string which occurs only **once**.
```bash
bandit8@bandit:~$ cat data.txt | sort | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```
The password for `bandit9` is `EN632PlfYiZbn3PhVK3XOGSlNInNE00t`.
# Level 9
```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several "=" characters

There are multiple methods to complete this level. I will explain how I solved it. I first used `grep` to filter out lines with `=` . However, the file has **binary data**, and grep will not search through binary files by default. Adding the `-a` or `--binary-files=text` options tells grep to search through binary files. This gives the password, except there is still binary data in the output. A command that removes binary data from the output of a command is the `strings` command. The combination of `strings` and `grep` will give the password.
```bash
bandit9@bandit:~$ strings data.txt | grep "======"
x]T========== theG)"
========== passwordk^
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```
The password for `bandit10` is `G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s`.
# Level 10
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

**base64** is a binary to a text encoding scheme that represents binary data in an ASCII string format. Linux has a `base64` command that accepts input from **stdout** (standard output and in this case the pipe `|` symbol) and can decode it. Using the `-d` modifier decodes the base64.
```bash
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```
The password for `bandit11` is `6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`.
# Level 11
```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

A cipher which rotates the letters in the text by 13 positions is known as the "Caesar Cipher". It is invented by Julius Caesar the earliest form of encryption. A search for a Caesar Cipher in bash results in
```bash
tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
```
Then pipe the output of `cat data.txt` into the command above results in the password.
```bash
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```
The password for `bandit12` is `JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv`.
# Level 12
```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

The file in this level has been compressed multiple times with gunzip (`gzip`), bunzip (`bzip2`), and `tar`. These are all commands which compress and decompress files. The **data.txt** file starts as a hexdump. To reverse the hexdump, pipe the output of cat into `xxd -r`. Also, put the file in the `tmp` directory because that is where writing files is allowed on this system.
```bash
cat data.txt | xxd -r > /tmp/file2
```
From there, the flag requires discovering the filetype of the file, renaming it to fit the naming scheme so the decompression program accepts it, and decompressing the file until the password is given. 
```bash
bandit12@bandit:~$ cat data.txt | xxd -r > /tmp/qwerty/file2
bandit12@bandit:~$ cd /tmp/qwerty
bandit12@bandit:/tmp/qwerty$ file file2
file2: gzip compressed data, was "data2.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 573
bandit12@bandit:/tmp/qwerty$ mv file2 file2.gz
bandit12@bandit:/tmp/qwerty$ gunzip file2.gz 
bandit12@bandit:/tmp/qwerty$ file file2
file2: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/qwerty$ mv file2 file3.bz
bandit12@bandit:/tmp/qwerty$ bunzip2 file3.bz 
bandit12@bandit:/tmp/qwerty$ file file3 
file3: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/qwerty$ mv file3 file3.gz
bandit12@bandit:/tmp/qwerty$ gunzip file3.gz 
bandit12@bandit:/tmp/qwerty$ file file3
bandit12@bandit:/tmp/qwerty$ mv file3 file3.tar
bandit12@bandit:/tmp/qwerty$ tar -xvf file3.tar 
data5.bin
bandit12@bandit:/tmp/qwerty$ file data5.bin 
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/qwerty$ mv data5.bin data5.tar
bandit12@bandit:/tmp/qwerty$ tar -xvf data5.tar
data6.bin
bandit12@bandit:/tmp/qwerty$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/qwerty$ mv data6.bin data6.bz
bandit12@bandit:/tmp/qwerty$ bunzip2 data6.bz 
bandit12@bandit:/tmp/qwerty$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/qwerty$ mv data6 data7.tar
bandit12@bandit:/tmp/qwerty$ tar -xvf data7.tar 
data8.bin
bandit12@bandit:/tmp/qwerty$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/qwerty$ mv data8.bin data8.gz
bandit12@bandit:/tmp/qwerty$ gunzip data8.gz 
bandit12@bandit:/tmp/qwerty$ ls
bandit12@bandit:/tmp/qwerty$ file data8 
data8: ASCII text
bandit12@bandit:/tmp/qwerty$ cat data8 
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```
The password for `bandit13` is `wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`.
# Level 13
```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```
>The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

There is a `SSH Private Key` file in bandit13's home directory. Use to use the `sshkey.private` file to login into `bandit14`. 
```bash
ssh bandit14@localhost -p 2220 -i sshkey.private
cat /etc/bandit_pass/bandit14
```
The password for `bandit14` is `fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`.
# Level 14
```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
```
>The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**

Use `telnet` to connect to port 30000 on localhost.
```bash
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq                                                                                           
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```
The password for `bandit15` is `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`.
# Level 15
```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
```
>The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

Use `openssl` and `s_client` to connect to the server with SSL encryption. 
```bash
openssl s_client -host localhost -port 30001
```
Then submit the password for the current level (bandit15)
```
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1
```
The password for `bandit16` is `JQttfApK4SeyHwDlI9SXGR50qclOAil1`.
# Level 16
```bash
ssh bandit16@bandit.labs.overthewire.org -p 2220
```
>The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

To find the open ports on the system, use `nmap`. 
```bash
bandit16@bandit:~$ nmap localhost -p 31000-32000
Starting Nmap 7.80 ( https://nmap.org ) at 2023-12-04 14:07 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```
The service on port `31790` returns a RSA private key when the password for the current level is entered.
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```
The identity file for `bandit17` is above.
# Level 17
Save the RSA key from the previous level into a file onto the local system. Then use it to login into `bandit17`.
```bash
ssh bandit17@bandit.labs.overthewire.org -p 2220 -i bandit17.private
```
>There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**

The Linux command to find the difference between two files is the `diff` command.
```bash
bandit17@bandit:~$ diff passwords.old passwords.new 
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
```
The password for `bandit18` is `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`.
# Level 18
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
```
This level automatically logs me out when I login through SSH. I can pass a command to the `ssh` command to automatically execute on the machine. Simply supply the command after the regular `ssh` command.
```bash
┌──(kali㉿kali)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 ls        
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
readme                                                                
┌──(kali㉿kali)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```
This can be automated by using the `sshpass` command.
```bash
┌──(kali㉿kali)-[~]
└─$ sshpass -p hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       
                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames
readme                                                                      
┌──(kali㉿kali)-[~]
└─$ sshpass -p hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme 
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       
                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```
The password for `bandit19` is `awhqfNnAbc1naukrpqDYcF95h7HoMTrC`.
# Level 19
```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
```
>To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

```bash
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
```
The password for `bandit20` is `VxCazJaVykI6W36BkBU0mJTCM8rR95XT`.
# Level 20
```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
```
>There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

This challenge requires two terminals. One to run the setuid binary and another to listen on a port and send the current password. 
![](bandit20.png)

The password for `bandit21` is `NvEJF7oVjkddltPSrdKEFOllh9V1IBcq`.
