import os
print("Checking for requirements...!!!")

a = "dpkg -s figlet | grep Status >a.txt"
b = "dpkg -s lolcat | grep Status >b.txt"
os.system(a)
os.system(b)
af = open("a.txt","r")
bf = open("b.txt","r")
ra = af.readline()
rb = bf.readline()
print(ra)
print(rb)
if ra == "Status: install ok installed":
    print("figlet Installed ..!")
else:
    os.system("sudo apt-get install figlet")
if rb == "Status: install ok installed":
    print("lolcat installed")
else:
    os.system("sudo apt-get install lolcat")
try:
    module_req = input("Some modules need to download, do you want continue (Y/N): ")
    cap = module_req.upper()

    if cap == "YES":
        os.system("pip install requests")
        os.system("pip install termcolor")
    else:
        pass
except:
    pass
finally:
    print("Good job. Setup is Sucessfully Completed!!")
af.close()
bf.close()
