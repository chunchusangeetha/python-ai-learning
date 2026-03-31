import os
f = open("demofile.txt")
print(f.read())
f.close()
os.remove("demofile.txt")
