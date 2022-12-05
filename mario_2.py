def agn():
    print ('Please enter a number between 1 and 8')

while True:
    height=input('Height: ')
    try:
        height=int(height)
        if height>=1 and height<=8:
            height=int(height)+1
            for i in range(1,height,1):
                z=height-1-i
                print(z*' ',i*'#','  ',i*'#',sep='')
            break
        else:agn()
    except:agn()
