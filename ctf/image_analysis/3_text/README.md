# Image Analysis 2
This challenge is from CloudCTF.

## Challenges
### Challenge 1
<details>
<summary>What text is hidden in the image?</summary>
WW91J3JlIGFsbW9zdCB0aGVyZS4uLiBqamV5e2NteF95cG9wd3dfZ3JfbHdjX21rZXl0fQ==
</details>

<details>
<summary>Walkthrough</summary>
View the raw image contents by printing them to the terminal with `cat`.

```bash
cat eyeendere.png
```

</details>

### Challenge 2
<details>
<summary>What do the characters from the previous challenge decode to?</summary>
flag{not_always_in_the_image}
</details>

<details>
<summary>Walkthrough</summary>

The characters from before are base64. Once decoded, it still looks like giberish. The image gives a "key" of `EYESPY`. A cipher that uses a key is the Vigenere cipher. You can use a website such as [CyberChef](https://gchq.github.io/CyberChef) to decode and decipher the characters from before.

</details>