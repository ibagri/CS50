while True:
    inp=input("Card number: ")
    try:
        num=[str(i)for i in inp]
        num=[int(j)for i in inp for j in i][::-1]
        l=num[::2]
        lx=num[1::2]
        lx2=list()
        for i in lx:
            i*=2
            lx2.append(i)
        lx2=[str(i)for i in lx2]
        lx2=[int(j)for i in lx2 for j in i]
        if (sum(lx2)+sum(l))%10==0: #reminder of 10 is always the last digit
            print('VALID')
        else:print('INVALID')
        break
    except:print('Enter numbers only')
