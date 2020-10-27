import string
import numpy 
import math as m
alphabets = list(string.ascii_lowercase)


def encrypt(plain_text,key_list,row,column):
    plain_text_value = []
    for i in plain_text:
        plain_text_value.append(alphabets.index(i))
    plain_text_root = m.sqrt(len(plain_text_value))
    
    plain_text_value_matrix = numpy.array_split(plain_text_value,plain_text_root)
    plain_text_value_matrix_array = []
    for array in plain_text_value_matrix:
        plain_text_value_matrix_array.append(list(array))

    
    cipher_value_list_matrix = []


    for i in range(len(plain_text_value_matrix_array)):
        cipher_value = []
        cipher_value = numpy.matmul(key_list,plain_text_value_matrix_array[i])
        cipher_value_list_matrix.append(cipher_value)

    cipher_value_list =[]
    for array in cipher_value_list_matrix:
        cipher_value_list.append(list(array))

    for i in range(len(cipher_value_list)-1):
        cipher_value_list_final = cipher_value_list[i] + cipher_value_list[i+1]
    cipher_value_string = []
    for i in cipher_value_list_final:
        if i >= 26:
            cipher_value_string.append(alphabets[i%26])
        else:
            cipher_value_string.append(i)

    cipher_text=""
    return cipher_text.join(cipher_value_string)
    

def decrypt():
    pass






method = int(input ("what do you wants to do?\nEncrypt or Decrypt\npress 1 or 2: "))

if method == 1:
    plain_text = list(input("enter the plain text: "))
    print ("enter the key")
    row = int(input("Enter matrix row number: "))
    key_list = []
    column =  int(input("Enter matrix column number"))
    
    for i in range(row):
        data = []
        for j in range(column):
            data.append(int(input()))
        key_list.append(data)
    result = encrypt(plain_text,key_list,row,column)
    print("Encrypted text is:- "result)
elif method == 2:
    decrypt()
else:
    print("Wrong input")
