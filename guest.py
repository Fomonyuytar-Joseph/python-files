filename="guest.txt"
while True:
 name=input(" what is your name:\n")

 with open(filename,'w') as file_object:
     file_object.write(name)

print("your name has been written to he file")