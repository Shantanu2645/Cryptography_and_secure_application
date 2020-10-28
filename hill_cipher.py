import string
import numpy 
import math as m
from numpy.linalg import inv
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
    

def decrypt(cipher_text,key_list,row,column):
    cipher_text_value = []
    for i in cipher_text:
        cipher_text_value.append(alphabets.index(i))
    cipher_text_root = m.sqrt(len(cipher_text_value))

    cipher_text_value_matrix = numpy.array_split(cipher_text_value,cipher_text_root)
    cipher_text_value_matrix_array = []
    for array in cipher_text_value_matrix:
        cipher_text_value_matrix_array.append(list(array))
    
    
    for i in range(len(key_list)-1):
        key_list_full_list = key_list[i]+ key_list[i+1]
    key_minimum = min(key_list_full_list)
    # print (key_minimum)

    key_inverse = inv(numpy.array(key_list))*key_minimum

    
    key_inverse_final = []
    key_inverse_list = []
    for i in range(len(key_inverse)):
        for j in key_inverse[i]:
            if m.floor(j) < 0:
                key_inverse_list.append(m.floor(j+26))
            else:
                key_inverse_list.append(m.floor(j))

    key_inverse_final = numpy.array_split(key_inverse_list,column)
    
    key_determinent = int(numpy.linalg.det(key_inverse))
    
    key_inverse_final_list = []
    for array in key_inverse_final:
        key_inverse_final_list.append(list(array))
    print (key_inverse_final_list)
    

    
    #eculideans law

    d= 0
    r1 = 26
    r2 = int(key_determinent)
    R = 0
    t1 = 0
    t2 = 1 
    
    while(r1!=1):
        d = int(m.floor( r1/r2))
        R = r1%r2
        t = t1 - (t2*d) 
        r1 = r2 
        r2 = R
        t1 = t2
        t2 = t
    cipher_key_prosessed =[]
    cipher_key_prosessed = numpy.array(key_inverse_final_list)*3
    print (cipher_key_prosessed)






    



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
    print("Encrypted text is:- ",result)
elif method == 2:
    cipher_text = input("Please enter the Encrypted text: ")
    print ("Enter the key")
    row = int(input("Enter matrix row number: "))
    key_list = []
    column =  int(input("Enter matrix column number"))
    
    for i in range(row):
        data = []
        print("Enter data in row", i+1)
        for j in range(column):
            data.append(int(input()))
        key_list.append(data)
    result = decrypt(cipher_text,key_list,row,column)
else:
    print("Wrong input")
