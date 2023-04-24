#############################
import random
import os
import time
import getpass
import pyfiglet
import json
import image
import colorama
############################
colorama.init(autoreset=True)


mainWordslist = {}
WordsEng = []
WordsTr = []
Streak=0
font = 'big'

def SearchWord(word):
    for i in mainWordslist.keys():
        if i == word:
            return True
    return False


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def GetWords():
    global mainWordslist
    mainWordslist = GetJson()
    for i in mainWordslist.keys():
        WordsEng.append(i)
    for i in mainWordslist.values():
        WordsTr.append(i)


def AddWord():
    word = input("\033[20;80H")
    wordTr = input("\033[20;120H")
    if len(word) <= 1 or len(wordTr) <= 1:
        return
    for i in word:
        if i.isdigit():
            return
    mainWordslist[word] = wordTr
    Post()


def Post():
    with open("Keys.json", "w") as file:
        json.dump(mainWordslist, file)


def DeleteWord(word):
    del mainWordslist[word]
    Post()
    WordsTr.clear()
    WordsEng.clear()
    for i in mainWordslist.keys():
        WordsEng.append(i)
    for i in mainWordslist.values():
        WordsTr.append(i)



def DeleteAll():
    mainWordslist.clear()
    Post()


def RandomNumber():
    if len(mainWordslist)-1==-1:
        x=-1
        return x
    else:
        x = random.randint(0, len(mainWordslist) - 1)
        return x


def AskMe():
    global Streak
    indexNumber = RandomNumber()
    if indexNumber==-1:
        print(colorama.Fore.LIGHTRED_EX+"\033[30;0H"+image.ListeBos)
        getpass.getpass("")
        return
    wordEn = WordsEng[indexNumber]
    wordTr = WordsTr[indexNumber]

    if Streak>1:
        print("\033[15;0H")
        PrintTxtLine("x"+str(Streak))

    print(colorama.Fore.LIGHTYELLOW_EX+"\033[20;80H" + wordEn)
    answer = input("\033[20;120H")


    if answer == wordTr:
        print(colorama.Fore.LIGHTGREEN_EX+"\033[25;0H" +image.TrueImg)
        Streak+=1
        time.sleep(1.5)
    else:
        print(colorama.Fore.LIGHTRED_EX+"\033[25;0H" +image.FalseImg)
        print(colorama.Fore.LIGHTYELLOW_EX+"\033[35;93H" +"DOGRU CEVAP:  "+ wordTr)
        Streak=0
        time.sleep(1.5)


def Printimage(img):
    for i in img:
        print(colorama.Fore.LIGHTCYAN_EX+5 * "" + i, end='')


def clearscreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def GetJson():
    if None != find("Keys.json", "./"):
        with open("Keys.json") as file:
            data = json.load(file)
    else:
        Post()
        with open("Keys.json") as file:
            data = json.load(file)
    return data

def PrintTxtLine(txt):
    f = pyfiglet.Figlet(font=font)
    print(colorama.Fore.CYAN+f.renderText(txt), end="")


def PrintTxt(txt):
    f = pyfiglet.Figlet(font=font)
    print(colorama.Fore.CYAN+f.renderText(txt))