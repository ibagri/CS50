import string
azl=string.ascii_lowercase
azl=[(a)for a in azl]
azu=string.ascii_uppercase
azu=[(a)for a in azu]

ct=list()

def agn():
    print ('Key must contain 26 characters')


while True:
    naz=input('Key: ')
    nazl=[z.lower() for z in naz]
    dlow=dict(zip(azl,nazl))
    dup=dict(zip(azu,naz))
    d={**dup, **dlow}
    try:
        naz=str(naz)
        if len(naz)==26:
            naz=[(z)for z in naz]
            plaintext=input('Enter plaintext: ')
            pt=[(z)for z in plaintext]
            for n in pt:
                for key, value in d.items():
                    if key==n:
                        ct.append(value)
                if n.isalpha()==False: ct.append(n)
            print(*ct,sep='')
            break
        else:agn()
    except:agn()
