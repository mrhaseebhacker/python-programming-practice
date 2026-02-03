f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

f = open("new.txt", "w")
f.write("I want to learn python")
f.close()

f = open("new.txt", "a")
f.write(" I want to learn javascript")
f.close()

with open("new.txt", "r") as f:
    data = f.read()
    print(data) #we don't need to close the file

with open("new.txt", "w") as f:
    f.write("I am a programmer")    
