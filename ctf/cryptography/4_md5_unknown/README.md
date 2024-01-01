# Cracking Hashes when part of the text is known
## Introduction
Now that you know how to crack password hashes, lets crack hashes when we do not have a wordlist. What we will be doing is a bruteforce attack. However, the hashes can map to any string. CTF Competitions will sometimes be nice and give you part of the password to give you a head start.
## Charsets
The guide will use hashcat charsets and the known part of the string to crack the hashes.

*What is a charset?* A charset is a set of characters used to bruteforce passwords. When a charset is used, characters in the command are used to represent the unknown characters in the known password string. For example, there are four unknown numbers in `SKY-HQNT-####`. We can look at `hashcat -h` to view the charsets predefined in hashcat. 
```
l | abcdefghijklmnopqrstuvwxyz [a-z]
u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]
d | 0123456789                 [0-9]
h | 0123456789abcdef           [0-9a-f]
H | 0123456789ABCDEF           [0-9A-F]
s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
a | ?l?u?d?s
b | 0x00 - 0xff
```
To use a charset, type `?` before one of the characters above. Note: you may need to enter a `\` before the `?` to "escape" the `?`. 

Now use `hashcat` to bruteforce the hashes in the [hashes.txt](hashes.txt).
```bash
hashcat -m 0 -a 3 hashes.txt SKY-HQNT-\?d\?d\?d\?d
```
- `hashcat` - the program
- `-m 0` - the hashes are MD5, therefore going to use method `0`
- `-a 3` - using bruteforce
- `hashes.txt`- the file with the hashes
- `SKY-HQNT-\?d\?d\?d\?d` - the pattern of the plaintext with the charset rules
Note: if you do not see the hashes in the output, append `--show` to the end of the previous command to see them again.