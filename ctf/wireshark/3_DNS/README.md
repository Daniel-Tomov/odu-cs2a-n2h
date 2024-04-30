# Wireshark 3
This challenge is from Virginia Tech's Summit CTF 2023
## Challenges
### Challenge 1
<details>
<summary>What is the flag?</summary>
SummitCTF{Sus_D0ma1n_n4mes}
</details>

<details>
<summary>Walkthrough</summary>

The capture has dns requests to seemingly random domains. However, upon inspection of the domain of the first packet (which is `VGhlIGZsYWcg.Tscc1QuycZN4.summit`), the first part (or third-level domain) is base64 for `The flag `. The second-level domain is occurs a few times. We can use Linux commands to go through the capture and extract those packets with `Tscc1QuycZN4` in the domain.

```bash
└─$ tshark -r EscapingTheMatrix.pcap | awk '{print $12}' | grep "Tscc1QuycZN4"
VGhlIGZsYWcg.Tscc1QuycZN4.summit
eW91IGhhdmUg.Tscc1QuycZN4.summit
YmVlbiB3YWl0.Tscc1QuycZN4.summit
aW5nIGZvciBp.Tscc1QuycZN4.summit
cyAuLi4gUGF1.Tscc1QuycZN4.summit
c2luZyBmb3Ig.Tscc1QuycZN4.summit
ZHJhbWF0aWMg.Tscc1QuycZN4.summit
ZWZmZWN0IC4u.Tscc1QuycZN4.summit
LiA6IFN1bW1p.Tscc1QuycZN4.summit
dENURntTdXNf.Tscc1QuycZN4.summit
RDBtYTFuX240.Tscc1QuycZN4.summit
bWVzfQ==.Tscc1QuycZN4.summit
```

Based on the length of the output, the decoded text could be one sentence. Use CyberChef to remove the extraneous characters and decode the base64 to get the flag.

Result: `The flag you have been waiting for is ... Pausing for dramatic effect ... : SummitCTF{...}`
</details>