import random

#We will test our Cipher with some quotes 
#Ten quotes and we will test various keys 
Quotes1 = "It sounds plausible enough tonight, but wait until tomorrow. Wait for the common sense of the morning."
Quotes2 = "They always say time changes things, but you actually have to change them yourself."
Quotes3 = "The strongest of all warriors are these two — Time and Patience."
Quotes4 = "All animals are equal, but some animals are more equal than others."
Quotes5 = "Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them"
Quotes6 = "Because there are three classes of intellects: one which comprehends by itself; another which appreciates what others comprehend; and a third which neither comprehends by itself nor by the showing of others; the first is the most excellent, the second is good, the third is useless."
Quotes7 = "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth."
Quotes8 = "Deep in the human unconscious is a pervasive need for a logical universe that makes sense. But the real universe is always one step beyond logic."
Quotes9 = "You forget what you want to remember, and you remember what you want to forget."
Quotes10 = "Some birds are not meant to be caged, that's all. Their feathers are too bright, their songs too sweet and wild. So you let them go, or when you open the cage to feed them they somehow fly out past you. And the part of you that knows it was wrong to imprison them in the first place rejoices, but still, the place where you live is that much more drab and empty for their departure."

List = [Quotes1,Quotes2,Quotes3,Quotes4,Quotes5,Quotes6,Quotes7,Quotes8,Quotes9,Quotes10]

#Now we will take 10 keys and put them in an other list 
KeyList = []
for Valeur in List :
    KeyList.append(random.randint(1,len(Valeur)))

EncryptDecryptList = []
n = len(KeyList)

def EncryptTranspo(Message,Key) :

    #variable initialization 
    Length = len(Message)
    k = 0
    n = 0
    EncryptMessage = ""

    while n<Key :
        while k<=(Length//Key) :
            print(n+k*Key)
            if (n+k*Key)<Length :
                EncryptMessage += Message[n+k*Key]
            k+=1
        
        k=0
        n+=1
    return EncryptMessage

def DecryptTranspo(CipherText,Key) :

    #Initialisation of the values
    Length = len(CipherText)
    Rows = 0
    Columns = 0
    Novalue = Key*((Length//Key)+1) - Length
    PlainText = [""] * ((Length//Key)+1)

    for Caracters in CipherText :
        PlainText[Columns] += Caracters
        Columns += 1

        if Columns==((Length//Key)+1) or (Columns==(Length//Key) and Rows>=(Key-Novalue)) :
            Columns = 0 
            Rows +=1

    Message = ""
    for val in PlainText :
        Message += val
    return Message

ValidTest = 0

for i in range(0,n) :
     EncryptDecryptList.append(DecryptTranspo(EncryptTranspo(List[i],KeyList[i]),KeyList[i]))
     if EncryptDecryptList[i]==List[i] :
         ValidTest += 1

if ValidTest==n :
    print("Success")
else :
    print("Error")


