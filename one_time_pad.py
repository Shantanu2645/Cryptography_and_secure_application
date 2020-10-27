import string
#importing alphabets
alphabets = list(string.ascii_letters)                                          

#function for encryption
def encrypt(plain_text_list,key):                                               
    key_list = []
    #making list of index number of the letters of key
    for i in key:                                                              
        key_list.append(alphabets.index(i))            
    count = 0

  

        

    encrypt = []
    #process of encryption
    for i in plain_text_list:                                                   
        #if any space in the plain text, it will include in the list
        if i ==" ":                                                             
            encrypt.append(" ")
        else:
            #calculating the ciphertext value by adding plaintext value and key value
            cipher_value = alphabets.index(i) + int(key_list[count])            
            if cipher_value >= 26:
                cipher_value = cipher_value % 26
                encrypt.append(alphabets[cipher_value])
                
            else:
                encrypt.append(alphabets[cipher_value])
        count = count + 1
    cipher_text = ""

    return cipher_text.join(encrypt)                                            

#Function for encryption
def decrypt(cipherText_list, key):                                              
   
    key_list = []
    #making list of index number of the letters of key
    for i in key:
        key_list.append(alphabets.index(i))                                    
                     
    count = 0

    decrypt = []


    for j in cipherText_list:
        if j == " ":
            decrypt.append(" ")

        else:           

            #making plaintext value by subtracting cipherkey value from ciphertext value
            plain_value =  alphabets.index(j) - int(key_list[count])            
            
            if plain_value < 0 :
                plain_value = plain_value + 26
                decrypt.append(alphabets[plain_value])
                
            else:
                decrypt.append(alphabets[plain_value])
            
        count = count + 1

    decrypted_plain_text= ""
    return decrypted_plain_text.join(decrypt)
            
            


try:

    method = int(input ("what do you wants to do?\nEncrypt or Decrypt\npress 1 or 2: "))
 
 #Taking input for Encryption
    if method == 1:                                                            
        plain_text = input("enter the plain text: ")
        plain_text_list = list(plain_text)
        key = list(input("Enter the key: ")) 
        result = encrypt(plain_text_list,key)
        print (result)

#taking input for Decryption
    elif method == 2:                                                           
        cipherText = input("enter the encrypted text: ")
        cipherText_list = list(cipherText)
        key = list(input("Enter the Decryption key: "))
        if " " in key:
            print("Invalid key with space")
        else:
            result = decrypt(cipherText_list, key)
            print (result)

    else:
        print("wrong input")

except EOFError:
    print ("wrong input")
except ValueError:
    print ("wrong input. key is not valid (space included)")
except KeyboardInterrupt:
    print("Exiting")


#Shantanu Dey Anik
