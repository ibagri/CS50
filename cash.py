lst=[25,10,5,1]
coins=0
while True:
    try:
        inp=input('Change owed: ')
        inp=float(inp)
        inp=round(inp*100)
        if inp<=0:
            print('Plese input only numbers')
        for i in lst:
            while inp>=i:
                coins+=int(inp/i)
                inp%=i
        print(coins)
        break
    except:
        print('Plese input only numbers')
