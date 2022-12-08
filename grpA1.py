A=[]    #students playing cricket
B=[]    #students playing badminton
C=[]    #students playing football
U=[]    #universal set
a=int(input("enter number of students playing cricket"))
for i in range (a):
    roll=input("enter roll no")
    A.append(roll)
print(A)
b=int(input("enter number of students playing badminton"))
for i in range(b):
    roll=input("enter roll no")
    B.append(roll)
print(B)
c=int(input("enter number of students playing football"))
for i in range(c):
    roll=input("enter roll no")
    C.append(roll)
print(C)
uni=int(input("enter total number of students in class"))
for i in range(uni):
    roll=input("enter roll no")
    U.append(roll)
print(U)
while True:
    print("1.students who play both cricket and badminton\n2.students who play either cricket or badminton but not both\n3.students who play neither cricket nor badminton\n4.students who play cricket and football but not badminton")
    ch=int(input("enter your choice"))
    if ch==1:
        #list of students who play both cricket and badminton
        CB=[]
        for i in A:
            for j in B:
                if i==j:
                    CB.append(j)
        print("list of students who play both cricket and badminton are",CB)
    if ch==2:
        #list of students who play either cricket or badminton but not both
        CBE=[]
        for i in A:
            if i not in B:
                CBE.append(i)
        for i in B:
            if i not in A:
                CBE.append(i)
        print("list of students who play either cricket or badminton but not both are",CBE)
    if ch==3:
        #list of students who play neither cricket nor badminton
        CBN=[]
        X=[] #students who play cricket or badminton
        X.extend(A)
        for i in B:
            if i not in A:
                X.append(i)
        #comparing with universal set
        for i in U:
            if i not in X:
                CBN.append(i)
        print("list of students who play neither cricket nor badminton",CBN)
    if ch==4:
        #list of students who play cricket and football but not badminton
        CFNB=[]
        CF=[] #students playing cricket and football
        CF.extend(A)
        for i in C:
            if i not in A:
                CF.append(i)
        for i in CF:
            if i not in B:
                CFNB.append(i)
        print("list of students who play cricket and football but not badminton",CFNB)
        break
