a=int(input('Dati dimensiunea matricii:'))
n=[]
if a>=2 and a<=10:
    for linie in range (0,n):
        linie=[]
        for element in range (0,n):
            element=int(input('dati numarul: '))
            linie.append([element]) 
        n.append([linie])
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
                mjd_secundara.append(n[i[j]])
print("Suma componentelor care se afla pe diagonala principala este",sum(d_principala))
print("Suma componentelor care se afla pe diagonala secundara este",sum(d_secundara))
print("Suma componentelor care se afla mai sus de diagonala princiapla este ",sum(msd_principala))
print("Suma componentelor care se afla mai jos de diagonala princiapla este",sum(mjd_principala))
print("Suma componentelor care se afla mai sus de diagonala principala este",sum(msd_secundara))
print("Suma componentelor care se afla mai jos de diagonala principala este",sum(mjd_secundara))