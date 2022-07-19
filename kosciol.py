
from unicodedata import name


def start():

    from colorama import Fore, Back, Style 
    import os
    import time

    os.system('cls')
    
    print(Fore.GREEN + ("\nZa 2 sekundy zacznie się praca :)\n"))
    os.system("title [Randkowanie] kacperjakub to szef [jebac marlene]")
    Style.RESET_ALL

start()

def main():


    from pynput.keyboard import Key, Controller
    import time
    from colorama import Fore, Back, Style 
    import os
    import random

    keyboard1 = Controller()

    time.sleep(2)

    zart = random.choice(open('names.txt', 'r').readlines()).strip()

    work = zart
    for char in zart:
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.1)
    keyboard1.press(Key.enter)
    if keyboard1.pressed():
        print(Fore.GREEN + "[WYKONANO]", Style.RESET_ALL + work)



    from datetime import datetime, timedelta
    now = datetime.now()
    now_plus_10 = now + timedelta(minutes = 8)
    print(Fore.CYAN + "\nNastępne wykonanie żartu: ", now_plus_10)

    for char in "Za 8 minut kolejny żart! - BOT":
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.1)
    keyboard1.press(Key.enter)

    Style.RESET_ALL

    time.sleep(480)
    main()


main()

