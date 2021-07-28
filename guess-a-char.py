import  worseng

import  random

select_word= random.choice(worseng.word_list)

# print(select_word)
blank=[]
for i in range(len(select_word)):
    blank+="_"
# print(blank)
print((''.join(str(l) for l in blank)))
loop = 1
while loop<=len(select_word):
    if '_' in blank:
        guess = input("guess the correct letter to fill the blanks\n").lower()
        if guess in select_word:
            for j in range(0, len(select_word)):
                if select_word[j]==guess:
                    blank[j]=guess




        print((''.join(str(e) for e in blank)))





    loop+=1

if not '_' in blank:
    print('you won')
else:
    print('you lost')
