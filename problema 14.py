n=int(input('Dati dimensiunea matricii:'))
a=[]
if n>=2 and n<=10:
    for i in range (0,n):
        v=[]
        for j in range (0,n):
            x=int(input('dati numarul: '))
            v.append([x]) 
        a.append([v])
    print(a)
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
                mjd_secundara.append(n[i[j]])
print("Suma componentelor care se afla pe diagonala principala este",sum(d_principala))
print("Suma componentelor care se afla pe diagonala secundara este",sum(d_secundara))
print("Suma componentelor care se afla mai sus de diagonala princiapla este ",sum(msd_principala))
print("Suma componentelor care se afla mai jos de diagonala princiapla este",sum(mjd_principala))
print("Suma componentelor care se afla mai sus de diagonala principala este",sum(msd_secundara))
print("Suma componentelor care se afla mai jos de diagonala principala este",sum(mjd_secundara))