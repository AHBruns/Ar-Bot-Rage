import time
import HandOfGod.spectacles as eyes
import pyautogui as GUI

positions = eyes.read()
move_dur_default = .25


def setup_scene_1():
    time.sleep(5)
    hard_open_chrome()
    default_urls()
    return 0


def default_urls():
    url = "https://www.coinexchange.io/market/ETH/BTC"
    url_1_input(url)
    url_2_input(url)
    url_3_input(url)
    return 0


def url_1_input(string):
    GUI.moveTo(positions["chrome-window-1-url-bar"][0],positions["chrome-window-1-url-bar"][1],move_dur_default)
    GUI.click()
    GUI.typewrite(string)
    GUI.press('enter')
    return 0


def url_2_input(string):
    GUI.moveTo(positions["chrome-window-2-url-bar"][0],positions["chrome-window-2-url-bar"][1],move_dur_default)
    GUI.click()
    GUI.typewrite(string)
    GUI.press('enter')
    return 0


def url_3_input(string):
    GUI.moveTo(positions["chrome-window-3-url-bar"][0],positions["chrome-window-3-url-bar"][1],move_dur_default)
    GUI.click()
    GUI.typewrite(string)
    GUI.press('enter')
    return 0


def hard_open_chrome():
    GUI.moveTo(positions["toolbar-open-pos"][0],positions["toolbar-open-pos"][1],move_dur_default)
    time.sleep(2)
    GUI.moveTo(positions["chrome-icon-pos"][0],positions["chrome-icon-pos"][1],move_dur_default)
    GUI.click()
    time.sleep(2)
    two_finger_tap()
    GUI.moveTo(positions["chrome-icon-new-window-option-pos"][0],positions["chrome-icon-new-window-option-pos"][1],move_dur_default)
    GUI.click()
    time.sleep(2)
    GUI.moveTo(positions["chrome-left-new-window-grab-pos"][0],positions["chrome-left-new-window-grab-pos"][1],move_dur_default)
    GUI.dragRel(619,-40,5)
    GUI.moveTo(positions["toolbar-open-pos"][0],positions["toolbar-open-pos"][1],move_dur_default)
    time.sleep(2)
    GUI.moveTo(positions["chrome-icon-pos"][0],positions["chrome-icon-pos"][1],move_dur_default)
    two_finger_tap()
    GUI.moveTo(positions["chrome-icon-new-window-option-pos"][0],positions["chrome-icon-new-window-option-pos"][1],move_dur_default)
    GUI.click()
    time.sleep(2)
    GUI.moveTo(positions["chrome-middle-new-window-grab-pos"][0],positions["chrome-middle-new-window-grab-pos"][1],move_dur_default)
    GUI.dragRel(620,-40,5)
    return 0


def two_finger_tap():
    GUI.mouseDown(button='left')
    GUI.mouseDown(button='right')
    time.sleep(.5)
    GUI.mouseUp(button='left')
    GUI.mouseUp(button='right')
    return 0





