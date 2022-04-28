import pyautogui
import time
import pyperclip

import json

f = open("../data/tokens.json")
tokens = json.load(f)

f2 = open("../data/config.json")
config = json.load(f2)

import keyboard

sell = False
buy = False
run = True

while run:
    if keyboard.is_pressed(config["buy"]):
        buy = True
        while buy:
            for token in tokens:
                token_list = token.split("#")
                pyperclip.copy(f"!buy {token_list[0]}\u0023{token_list[1]}")
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")
                time.sleep(3.5)
            pyperclip.copy("Done buying")
            pyautogui.hotkey("ctrl", "v")
            buy = False
    elif keyboard.is_pressed(config["sell"]):
        sell = True
        while sell:
            for token in tokens:
                token_list = token.split("#")
                pyperclip.copy(f"!sell {token_list[0]}\u0023{token_list[1]} {config['sell_price']}")
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")
                time.sleep(3.5)
            pyperclip.copy("Done selling")
            pyautogui.hotkey("ctrl", "v")
            sell = False
    elif keyboard.is_pressed(config["run_key"]):
        run = False
