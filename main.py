'''
   Copyright (c) 2020, Primesh Shamilka,
   email: primeshs.17@cse.mrt.ac.lk
   All rights reserved. https://github.com/PrimeshShamilka/
   
   Revision history:
	  April 28th, 2020: initial version.
'''

from monoalphabetic_cipher import converter
import matplotlib.pyplot as plt
import numpy as np

key = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def count_characters(string):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_dic = {}
    for i in string:
        if i.islower():
            i.upper()
        if i in letters:
            try:
                letter_dic[i] = letter_dic[i] + 1

            except:
                letter_dic[i] =  1
    return letter_dic


#
#
#  Encrypting the Original text using the given Key
#
#

plain_text_file = open("/home/primesh/plain_text.txt", "r", encoding='utf-8')
cipher_text_file = open("/home/primesh/cipher_text.txt", "w", encoding='utf-8')

plain_text = plain_text_file.read()
cipher_text = converter(key,plain_text, 'encrypt', letters)
cipher_text_file.write(cipher_text)

plain_text_file.close()
cipher_text_file.close()


#
#
#  Count the occurrence of each letter and plot it.
#
#

letter_dic = count_characters(cipher_text)
print(letter_dic)

objects = ('A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z')
y_pos = np.arange(len(objects))
performance = []
for i in objects:
    performance.append(letter_dic[i])

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.title('Character frequency distribution')
plt.show()


#
#
#  Identify 5 ciphertext characters with the highest frequency
#  and Prepare a partial decryption of the ciphertext with only the
#  identified top-5characters replaced with their corresponding
#  plaintext guesses.
#
#
#  using Relative frequecy of letters in english, the most appeard 
#  5 characters are e,t,a,r,i
#  source - https://en.wikipedia.org/wiki/Letter_frequency
#
#

sorted_letter_dic = {k: v for k, v in sorted(letter_dic.items(), 
                        key=lambda item: item[1],reverse =True )}

most_used_letters = ""
counter = 5
for i in sorted_letter_dic:
    if counter ==0:
        break
    most_used_letters = most_used_letters + i
    counter = counter - 1

print (most_used_letters)
part_dec_key = "ETARI"
part_dec_text = converter(part_dec_key, cipher_text, 'decrypt', most_used_letters)
part_dec_txt_file = open("Partially_decrypted.txt", "w", encoding="utf-8")
part_dec_txt_file.write(part_dec_text)
part_dec_txt_file.close()
