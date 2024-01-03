# Memory Analysis 2 - Volatility3
This challenge is from the National Cyber League Fall 2023 season.
## Introduction
Volatility3 is an upgrade from Volatility2. Volatility3's commands are different from Volatility2. After all, Volatility3 is written in Python3 while Volatility2 is in Python2. However, while Volatility3's commands are more complex, I think they allow for greater compatibility for operating systems.

## Setup
1. Download Volatility3 from [github.com/volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3).
2. Open a terminal on your computer and navigate to the folder where you downloaded the Volatitlity3
3. Create a Python virtual environment. I like to call them `env`, but you can name it what you wish. The command is:
```bash
python3 -m venv env
```
4. Activate the virtual environment
- Linux:

```bash
source env/bin/activate
```
    
- Windows
  - Powershell (You may need to enable Powershell script execution)

  ```powershell
  env\Scripts\activate.ps1
  ```
  - Enable Powershell script execution:

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
  ```

  - Command Prompt

  ```cmd
  "env\Scripts\activate.bat"
  ```

Finally, install the required dependancies for volatility3.

```bash
pip3 install -r requirements.txt
```

## Challenges
Download the memory dump [https://drive.google.com/file/d/1mjEFVUpRpk8fFIkKrUduvIKw1RcERnxG](https://drive.google.com/file/d/1mjEFVUpRpk8fFIkKrUduvIKw1RcERnxG/view?usp=sharing) and start solving the challenges. If you get stuck, each challenge has a walkthrough.

This page may be a helpful reference: [https://blog.onfvp.com/post/volatility-cheatsheet/](https://blog.onfvp.com/post/volatility-cheatsheet/).


### Challenge 1
<details>
<summary>What is the PID of the suspicious process ("DB Browser ...")?</summary>
3768
</details>
<details>
<summary>Walkthrough</summary>
Looking at the reference, run the command that lists the running processes in the memory dump.

```bash
python3 vol.py -f memdump.mem windows.psscan
```
</details>

### Challenge 2
<details>
<summary>What is the computer name?</summary>
DESKTOP-OT97GG3
</details>
<details>
<summary>Walkthrough</summary>
This challenge has two parts. The first one is finding how to read the registry. The second is finding the key that stores the computer name.

The reference has a command for getting a specific key from the registry. 
```bash
python3 vol.py -f memdump.mem windows.registry.printkey ‑‑key “”
```

What registry key holds the computer name? A Google search shows it is ```CurrentControlSet\Control\ComputerName```. However, searching for that registry key has no results. What about going back to the root, `CurrentControlSet`? What does that result in? It seems `CurrentControlSet` has a link to `ControlSet001`. So, replace `CurrentControlSet` with `ControlSet001`. You get `ControlSet001\Control\ComputerName`. Searching the memory dump for the key results in having to go another level deeper, either `ComputerName` or `ActiveComputerName`. Both will get you the answer. 
</details>

### Challenge 3
<details>
<summary>What is the username with ID 1001? The user is also running the process from challenge 1.</summary>
liber8hacker
</details>
<details>
<summary>Walkthrough</summary>
Looking at the reference, there is not a command that hints at how to get users. The challenge mentions the user is also running the process from challenge 1. Maybe that is important?

Yes, it is! You could dump the [SIDs](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers) (a unique value that is used to identify any security entity that the Windows operating system can authenticateate). [^1]

[^1]: https://www.techtarget.com/searchsecurity/definition/security-identifier

```bash
python3 vol.py -f memdump.mem windows.psscan
```
</details>

### Challenge 4
<details>
<summary>What is the password for the previous challenge's username?</summary>
avatar2
</details>
<details>
<summary>Walkthrough</summary>
Passwords are stored in the regisry. The regisry is made of three files called "hives." There is a command that dumps the password hashes for all the users. Note: you need to have installed the required dependancies for volatility3 for this command to work.

```bash
python3 vol.py -f memdump.mem windows.hashdump.Hashdump
```

You will get the password hashes for the users on the system. The LM password hashes are disabled. We can see this by the LM hash for the user in the previous question is ```aad3b435b51404eeaad3b435b51404ee```. Therefore, we have to crack the NT hash. Let's use `hashcat` to crack it. Note: refer to the hash cracking lessons in the `cryptography` module for more examples.

```bash
hashcat -m 1000 -a 0 214a7d83f1c36a5f7071137d7c6e5ae6 /usr/share/wordlists/rockyou.txt
```

- `-m 1000` - cracking NT hashes
- `-a 0` - using a wordlist
- `214a7d83f1c36a5f7071137d7c6e5ae6` - the NT hash from Volatility
- `/usr/share/wordlists/rockyou.txt` - the location of rockyou.txt

The password will be in the output. If you don't see it, append `--show` to the end of the command. 
</details>

### Challenge 5
<details>
<summary>What name (first and last) maps to the username from above?</summary>
tom hess
</details>
<details>
<summary>Walkthrough</summary>
Refer to the cheatsheet for a command to list the files.

```bash
python3 vol.py -f memdump.mem windows.filescan
```

It returns a lot of files. Let's filter the output with `grep` for files on the `Desktop`.

```bash
python3 vol.py -f memdump.mem windows.filescan | grep "Desktop"
```

There is a file on the Desktop called `black_book.db`. Let's extract it. Note the address on the left of the output from the command above. I will use `0xe0003f5a9d00` as the address. You also need to make a folder called `memory_dump` for Volatility3 to put the file into.

```bash
python3 vol.py -f memdump.mem -o memory_dump windows.dumpfiles.DumpFiles --virtaddr 0xe0003f5a9d00
```

What is the file type of the dumped file?

```bash
file memory_dump/<file_name>
```

Both of them seem to be SQLite3 files. Let's try both

```bash
sqlite3 *.dat
SQLite version 3.44.0 2023-11-01 11:23:50
Enter ".help" for usage hints.
sqlite> .tables
Error: database disk image is malformed
sqlite> .exit
```

The file ending in `.dat` is not a valid sqlite3 database. Let's try the other one.

```bash
SQLite version 3.44.0 2023-11-01 11:23:50
Enter ".help" for usage hints.
sqlite> .tables
aliases  book
```

This one has tables in it. Using SQL we can get the flag.

```sqlite3
sqlite> select * from aliases;
1|grace
2|wasp
3|ace
4|torpedo
5|diablo
6|liber8
7|alpha
8|cloud
9|indie
10|nobody
sqlite> select * from book;
1|robert|sturm
2|laura|replogle
3|delmar|couch
4|troy|enriquez
5|leslie|mullis
6|tom|hess
7|steve|scott
8|gloria|hampton
9|barbara|walters
10|johanna|weiland
```

Using both the `aliases` and `book` tables, we can see the `liber8` user is at index `6`, and the first and last name at index `6` is `tom hess`. 
</details>