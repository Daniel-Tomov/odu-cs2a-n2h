# Memory Analysis 1
This challenge is from CloudCTF.

# What is memory?
To start, let's ask the question, *what is computer memory?* According to *Crucial*,

> RAM (which stands for Random Access Memory) is the familiar acronym for [computer memory], which is the temporary storage in your computer that gives applications a place to store and access data on a short-term basis.

Anytime you open a program, such as Chrome or a text editor, the data they need to store is put into RAM. Programs need memory to function, or else they start to forget!

# The Lab
## Goals for this lab
- Setup Volatility
- Extract data from a running process in a memory dump using Volatility

## Lab Setup
1. Download [Volatility](https://github.com/volatilityfoundation/volatility).
2. Since Volatility is written in Python2, we need to install pip2 because most Linux distributions do not come with pip2 installed. If you are on Windows, I'm sorry. Download the [pip2 installer](https://bootstrap.pypa.io/pip/2.7/get-pip.py). Then run

```bash
python2 get-pip.py
```

3. Go into the directory where you downloaded Volatility and run the command below to install the dependancies.
```bash
pip2 install pycryptodome
```
4. Download the [memory dump](https://drive.google.com/file/d/1Pm6xHgYBT3tV84QQy9m4Kvtrfjk4XV1B) for the challenge.

# Challenges
There is a resource on the Internet that explains how to solve the challenges. It is not a writeup, but someone explaining how to do the same steps below.

# Challenge 1

<details>
<summary>What version of Windows is the image of?</summary>
Win7SP1x86_23418
</details>

<details>
<summary>Walkthrough</summary>
You can identify the Windows version of the image with

```bash
vol.py -f memories.dat imageinfo
```

</details>

## Challenge 2
<details>
<summary>What is the PID of Notepad?</summary>
3216
</details>

<details>
<summary>Walkthrough</summary>
You can identify the running processes with

```bash
vol.py -f memories.dat --profile <version name from above> pslist
```
</details>

## Challenge 3
<details>
<summary>What text was being edited in Notepad? Flag is in flag{...} format</summary>
flag{Sum_D@TA_Nev3r_Gits_2_disk}
</details>

<details>
<summary>Walkthrough</summary>
You can dump the memory contents of a process with 

```bash
mkdir dump_dir
vol.py -f memories.dat --profile Win7SP0x86 procdump --pid 3216 --dump-dir dump_dir
```

The challenge says the flag format is `flag{...}`. We can search the dump for that string. 

```bash
strings -e l dump_dir/3216.dmp | grep "flag"
```
</details>