x=[]
n=int(input('introdu numarul de linii'))
if ((n>=2)and(n<=10)):
    print("introdu elementele matricei:")
    for k in range(0,n):
        k=[]
        for l in range(0,n):
            l=int(input())
            k.append(l)
        x.append(k)
    print(x)
    diagonala_principala=[]
    diagonala_secundara=[]
    sus_principala=[]
    jos_principala=[]
    sus_secundara=[]
    jos_secundara=[]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if i==j:
                diagonala_principala.append(x[i][j])
            if(i+j)==(len(x)-1):
                diagonala_secundara.append(x[i][j])
            if i<j:
                sus_principala.append(x[i][j])
            if i>j:
                jos_principala.append(x[i][j])
            if (i+j)<(len(x)-1):
                sus_secundara.append(x[i][j])
            if (i+j)>(len(x)-1):
                jos_secundara.append(x[i][j])       
    print('suma elementelor diagonale principale=',sum(diagonala_principala))
    print('suma elementelor diagonale secundare=',sum(diagonala_secundara))
    print('suma elementelor mai sus de diagonala principala=',sum(sus_principala))
    print('suma elementelor mai jos de diagonala principala=',sum(jos_principala))
    print('suma elementelor mai sus de diagonala secundara=',sum(sus_secundara))
    print('suma elementelor mai jos de diagonala secundara=',sum(jos_secundara))
