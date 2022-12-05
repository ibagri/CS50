#Here, L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

import re
text=input("Enter text: ")
words=0
letters=list()

for i in text:
    for j in i:
        if j.isalpha():
            j=j.lower()
            letters.append(j)

for i in text.split():words+=1

sentences=re.split('[.!?]\s*',text)

L=round((float(len(letters))/words)*100,2)
S=round((float(len(sentences)-1)/words)*100,2)

index=round(0.0588*L-0.296*S-15.8)

if index<1:print('Before Grande 1')
elif index>16:print('Grade 16+')
else:print('Grade',index)
