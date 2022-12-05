#Implement a program that encrypts messages using Caesar’s cipher.

def agn():
    print ('Please enter a valid key')

def cnt(x):
    o=(i+k-x)%26+x
    pt[n]=chr(o)

while True:
    key=input('Enter key: ')
    try:
        k=int(key)
        if k>0:
            plaintext=input('Enter plaintext: ')
            pt=[(z)for z in plaintext]
            for n,i in enumerate(pt):
                i=ord(i)
                if i in range (97,123):
                    cnt(97)
                if i in range (65,91):
                    cnt(65)
            print(*pt,sep='')
            break
        else:agn()
    except:agn()
