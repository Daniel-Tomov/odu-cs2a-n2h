shift = 3

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

plaintext = "ODU Cybersecurity Student Association Noobs To  Hackers"
ciphertext = ""
for i in plaintext:
	tmp = encrypt(i, shift)
	ciphertext += tmp
print(ciphertext)


plaintext = ""
for i in ciphertext:
        tmp = decrypt(i, shift)
        plaintext += tmp
print(plaintext)
