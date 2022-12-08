#the average score of the class
def average(marklist):
    sum=0
    c=0
    for i in range(len(marklist)):
        sum+=marklist[i]
        c+=1
    avg=sum/c
    print("sum=",sum)
    print("average=",avg)

#highest score
def highest(marklist):
    for i in range(len(marklist)):
        max=marklist[0]
        break
    for i in range(len(marklist)):
        if marklist[i]>max:
            max=marklist[i]
    return(max)

#lowest score
def lowest(marklist):
    for i in range(len(marklist)):
        min=marklist[0]
        break
    for i in range(len(marklist)):
        if marklist[i]<min:
            min=marklist[i]
    return(min)

#counting absent no. of students

#displaying marks with highest frequency
def frequency(marklist):
    i=0
    max=0
    print("marks  |   frequency")
    for j in marklist:
        if(marklist.index(j)==i):
            print(j,"  |  ",marklist.count(j))
            if marklist.count(j)>max:
                max=marklist.count(j)
                mark=j
        i+=1
    return(mark,max)

#main function
FDSmarks=[]
n=int(input("enter total number of students"))
for i in range(n):
    marks=int(input("enter marks of student"+str(i+1)+":"))
    FDSmarks.append(marks)
    
while True:
    print("1.total and avg marks\n2.max marks andnmin marks\n4.marks with highest frequency")
    ch=int(input("enter your choice"))
    if ch==1:
        average(FDSmarks)
    if ch==2:
        print("highest score in class:",highest(FDSmarks))
        print("lowest score",lowest(FDSmarks))
    if ch==4:
        mark,fr=frequency(FDSmarks)
        print("highest frequency is of marks {0} which is {1}".format(mark,fr))
    


