# Log Analysis 1

## Challenges
The walkthroughs in this lesson will use Python to analyze the log.
### Challenge 1
<details>
<summary>What is the most common source IP address?</summary>
169.254.169.123
</details>

<details>
<summary>Walkthrough</summary>
There are many ways to complete a scripting challenge, here is the way I did it.

```python
log = open("iptable.log", "r").readlines()
srcIPs = {}
for entry in log:
    srcip = entry.split("SRC=")[1].split(" ")[0]
    try:
        srcIPs[srcip] += 1
    except Exception:
        srcIPs[srcip] = 1
dstPorts = dict((v,k) for k,v in dstPorts.items())

print(dstPorts)
```

Manually look through the output for the source IP (value in dictionary) with the highest number (key in dictionary).
</details>

### Challenge 2
<details>
<summary>What is the most common destination port?</summary>
123
</details>

<details>
<summary>Walkthrough</summary>
There are many ways to complete a scripting challenge, here is the way I did it.

```python
log = open("iptable.log", "r").readlines()
dstPorts = {}
for entry in log:
    dstport = entry.split("SPT=")[1].split(" ")[0]
    try:
        dstPorts[dstport] += 1
    except Exception:
        dstPorts[dstport] = 1
dstPorts = dict((v,k) for k,v in dstPorts.items())
print(dstPorts)
```

Manually look through the output for the port (value in dictionary) with the highest number (key in dictionary).
</details>