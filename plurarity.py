result=list()
vote=dict()

while True:
    c=input('Candidates: ').split(' ')
    if len(c)<=9:break
    else:print('Maximum of 9 candidates')

while True:
    nv=input('Number of voters: ')
    try:
        nv=int(nv)
        for i in range(nv):
            v=input('Vote: ')
            if v in c:
                vote[v]=vote.get(v,0)+1
            else:
                print ('Invalid vote.')

        for key,val in vote.items():
            if val==max(vote.values()):
                result.append(key)

        print(*result,sep=' ')#get key with max value
        break
    except:
        print('Please enter a number of voters with numbers only.')
        continue
