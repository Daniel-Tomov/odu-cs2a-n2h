# Password Cracking with a Wordlist
## Introduction
Companies do not store user's passwords in plaintext (or at least they should not). Passwords are stored as hashes.

*What is a hash?* A hash is a string of text that represents a specific string of characters.

*What creates hashes?* A *Hash function* does. It is a function that produces a hash string from an original string. A hash function is considered strong if it is not possible to have two different strings produce the same hash. Lastly, hash functions are "trapdoor functions." It is not possible to reverse a trapdoor function. Hence the name "trapdoor." Once the door closes, it is not possible to go back.

*So if it is not possible to get the original message from a hash string, how do people crack passwords?* Hackers obtain password hashes by hacking into databases. They then have a wordlist with millions of possible passwords. Hash cracking programs hash each line in the wordlist and compare it to the obtained hashes. If it matches, then the obtained hash from the database maps to the specific word in the wordlist.

## Cracking Passwords
There are two popular hash cracking programs. One is `John the Ripper` or `JTR`, or simply `John`. The other is `hashcat`. Both programs can use a wordlist, use a pattern, or bruteforce to crack hashes.
### John the Ripper
1. Open your Kali Linux virtual machine (Kali has `john` preinstalled). 
2. Download the [hashes](hashes.txt) above. In it you will see what seems like random characters. While they seem random, they are actually hashes. They have different lengths because they are from different hash functions.
3. Download a wordlist. [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) is a popular wordlist because it contains passwords from a real breach. Using any of those passwords could lead to one of your passwords being cracked in a breach.
4. Now run the command to start cracking the hashes.
```bash
john hashes.txt --wordlist=<path_to_rockyou.txt>
```
What the command means:
- `john` - the name of the program
- `hashes.txt` - the file with the hashes
- `--wordlist=<path_to_rockyou.txt>` - using `rockyou.txt` as the wordlist
You can view the hash to password map with
```bash
john hashes.txt --show
```
You may notice that some of the passwords are not shown in the output. *Why is that?* You need to specifically tell `john` to crack those specific types of hashes. 

While running the first command, you may have noticed `john` telling you it noticed other types of hashes in `hashes.txt`.
```
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-Linkedin"
Use the "--format=Raw-SHA1-Linkedin" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "ripemd-160"
Use the "--format=ripemd-160" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "has-160"
Use the "--format=has-160" option to force loading these as that type instead
Warning: only loading hashes of type "Raw-SHA1", but also saw type "LM"
Use the "--format=LM" option to force loading hashes of that type instead
Warning: only loading hashes of type "Raw-SHA1", but also saw type "dynamic=md5($p)"
Use the "--format=dynamic=md5($p)" option to force loading hashes of that type instead
Warning: only loading hashes of type "Raw-SHA1", but also saw type "cryptoSafe"
Use the "--format=cryptoSafe" option to force loading hashes of that type instead
```
### Hashcat
The other program that cracks hashes is `hashcat`. You already have the hashes and wordlist downloaded, so lets look at a command blueprint.
```bash
hashcat -m <hash type> -a <mode> <hashes> <wordlist>
```
- `hashcat` - name of the program
- `-m` - the type of hash being cracked. You can get a list of hashes and their codes by doing `hashcat -h` (the hashcat help command)
- `-a` - the method used to crack hashes. Possible methods are 
```
0 | Straight
1 | Combination
3 | Brute-force
6 | Hybrid Wordlist + Mask
7 | Hybrid Mask + Wordlist
9 | Association
```
- `<hashes>` - the file with the hashes
- `<wordlist>` - the wordlist file
Here is the full command:
```bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```
- `-m 0` - cracking MD5 hashes. Again, use `hashcat -h` to get a list of hashes and their codes
- `-a 0` - using the `Straight` method (going through the wordlist line by line, hashing each line, and comparing the resulting hash to the list of hashes)
One of the hashes will be in the output along with the word corresponding to the hash.
<details>
<summary>MD5 password</summary>
335ff997de9fcf280151d9375a24a564:wingardiumleviosa
</details>

Lets crack the rest of the hashes. You can use a tool like `hash-identifier` to identify the rest of the hashes.
```bash
hash-identifier 849ab79edcc427ebdc6d44459a9eb3ea8fd42847
hash-identifier b2316366ab970c525575e370cef6d95b
hash-identifier f3d698a7c826e1843384afaaeb7d673ea633ecf2346dcd6258951439d918833865b248f56e797269110f9b3db6dc72bdef3bdafdddf6c42908b1bb381943d8f9
```
<details>
<summary>849ab79edcc427ebdc6d44459a9eb3ea8fd42847 hash type</summary>
SHA-1
</details>
<details>
<summary>b2316366ab970c525575e370cef6d95b hash type</summary>

This one is MD4
It may have not been at the top of the list when you ran the command. `MD5` have been first. This is an important lesson to learn. The answer is not always obvious in CTF competitions. You have to try everything to get the flag.

</details>
<details>
<summary>f3d698a7c826e1843384afaaeb7d673ea633ecf2346dcd6258951439d918833865b248f56e797269110f9b3db6dc72bdef3bdafdddf6c42908b1bb381943d8f9 hash type</summary>
SHA-512
</details>

Now that you the hash types, you need to know the code for the hashes. Run `hashcat -h` to find them. You can pipe the output into `grep` to filter the output. For example,

```bash
hashcat -h | grep "SHA"
```
will filter the output for lines with "SHA". 