'''write a python program to store roll nos of students in array who attended training program in 
random order. write function for searching whether particular student attended training program or not,
using linear search and sentinel search.'''

arr=[]
n=int(input("enter how many students attended the program"))
for i in range(n):
    a=int(input("enter roll nos of students present"))
    arr.append(a)
print(arr)

print("1. Linear search\n2. Sentinel search")
ch=int(input("enter your choice"))

if (ch==1):
    #linear search

    def linear(arr):
        roll=int(input("enter the roll no that you want to search"))
        for i in range(len(arr)):
            if(arr[i]==roll):
                print("roll no ",arr[i],"is present at index no ",i)
    linear(arr)

elif(ch==2):
    #sentinel search

    def sentinel(arr):
        n=len(arr)
        roll=int(input("enter the rollno that you want to search"))
        last=arr[n-1]
        arr[n-1]=roll
        i=0
        while(arr[i]!=roll):
            i+=1
        arr[n-1]=last
        if(i<(n-1)or(arr[i]==roll)):
            print("roll no ",arr[i], "is present at index no ",i)
        else:
            print("roll no not found")
    sentinel(arr)



