# Disk Analysis 1
This challenge is from VT's Summit CTF 2023.

## Setup
1. Install FTK Imager on Windows. Sorry Linux, there is not an easy way to get FTK Imager for PC. I also could not use Autopsy to complete the challenge.
2. Download the [disk image](https://drive.google.com/file/d/1BgP3UnFl8W9N-LzTwZUg_XP7rxdx2oAM) and extract it. 
3. Open FTK imager and open the unzipped image file into the program.

## Challenges
### Challenge 1
<details>
<summary>What is the flag?</summary>
MBR_tr1ksy_h1D1Ng_7l4g
</details>
<details>
<summary>Walkthrough</summary>

1. Extract `extraction.rar` using FTK Imager. Or you can directly extract the next disk image from the archive within FTK Imager and skip step 2.
2. Extract the next disk image from the archive.
3. Open the second image and scroll down in the hex window area. Flag is there.
</details>