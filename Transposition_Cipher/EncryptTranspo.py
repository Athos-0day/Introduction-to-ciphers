#Implementation of encryption by transposition

#Retrieving values
print("Give a key value and the associated message")
Key = int(input("The value of the key: "))
Message = input("The message you want to encrypt: ")

#variable initialization 
Length = len(Message)
k = 0
n = 0
EncryptMessage = ""

while n<Key :
    while k<=(Length//Key) :
        
        if (n+k*Key)<Length :
            EncryptMessage += Message[n+k*Key]
        k+=1
        
    k=0
    n+=1

print(EncryptMessage)






