import os

f = open("example.txt","w+")
str = "field1,field2,field3,filed4,field5\r"
while os.stat("example.txt").st_size <= 1e+9:
    f.write(str)

f.close()
    