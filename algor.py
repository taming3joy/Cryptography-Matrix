from random import randint
import numpy as np
import pyperclip

def convert_message_to_matrix(mes):
    if len(mes)%3!=0:
        mes="{"*(3-len(mes)%3)+mes #Added "{" buffer to make len(mes) multiple of 3
    mes=[ord(x) for x in mes] #Convert each character in mes into its unicode representation
    mes=np.reshape(mes,(3,len(mes)//3)) #Reshaped into matrix size: (3 , len(mes)//3)
    return np.matrix(mes) #convert to numpy matrix

def convert_message_to_matrix_transposed(mes): #Used for encrypted message since it's transposed
    if len(mes)%3!=0:
        mes="{"*(3-len(mes)%3)+mes #Added "{" buffer to make len(mes) multiple of 3
    mes=[ord(x) for x in mes] #Convert each character in mes into its unicode representation
    mes=np.reshape(mes,(len(mes)//3,3)) #Reshaped into matrix size: (len(mes)//3 , 3)
    return np.matrix(mes) #convert to numpy matrix

def convert_matrix_to_message(mat): #Converting matrix back to message
    mat=np.array(mat).flatten() #Convert matrix into 1D array
    mat=[chr(x) for x in mat] #Convert each number into its character representation
    return ("".join(mat)).strip("{") #Removing the ddded "{" buffer

def generate_key_matrix(): #Generate a random matrix for key
    key_mat = np.matrix(np.reshape([randint(880,1023) for _ in range(9)],(3,3))) #Greek & Coptic unicode range = (880,1023)
    while np.linalg.det(key_mat)==0: #Make sure the key matrix is inversible, not a singular matrix (det = 0)
        key_mat = np.matrix(np.reshape([randint(880,1023) for _ in range(9)],(3,3))) #Greek & Coptic unicode range = (880,1023)
    return key_mat

def generate_key_string(): #Generate a random key string
    key_string = convert_matrix_to_message(generate_key_matrix()) 
    return key_string

def convert_key_matrix(key_string): #Convert key string into matrix
    key_mat=np.reshape([ord(x) for x in key_string],(3,3))
    return np.matrix(key_mat)

def encrypt_matrix(mat,key):
    transformed_mat = (key@mat).astype(int) #Apply 3x3 matrix linear transformation (the key) to message matrix
    transposed_mat = np.matrix_transpose(transformed_mat) #Transpose it to add complexity
    return transposed_mat

def decrypt_matrix(mat,key):
    inverse_key = np.linalg.inv(key) #Finding the inverse matrix of the key to undo the linear transformation
    transposed_mat = np.matrix_transpose(mat) #Transpose back the encrypted matrix
    transformed_mat = np.rint(inverse_key@transposed_mat).astype(int) #Apply the inversed key matrix back to the transposed matrix to obtain the original message matrix, then round the values back into int
    return transformed_mat

def encrypt_message(mes,key):
    key=convert_key_matrix(key) #Convert the key string into key matrix
    mat=convert_message_to_matrix(mes) #Convert the message into its matrix
    encrypted_mat = encrypt_matrix(mat,key) #Apply the encryption algorithm to optain the encrypted matrix
    encrypted_mes = convert_matrix_to_message(encrypted_mat) #Convert the encrypted matrix into a encrypted message
    return encrypted_mes

def decrypt_message(mes,key):
    key=convert_key_matrix(key) #Convert the key string into key matrix
    mat=convert_message_to_matrix_transposed(mes) #Convert the encrypted message into its matrix
    decrypted_mat = decrypt_matrix(mat,key) #Apply the decryption algorithm to optain the decrypted matrix
    decrypted_mes = convert_matrix_to_message(decrypted_mat) #Convert the decrypted matrix into the original message
    return decrypted_mes

#main
if __name__ == "__main__":
    print (f"Generated key= {generate_key_string()}")
    mes=input("Enter message to encrypt: ")
    key=input("Enter the secret key: ")
    encrypted_message = encrypt_message(mes,key)
    print (encrypted_message)
    pyperclip.copy(encrypted_message)

    print()

    mes=input("Enter message to decrypt: ")
    key=input("Enter the secret key: ")
    print (decrypt_message(mes,key))