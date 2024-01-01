# Cracking Windows Passwords
The following is a challenge from the Technology Student Association Cybersecurity competition in 2022.
## Introduction
The Windows operating system is used by a large part of the world. It has the largest market share in the consumer space. 
## The Lab
You are given a zip file with the `SYSTEM` and `SAM` registry hives from a computer. These files contain the settings for the computer. If you are using a Windows computer, you can find these files in `C:\Windows\System32\config`.

> Caution! Be extremely careful when editing the registry. It contains the configuration for your operating system and making a wrong change or deleting the files may result in an nonoperational operating system.

In addition to Windows settings, the registry also contains the password hashes for user accounts. One way to obtain the password hashes for a system is by using the `SYSTEM` and `SAM` files. Then use `samdump2` to extract the hashes from the files.
```bash
$ samdump2 SYSTEM SAM
*disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
LAB:1000:aad3b435b51404eeaad3b435b51404ee:25700d98aafce3db5ffad8a949731c6d:::
flag_user:1002:aad3b435b51404eeaad3b435b51404ee:032c72c6d11bf91e740ea34c523f9c21:::
```
We will be cracking the password hash for the `flag_user` user using `hashcat`. But first we need to identify the hash. That is simple. Windows computers use `NTLM` to hash their passwords. There are a few parts to the line for the `flag_user` user. *What do they mean?*

`flag_user:1002:aad3b435b51404eeaad3b435b51404ee:032c72c6d11bf91e740ea34c523f9c21:::`
- The colons are separators for different pieces of information
- `flag_user` - the name of the user
- `1002` - the identifier of the user. Identifiers start at 1000
- `aad3b435b51404eeaad3b435b51404ee` - the LM hash of the user's password. LM is not secure anymore and is not used. It is disabled by default but can be enabled. 
- `032c72c6d11bf91e740ea34c523f9c21` - the NT hash of the user's password
Because the LM hash is disabled by default, lets crack the NT hash.
1. Save the output of `samdump2` to a file. You can use the `>` to direct the output to a file. `samdump2 SYSTEM SAM > hashes.txt`
2. Find the correct hash code for NTLM in hashcat. You can use `hashcat -h`. <details><summary>The code is</summary>1000</details>
3. Run the command on `hashes.txt` with `rockyou.txt` as the wordlist
```bash
hashcat -m 1000 -a 0 hashes.txt rockyou.txt
```
If you miss the cracked password, append `--show` to the end of the command to view the passwords.
