a=int(input('Dati dimensiunea matricii:'))
n=[]
if a>=2 and a<=10:
    for i in range(a):
        list = []
        for j in range(a):
            list.append(int(input(f'Dati element pe pozitia: ')))
        n.append(list)
    print(n)
    d_principala=[]
    d_secundara=[]
    msd_principala=[]
    mjd_principala=[]
    msd_secundara=[]
    mjd_secundara=[]
    for i in range (len(n)):
        for j in range(len(n[0])):
            if j==i:
                d_principala.append(n[i][j])
            if (i+j)==(len(n)-1):
                d_secundara.append(n[i][j])
            if i<j:
                msd_principala.append(n[i][j])
            if i>j:
                mjd_principala.append(n[i][j])
            if (i+j)<(len(n)-1):
                msd_secundara.append(n[i][j])
            if (i+j)>(len(n)-1):
                mjd_secundara.append(n[i][j])
print("Suma componentelor care se afla pe diagonala principala este",sum(d_principala))
print("Suma componentelor care se afla pe diagonal")
if a>=2 and a<=10:
    for i in range(a):
        list = []
        for j in range(a):
            list.append(int(input(f'Dati element pe pozitia: ')))
        n.append(list)
    print(n)
