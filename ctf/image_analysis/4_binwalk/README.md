# Image Analysis 4


## Challenges
### Challenge 1
<details>
<summary>What text is the flag?</summary>

</details>

<details>
<summary>Walkthrough</summary>

Use binwalk to extract any embedded data in the image.

```bash
binwalk --dd=".*" image.png
```
- `--dd=".*"` - extract all file types

</details>
