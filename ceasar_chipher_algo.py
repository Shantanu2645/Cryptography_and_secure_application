import string
alphabets = list(string.ascii_lowercase)


def encrypt(plain_text_list,key):
    encrypt = []
    for i in plain_text_list:
        if i ==" ":
            encrypt.append(" ")
        else:
            cipher_value = alphabets.index(i) + key 
            if cipher_value >= 26:
                cipher_value = cipher_value % 26
                encrypt.append(alphabets[cipher_value])
                
            else:
                encrypt.append(alphabets[cipher_value])
    cipher_text = ""
    return cipher_text.join(encrypt)


def decrypt(cipherText, key):
    decrypt = []
    for i in cipherText:
        if i == " ":
            decrypt.append(" ")
        else:           
            plain_value = abs (alphabets.index(i) - key)
            absolute_plain_value = plain_value
            if absolute_plain_value % 26 == 0:
                decrypt.append(alphabets[0])
            else:
                if plain_value > 26:
                    plain_value = (((((absolute_plain_value - (absolute_plain_value % 26))/26) +1) *26) - absolute_plain_value)
                    
                    plain_value = int(plain_value)
                    decrypt.append(alphabets[plain_value])
                else:
                    dedecrypt.append(alphabets[plain_value])

    decrypted_plain_text= ""
    return decrypted_plain_text.join(decrypt)
            
            


try:

    method = int(input ("what do you wants to do?\nEncrypt or Decrypt\npress 1 or 2: "))

    if method == 1:
        plain_text = input("enter the plain text: ")
        plain_text_list = list(plain_text)
        key = int(input("Enter the key: "))
        result = encrypt(plain_text_list,key)
        print (result)

    elif method == 2:
        cipherText = input("enter the encrypted text: ")
        cipherText_list = list(cipherText)
        key = int(input("Enter the Decryption key: "))
        result = decrypt(cipherText, key)
        print (result)

    else:
        print("wrong input")

except EOFError:
    print ("wrong input")
except ValueError:
    print ("wrong input")
except KeyboardInterrupt:
    print("Exiting")


#Shantanu Dey Anik
