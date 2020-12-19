#first install prettytable (pip install prettytable)
# C = Cipher text
# M = message/plaintext
# e = public key
# d = private key
# 1. let P & Q are the prime number
# 2. n = P*Q 
# 3. modulo, FAI(n) = (P-1)(Q-1)
# Prime number P condition, 0 < P < FAI(n) and gcd (FAI(n))
import math as m
from prettytable import PrettyTable

def encryption(m,e,n):
    M = m
    E = e
    N = n
    C = (M**E)%N
    print("Your messege is",C)

def decryption(c,d,n):
    C= c
    D = d
    N = n
    M = (C**D)%N
    print("Your messege is",M)


def eculid_table(fai_n, e):
    d= 0
    r1 = fai_n
    r2 = e
    R = 0
    t1 = 0
    t2 = 1 
    
    table = PrettyTable(['d','r1','r2','R','t1','t2','T'])
    while(r1!=1):
    
        d = int(m.floor( r1/r2))
        R = r1%r2
        t = t1 - (t2*d) 
        table.add_row([d,r1,r2,R,t1,t2,t])
        r1 = r2 
        r2 = R
        t1 = t2
        t2 = t
    table.add_row(['',r1,r2,'',t1,t2,''])

    print(table)
    print("t1= ",t1)
    return t1
    


def prime_check(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return False  
                break  
        else:  
            return True
    else:  
        return False

def gcd(a,b):
    if(b==0): 
        return a 
    else:
        return gcd(b,a%b)



p =  int(input("enter value of p: "))

p_prime = prime_check(p)

if p_prime == True:
    q = int(input("enter value of q: "))
    q_prime = prime_check(q)
    if q_prime == True:
        n = p*q
        fai_n = (p-1)*(q-1)
        gcd_value = gcd(fai_n,2)
        e= int(input("enter value of e: "))
        e_prime = prime_check(e)
        if e_prime == True:
            if 0 < e < fai_n:
                if e != p and e !=q and e != gcd_value :
                    print("p= ",p)
                    print("q= ",q)
                    print("n= ",n)
                    print("FAI(n) = (P-1)(Q-1) = ",fai_n)
                    
                    t1_eculid = eculid_table(fai_n,e)
                    
                    
                    if t1_eculid > fai_n:
                        d = t1_eculid % fai_n
                        print ("t1 > fai(n) so:")
                        print ("d = t1 mod Fai(n)= ",d)

                    else:
                        d = t1_eculid + fai_n
                        
                        print ("d = t1 + Fai(n) = ",d)                  
                    
                    continue_program = int(input("Do you wish to continue yes(1) or no(2)"))
                    if continue_program == 1:
                        
                        user_con =  int(input("wHAT DO you wants to do encryption(1) or decryption(2): "))
                        if user_con == 1 :
                            m = int(input("Enter your messege (int): "))
                            encryption_result = encryption(m,e,n)
                            

                        elif user_con == 2:
                            c = int(input("Enter your cipher messege (int): "))
                            decryption_result = decryption(c,d,n)
                            
                        else:
                            print("Wrong input, exiting")





                    elif continue_program == 2:
                        print("Exiting")
                    else:
                        print("Wrong input, exiting")
                    
                else:
                    print ("e is not valid") 
            else:
                print ("e is not valid") 
        else:
                print ("e is not valid")
    elif q_prime == False:
        print("q is not prime number")
            



elif p_prime == False:
    print("p is not prime number")
