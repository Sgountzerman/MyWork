from random import randrange

Tuxaioi=[]
for i in range(30):
    Tuxaioi.append(randrange(-30,30))
    
c=0
for i in range(28):
    for y in range(i,29):
        for z in range(y,30):
                if (Tuxaioi[i] + Tuxaioi[y] + Tuxaioi[z])==0:
                    c=1
                    print(Tuxaioi[i] , Tuxaioi[y] , Tuxaioi[z])

if c==0:
    print('Δεν υπάρχει συνδυασμός τριών αριθμών της λίστας που να δίνει άθροισμα 0')
