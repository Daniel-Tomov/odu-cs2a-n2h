# Log Analysis 2

## Challenges
The walkthroughs in this lesson will use Linux commands to analyze the log.
### Challenge 1
<details>
<summary>List the ports in the log in order from least to greatest</summary>
22,80,443
</details>

<details>
<summary>Walkthrough</summary>
Look at the log for the ports.
</details>

### Challenge 2
<details>
<summary>What is the most common open port?</summary>
443
</details>

<details>
<summary>Walkthrough</summary>

```bash
cat masscan.txt | awk '{print $4}' | sort | uniq -c
```
- `cat masscan.txt` - print the contents of `masscan.txt` to the terminal.
- `awk '{print $4}'` - filter the output to the fourth column
- `sort` - sort the output
- `uniq -c` - count the number of lines which are the same
</details>