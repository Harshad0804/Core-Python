d={1:"Ajay",2:"Vijay",3:"Sanjay",4:"Jay",5:"Bijoy",6:"Sujoy"}

sname=input("Enter a Student name to search in Dictionary : ")
flag=False

for i in d:
    if sname==d[i]:
        flag=True
        break

if flag==True:
    print("This name is Present in Dictionary")
else:
    print("This name is not Present (Absent) in Dictionary")
