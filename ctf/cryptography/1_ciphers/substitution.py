alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "nzxtlociedqjuaphwksbrvgmyf"
def encrypt(letter):
	if letter == " ": return " "
	index = int(alphabet.index(letter.lower()))
	return key[index:index + 1]

def decrypt(letter):
	if letter == " ": return " "
	index = int(key.index(letter.lower()))
	return alphabet[index:index + 1]

plaintext = "ODU Cybersecurity Student Association Noobs To Hackers"
ciphertext = ""
for i in plaintext:
        tmp = encrypt(i)
        ciphertext += tmp
print(ciphertext)

plaintext = ""
for i in ciphertext:
        tmp = decrypt(i)
        plaintext += tmp
print(plaintext)
