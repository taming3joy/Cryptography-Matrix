from random import randint
import numpy as np
import pyperclip

def convert_message_to_matrix(mes):
    if len(mes)%3!=0:
        mes="{"*(3-len(mes)%3)+mes #Added "{" buffer to make len(mes) multiple of 3
    mes=[ord(x) for x in mes] #Convert each character in mes into its unicode representation
    mes=np.reshape(mes,(3,len(mes)//3)) #Reshaped into matrix size: 3 x len(mes)//3
    return np.matrix(mes) #convert to numpy matrix

def convert_message_to_matrix_transposed(mes): #Used for encrypted message since it's transposed
    if len(mes)%3!=0:
        mes="{"*(3-len(mes)%3)+mes #Added "{" buffer to make len(mes) multiple of 3
    mes=[ord(x) for x in mes] #Convert each character in mes into its unicode representation
    mes=np.reshape(mes,(len(mes)//3,3)) #Reshaped into matrix size: len(mes)//3 x 3
    return np.matrix(mes) #convert to numpy matrix

def convert_matrix_to_message(mat):
    mat=np.array(mat).flatten()
    print (mat)
    mat=[chr(x) for x in mat]
    return ("".join(mat)).strip("{")

def generate_key_matrix():
    key_mat = np.matrix(np.reshape([randint(174,591) for _ in range(9)],(3,3)))
    while np.linalg.det(key_mat)==0:
        key_mat = np.matrix(np.reshape([randint(174,591) for _ in range(9)],(3,3)))
    return key_mat

def generate_key_string():
    key_string = convert_matrix_to_message(generate_key_matrix())
    return key_string

def convert_key_matrix(key_string):
    key_mat=np.reshape([ord(x) for x in key_string],(3,3))
    return np.matrix(key_mat)

def encrypt_matrix(mat,key):
    transformed_mat = (key@mat).astype(int)
    transposed_mat = np.matrix_transpose(transformed_mat)
    return transposed_mat

def decrypt_matrix(mat,key):
    inverse_key = np.linalg.inv(key)
    transposed_mat = np.matrix_transpose(mat)
    transformed_mat = np.rint(inverse_key@transposed_mat).astype(int)
    return transformed_mat

def encrypt_message(mes,key):
    key=convert_key_matrix(key)
    mat=convert_message_to_matrix(mes)
    encrypted_mat = encrypt_matrix(mat,key)
    encrypted_mes = convert_matrix_to_message(encrypted_mat)
    return encrypted_mes

def decrypt_message(mes,key):
    key=convert_key_matrix(key)
    mat=convert_message_to_matrix_transposed(mes)
    decrypted_mat = decrypt_matrix(mat,key)
    decrypted_mes = convert_matrix_to_message(decrypted_mat)
    return decrypted_mes

#main
# print (f"Generated key= {generate_key_string()}")
# mes=input("Enter message to encrypt: ")
# key=input("Enter the secret key: ")
# encrypted_message = encrypt_message(mes,key)
# print (encrypted_message)
# pyperclip.copy(encrypted_message)

print()

mes=input("Enter message to decrypt: ")
key=input("Enter the secret key: ")
print (decrypt_message(mes,key))