# Cryptography 1 - Ciphers
## Introduction
Ciphers have been around for a long time. Julius Caesar was the first human to cipher his messages to make them hard to read. The receiving party would need to know how the message was ciphered to decrypt it back to the original. Today's ciphers are much more complicated. They put the message into columns and move the columns around 

## Vocabulary

- Plaintext - the original message before it was ciphered
- Ciphertext - the message after it is ciphered
## Ceasar Cihper
As discussed before, Julius Caesar was the first to encipher messages. For each letter in his message, he replaced it with the letter 3 characters after it. For example, an `a` (the first letter in the alphabet) will becomem a `d` (the 4th character; 1+3=4). The recieving party would subract 3 from the characters in the ciphertext and have the original message. If the number is less than 1 or greater than 26, then continue at the end or the beginning of the alphabet respectively. 

Caesar Cipher in Python
```python
def encrypt(letter, shift):
        if letter == " ": return " "
        temp = ord(letter.lower()) # convert the letter to a number
        temp = temp + shift # apply the shift
        temp = temp - 97 # the letter "a" is 65 in decimal. The alphabet begins at 1. Therefore need to convert.
        temp = temp % 26 # If the shift is more than 26, the cipher starts at the beginning of the alphabet. 
        temp = temp + 65 # convert the number back to valid decimal
        temp = chr(temp) # convert the decimal number to a letter
        return temp
def decrypt(letter, shift):
        if letter == " ": return " "
        temp = ord(letter.lower()) # convert the letter to a number
        temp = temp - shift # apply the shift
        temp = temp - 97 # the letter "a" is 65 in decimal. The alphabet begins at 1. Therefore need to convert.
        temp = temp % 26 # If the shift is more than 26, the cipher starts at the beginning of the alphabet. 
        temp = temp + 65 # convert the number back to valid decimal
        temp = chr(temp) # convert the decimal number to a letter
        return temp
```
Example code in [caesar.py](caesar.py).

Watch the video for more information [youtube.com/watch?v=fR8rVR72a6o](https://www.youtube.com/watch?v=fR8rVR72a6o)
## Vigenere Cipher
The Vigenere cipher is different from the Caesar Cipher in that the same letter is likely not going to be ciphered into the same letter every time. This cipher uses a code word and a table. The code word can be any word or phrase. Start writing the code word letter by letter above or below each letter in the message. Repeat the word for the entire length of the message. [The table](vigenere.jpg) has the alphabet on the first column and first row. The enciphered letter is where the letters from the code word and message line up. 

To decipher a ciphertext, align the ciphertext letter with the letters from the code word is. The letter on the other side (column or row) is the letter for the 

Watch the video for more information [youtube.com/watch?v=rccRQcyKB5g](https://www.youtube.com/watch?v=rccRQcyKB5g)
## Substitution Cipher
A substitution cipher replaces each character in the plaintext with a different character from the alphabet. The character `a` can map to a `u` and `b` can map to `g`. 

Substitution cipher in Python
```python
def encrypt(letter):
        if letter == " ": return " "
        index = int(alphabet.index(letter.lower()))
        return key[index:index + 1]

def decrypt(letter):
        if letter == " ": return " "
        index = int(key.index(letter.lower()))
        return alphabet[index:index + 1]
```
Example code in [substitution.py](substitution.py).
## Atbash Cipher

The Atbash cipher is a substitution cipher, but the key is the alphabet reversed.
## Enigma
The Enigma cipher was used by the Germans during the World Wars. The Enigma is a machine with rotors and a plugboard which scramble each letter each character in the plaintext. There are **158,962,555,217,826,360,000** possible combinations. The amount of combinations made it impossible to break by hand. In addition, the code was changed every day. Generals had a list of which combinations to use on which day of the month.
Despite the large number of combinations, the Engima had a weakness. A plaintext letter could not be encrypted into itself. In addition, the Germans included the weather report in their daily morning message. This meant there was a known set of characters in the message. The Allies used these two weaknesses to guess the daily codes and decrypt the encrypted messages.

Watch this video for more information [youtube.com/watch?v=ybkkiGtJmkM](https://www.youtube.com/watch?v=ybkkiGtJmkM).