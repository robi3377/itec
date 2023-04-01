poem = 'Ana are mere și pere, Fructe de care se bucură mult. Are și alte fructe, dar merele sunt preferatele ei.'
poem = poem.split(' ')
lis = []
c = 0
for i in range(len(poem)):
    if poem[i] == poem[i].capitalize():
        nr = i+c
        lis.append(nr)
        c+=1
        # poem.insert(i-1, '\n')

for i in lis:
    poem.insert(i, '\n')

poem = ' '.join(poem)
print(poem)