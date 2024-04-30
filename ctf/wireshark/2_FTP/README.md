# Wireshark 2

## Challenges
### Challenge 1
<details>
<summary>Which user successfully logged in?</summary>
user1
</details>

<details>
<summary>Walkthrough</summary>
Open the packet capture with Wireshark. Right click any packet and then `Follow -> TCP Stream`. Go through the streams until you see a valid login. (stream 1)
</details>

### Challenge 2
<details>
<summary>What is the password for the above user?</summary>
metropolis
</details>

<details>
<summary>Walkthrough</summary>
Open the packet capture with Wireshark. Right click any packet and then `Follow -> TCP Stream`. Go through the streams until you see a valid login. (stream 1)
</details>

### Challenge 3
<details>
<summary>What is the name of that file that was uploaded successfully?</summary>
compcodes.zip
</details>

<details>
<summary>Walkthrough</summary>
Open the packet capture with Wireshark. Right click any packet and then `Follow -> TCP Stream`. Go through the streams until you see a file being uploaded and was successful. (stream 1)
</details>

### Challenge 4
<details>
<summary>What is the username of the second user that logged in?</summary>
anonymous
</details>

<details>
<summary>Walkthrough</summary>
Open the packet capture with Wireshark. Right click any packet and then `Follow -> TCP Stream`. Go through the streams until you see a file being uploaded and was successful. (stream 4)
</details>

### Challenge 5
<details>
<summary>What file was deleted?</summary>
bank.cap
</details>

<details>
<summary>Walkthrough</summary>
Open the packet capture with Wireshark. Right click any packet and then `Follow -> TCP Stream`. Go through the streams until you see a file being deleted and was successful. (stream 1)
</details>