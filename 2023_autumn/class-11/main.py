def openFile():
    f = open("pythontextfile.txt", "r")
    print(f.read())
    f.close()

# openFile()

def openLines():
    f = open("pythontextfile.txt", "r", encoding='utf-8')
    # line = f.readline()  # csak 1 sor
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()


# openLines()


def findText():
    with open("pythontextfile.txt") as f:
        if("furcsa" in f.read()):
            print("Van furcsa a fajlban")
        else:
            print("Nincs furcsa a fajlban")


#findText()


def createFile(fileName):
    f = open("myfile1.txt", "w")
    f.close()
    
    f = open("myfile2.txt", "w").close()
    
    with open("myfile3.txt", "w") as f:
        print("3. fajl irva")
        

#createFile("myFile")


def writeFile():
    with open("myText.txt", "w+") as f:
        f.write("Hello World!\n")
        f.seek(0)
        print(f.read())


#writeFile()


def oneToTen():
    with open("newFile.txt", "w+") as f:
        for i in range(1, 11):
            f.write(f'{i} ')
        f.seek(0)
        print(f.read())


#oneToTen()


def noSpaces():
    text = ""
    with open("pythontextfile.txt", "r") as origin:
        text = origin.read().replace(" ", "")

    with open("noSpaces.txt", "w+") as newfile:
        newfile.write(text)
        newfile.seek(0)
        print(newfile.read())


#noSpaces()


from datetime import datetime

def appendFile():
    with open("appendedFile.txt", "a+") as f:
        f.write(f"This is a new line written at: {datetime.now()}\n")
        f.seek(0)
        print(f.read())


appendFile()
