r1=dict()
r2=dict()
r3=dict()
tie=list()
fin=dict()
from collections import Counter

def t(x):
    for k,v in x:
        if k in tie.keys():
            tie[k]=tie.get(v,v)


while True:
    c=input('Candidates: ').split(' ')
    if len(c)<=9:break
    else:print('Maximum of 9 candidates')

while True:
    nv=input('Number of voters: ')
    try:
        nv=int(nv)
        for i in range(nv):
            for z in range(3):
                rank1=input('Rank 1: ')
                if rank1 in c:
                    r1[rank1]=r1.get(rank1,0)+3
                else:
                    print ('Invalid vote.')
                rank2=input('Rank 2: ')
                if rank2 in c:
                    r2[rank2]=r2.get(rank2,0)+2
                else:
                    print ('Invalid vote.')
                rank3=input('Rank 3: ')
                if rank3 in c:
                    r3[rank3]=r3.get(rank3,0)+1
                else:
                    print ('Invalid vote.')
                print('')
                break
        #find the tie candidates
        for k,v in r1.items():
            if v==max(r1.values()):
                tie.append(k)
        print(tie)
        #if tie or not 50%+
        if len(tie)>1 or max(tie)<nv/2:
            print(r1,r2,r3)
            z=dict(Counter(r1)+Counter(r2)+Counter(r3))
            print(z)
            for k,v in z.items():
                if k==tie.items():
                    fin[k]=fin.get(v,v)
            print(fin)
            #tie a2 b2


#totals = {}
#for key, value in ds:
#    totals[key] = totals.get(key, 0) + value

        #if not +50%:d # if max(r1.values())>nv/2:

        else:print('The winner is',max(r1))
        break
    except:
        print('Please enter a number of voters with numbers only.')
        continue
