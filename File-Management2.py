import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()
