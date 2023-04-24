import Funcs
import image
##################
import time
import keyboard
import multiprocessing
import colorama
##################

space = 34
colorama.init(autoreset=True)

#############################

def BackGroundThread(pipei1):
    i1 = 0
    while 1:
        key = keyboard.read_key()
        time.sleep(0.2)
        if key == "1":
            i2 = i1
            if i2 == 1:
                keyboard.press('esc')
                keyboard.press('enter')
                keyboard.press('enter')
            elif i2 == 2:
                keyboard.press('esc')
                keyboard.press('enter')
            elif i2 == 4:
                keyboard.press('esc')
                keyboard.press('enter')
            i1 = 1
            pipei1.send(i1)

        if key == "2":
            i2 = i1
            if i2 == 1:
                keyboard.press('esc')
                keyboard.press('enter')
                keyboard.press('enter')
            elif i2 == 2:
                keyboard.press('esc')
                keyboard.press('enter')
            elif i2 == 4:
                keyboard.press('esc')
                keyboard.press('enter')
            i1 = 2
            pipei1.send(i1)

        if key == "3":
            i2 = i1
            if i2 == 1:
                keyboard.press('esc')
                keyboard.press('enter')
                keyboard.press('enter')
            elif i2 == 2:
                keyboard.press('esc')
                keyboard.press('enter')
            elif i2 == 4:
                keyboard.press('esc')
                keyboard.press('enter')
            i1 = 3
            pipei1.send(i1)

        if key == "4":
            i2 = i1
            if i2 == 4:
                keyboard.press('esc')
                keyboard.press('enter')
            if i2 == 3 or i2 == 4:
                i1 = 4
                pipei1.send(i1)

        if key == "tab":
            keyboard.press('esc')
            keyboard.press('enter')
            keyboard.press('enter')
            i1 = 5
            pipei1.send(i1)


def SoruEkrani():
    Funcs.clearscreen()
    keyboard.press('esc')
    Funcs.GetWords()
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(2 * """
        """)
    Funcs.Printimage(image.KelimeyiBil)
    print(38 * """
        """)
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(colorama.Fore.LIGHTCYAN_EX+
        "Cikmak Için : Tab" + space * " " + "Kelime Girmek Için: 1" + space * " " + "Kelime Sordurtmak Için: 2" + space * " " + "Kelimeleri Listelemek Için: 3")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;80H" + "English")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;120H" + "Turkish")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;100H" + image.Esittir)
    Funcs.AskMe()


def SayMerhaba():
    Funcs.Printimage(image.Merhaba)
    time.sleep(4)
    Funcs.clearscreen()


def FirstScreen():
    print("""
    """)
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(10 * """
    """)
    Funcs.Printimage(image.KelimeGir)
    Funcs.Printimage(image.KelimeSor)
    Funcs.Printimage(image.KelimeListele)
    print(10 * """
    """)
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")


def KelimeGirEkrani():
    Funcs.clearscreen()
    keyboard.press('esc')
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(2 * """
        """)
    Funcs.Printimage(image.KelimeSor2)
    print(38 * """
        """)
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(colorama.Fore.LIGHTCYAN_EX+
        "Cikmak Için : Tab" + space * " " + "Kelime Girmek Için: 1" + space * " " + "Kelime Sordurtmak Için: 2" + space * " " + "Kelimeleri Listelemek Için: 3")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;80H" + "English")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;120H" + "Turkish")
    print(colorama.Fore.LIGHTCYAN_EX+"\033[17;100H" + image.Esittir)
    Funcs.AddWord()


def KelimeListelemeEkrani():
    Funcs.clearscreen()
    keyboard.press('esc')
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(1 * """
            """)
    Funcs.Printimage(image.ListeBasligi)
    print("\033[17;0H")
    print(colorama.Fore.LIGHTCYAN_EX+41 * "  " + "English" + (space - 7) * " " + "Turkish")
    print("""
    """)
    for i in Funcs.mainWordslist:
        print(colorama.Fore.LIGHTYELLOW_EX+41 * "  " + i + (space - len(i)) * " " + Funcs.mainWordslist[i])
    print((29 - len(Funcs.mainWordslist.keys())) * """
                """)
    print()
    print(colorama.Fore.LIGHTCYAN_EX+210 * "-")
    print(colorama.Fore.LIGHTCYAN_EX+
        "Cikmak Için : Tab" + (space - 15) * " " + "Kelime Girmek Için: 1" + (
                space - 15) * " " + "Kelime Sordurtmak Için: 2" + (
                space - 15) * " " + "Kelimeleri Listelemek Için: 3" + (space - 15) * " " + "Kelime Silmek Için: 4")


def KelimeSil():
    keyboard.press('esc')
    KelimeListelemeEkrani()
    print()
    print(colorama.Fore.YELLOW+"Lutfen Silmek Istediginiz Kelimenin Ingilizcesini Yazın")
    w = input()
    if w == "":
        return
    elif Funcs.SearchWord(w):
        Funcs.DeleteWord(w)
        print(colorama.Fore.LIGHTGREEN_EX+"Kelime Silindi")
        time.sleep(1)
    else:
        print(colorama.Fore.LIGHTRED_EX+"Oyle Bir Kelime Yok")
        time.sleep(1)


if __name__ == '__main__':

    multiprocessing.freeze_support()
    keyboard.press('f11')

    Funcs.clearscreen()

    TitleStr = "Gkay'in Muhtesem Programi"
    print(f'\33]0;{TitleStr}\a', end='', flush=True)
    Funcs.GetWords()
    SayMerhaba()
    FirstScreen()
    pipei1, pipei1Finish = multiprocessing.Pipe()

    ThBack = multiprocessing.Process(target=BackGroundThread, args=(pipei1,))

    ThBack.start()
    i1 = pipei1Finish.recv()
    while 1:
        time.sleep(0.2)
        if i1 == 1:
            while i1 == 1:
                KelimeGirEkrani()
                if pipei1Finish.poll():
                    i1 = pipei1Finish.recv()
        if i1 == 2:
            while i1 == 2:
                SoruEkrani()
                if pipei1Finish.poll():
                    i1 = pipei1Finish.recv()

        if i1 == 3:
            KelimeListelemeEkrani()
            i1 = pipei1Finish.recv()

        if i1 == 4:
            while i1 == 4:
                KelimeSil()
                if pipei1Finish.poll():
                    i1 = pipei1Finish.recv()

        if i1 == 5:
            ThBack.terminate()
            break
