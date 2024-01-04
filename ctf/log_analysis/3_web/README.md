# Log Analysis 2
## Challenges
The walkthroughs in this lesson will use Linux commands to analyze the log.


### Challenge 1
<details>
<summary>What is the most common request method?</summary>
6633
</details>

<details>
<summary>Walkthrough</summary>

```bash
cat access.log | awk '{print $6}' | sort | uniq -c
```
- `cat access.log` - print the contents of `access.log` to the terminal.
- `awk '{print $6}'` - filter the output to the sixth column
- `sort` - sort the output
- `uniq -c` - count the number of lines which are the same
</details>

### Challenge 2
<details>
<summary>How much times was the status code 404 returned?</summary>
622
</details>

<details>
<summary>Walkthrough</summary>

```bash
cat access.log | awk '{print $9}' | sort | uniq -c
```
- `cat masscan.txt` - print the contents of `masscan.txt` to the terminal.
- `awk '{print $9}'` - filter the output to the ninth column
- `sort` - sort the output
- `uniq -c` - count the number of lines which are the same
</details>

### Challenge 3
<details>
<summary>What is the flag?</summary>
Sh3ll_Sh0cked_by_S1mpl1c1ty!
</details>

<details>
<summary>Walkthrough</summary>
Decode the base64 at line 7574.
</details>