from pynput.keyboard import Key, Controller
from selenium import webdriver
from colorama import Fore, Style
import time
import conf

print(f'{Fore.YELLOW}Welcome to type2fast\nRead README for instructions.\n')

DELAY_PER_WORD = float(input(f'{Fore.GREEN}[1] Delay per word: '))


browser = webdriver.Chrome(executable_path=conf.WEBDRIVER_PATH)

words = []


def enter_words(delay):
    words = get_words()

    input(f'\n{Fore.BLUE}[3] Press enter to start...')

    input_text = browser.find_element_by_class_name('txtInput')

    for word in words:
        for i in range(len(word)):
            input_text.send_keys(word[i])
        
        time.sleep(delay)
        
        input_text.send_keys(' ')


def goto_race():
    keyboard = Controller()

    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('i')

    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release('i')


def get_words():
    browser.get('https://play.typeracer.com/')
    
    print('\nWaiting for you to agree terms in the next 5 seconds...\n')
    time.sleep(5)

    goto_race()

    WHOLE_TEXT = input(f'\n{Fore.YELLOW}[2] Whole text:\n')
    
    words = WHOLE_TEXT.split()

    return words


enter_words(DELAY_PER_WORD)
