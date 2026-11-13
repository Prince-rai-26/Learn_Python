# File i/o in python 

# python can be used operation on a file (read and write data)

# TYPES of files (both are still stored in 0 and 1 binary )
# 1. Text files : e.g. .txt, .docs, .log, etc
# 2. Binary files : e.g. .mp4, .jpg, .png, .jpeg, etc

# character                             meaning 

#    r           -> open or reading(default)
#    w           -> open for writing , pehle ye file mein likha hua chij ko delete krta h fir likhtha h 
#    x           -> create a new file and open it for writing 
#    a           -> open for writing , ye file mein likha hua chij , ke baad likhtha h bina pehle wale chij ko delete kiye 
#    b           -> binary mode 
#    t           -> text mode (default)
#    +           -> open a disk file for updating (reading and writing)

#    r+          -> read  +  overwrite  (pointer at starting)   no truncate 
#    w+          -> read  +  overwrite                          truncate 
#    a+          -> read  +  append     (pointer at end)        no truncate 

#   Open, read & close File
#   We have to open a file before reading or writing.

#   f = open( “file_name”, “mode”)
#   sample.txt       <-|      |->                r : read mode
#   demo.docx        <-|      |->                w : write mode
#   
#   data = f.read( )
#   f.close()

#  f = open("demo.txt", "r")
#  
#  data = f.read()                #  (sharadha mam ne yahi code likhi thi , but vs code demo.txt ko file nhi dhund pa raha h )
#  print(data) 
#                but agar terminal mein cd fir cd file_input_output fir python file.py toh ye v run kr jayega , but directly nhi 

#  f.close()
                          
                                    ##   (isliye chat gpt ka code likhe h taki run kr jaye )
import os

file_path = os.path.join(os.path.dirname(__file__), "demo.txt")

f = open(file_path, "r")                                   
data = f.read()                #agar data read kr jayega toh readline execute nhi hoga kyunki cursor end pe chala jata h 
print(data)
# 
# line1 = f.readline()              # isme ek next line ka space aa jayega 
# print(line1)
# 
# line2 = f.readline()              # isme v ek next line ka space aa jayega 
# print(line2)
# 
# line3 = f.readline()              # isme v ek next line ka space aa jayega 
# print(line3)
# 
# f.close()

# f = open(file_path, "w")
# 
# f.write("you are my love okk 264")
# f.write("\nafter i hae loved my princess that live in dwarka 03")
# f.close()

# f = open(file_path, "a")
# 
# f.write("\ni have made many mistakes during our relationship")
# f.close()

# f = open("sample.txt","w")          when a new file is there ,, it automatically makes a folder 
# f.close

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
# 
# with open("demo.txt","w") as f:
#     f.write("new data")

# Deleting a file
# using the os module 
# Module (like a code library) is a file written by another programmer that generally has a functions we can use

import os 
os.remove("sample.txt")
