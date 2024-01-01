# Encoding
## Introduction
There are many different ways to represent characters. The characters we use daily are ASCII. There are 128 (7 bits) ASCII characters. There are other types of encodings; ways to display characters. They are: 
- binary - uses bits. Either a 0 or a 1
- octal - uses the numbers `0` through `7`. Can also be represented by three binary digits.
- decimal - uses the numbers `0` through `9`. We use the decimal numbering system to count.
- hexadecimal - uses 16 characters; the numbers `0` through `9` and letters `a` through `f`.
- base64 - uses 64 characters; all numbers, lowercase and uppercase and lowercase letters, `+`, and `/`. You may see an equals sign at the end of base64 text. The `=` represents padding. Padding is needed because base64 can not always represent the characters in the original message perfectly.
## Converting
When converting from one encoding to another, It is easiest to convert first to binary and then to whichever target encoding you need. Of course, you would not need to do this if you have a [conversion table](ASCII-Conversion-Chart.pdf).

### ASCII to hexadecimal
Lets convert `A` to hexadecimal.
First, convert the character to binary. The letter `A` is `01000001` in binary, or `65` in decimal. From there, split the binary into groups of four. `01000001` split up is `0100` and `0001`. `0100` is `4` and `0001` is `1` in hexadecimal. Combine them together and you get `41`. Use the [conversion table](ASCII-Conversion-Chart.pdf) to check the answer. Correct!

Converting to other formats is similar.