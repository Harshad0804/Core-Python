rno=int(input("Enter Roll No : "))
sname=input("Enter Your Name : ")
s1=int(input("Enter Subject 1 Marks : "))
s2=int(input("Enter Subject 2 MArks : "))
s3=int(input("Enter Subject 3 Marks : "))

total=s1+s2+s3
per=total/3

print("Roll No : ",rno)
print("Student Name : ",sname)
print("Total : ",total)
print("Percentage : ",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
