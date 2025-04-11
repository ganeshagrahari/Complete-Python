# in r+ mode the file is opened for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it creates a new file for reading and writing.
f = open(r"C:\Users\ganes\OneDrive\Desktop\python course by  Ganesh\Python_Files_IO\demo.txt","r+")
f.write("Gandu")
print(f.read())
f.close()

