from PIL import Image
import pyautogui
import time
import webbrowser
import pytesseract
import subprocess
import numpy as np


def Reaction():
	delay = 0
	lvls = 5
	(width, height) = pyautogui.size()
	print (width, height)
	width = int(width / 2)
	height = int(height / 4)
	pyautogui.moveTo(width, height)
	color = pyautogui.pixel(width, height)
	hexColor = '%02x%02x%02x' % color
	if hexColor == '2b87d1':
		pyautogui.click()
		for x in range(lvls):
			while hexColor != '4bdb6a':
				color = pyautogui.pixel(width, height)
				hexColor = '%02x%02x%02x' % color
			time.sleep(delay)
			pyautogui.click()
			if x != 4:
				pyautogui.click()
			hexColor = ''
	else:
		Reaction()

def verbalMemory():
	pytesseract.pytesseract.tesseract_cmd = \
		r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
	allWords = []
	xStart = 673
	yStart = 563
	xSeen = 600
	ySeen = 487
	xNew = 740
	yNew = 485
	delay = .35
	lvls = 300
	pyautogui.click(xStart, yStart)
	time.sleep(.5)
	color = pyautogui.pixel(xStart, yStart)
	hexColor = '%02x%02x%02x' % color
	if hexColor == '2b87d1':
		for num in range(lvls):
			im1 = pyautogui.screenshot(region=(xSeen - 280, ySeen - 154, 690, 75))
			word = pytesseract.image_to_string(im1)
			if word not in allWords:
				allWords.append(word)
				pyautogui.click(xNew, yNew)
			else:
				pyautogui.click(xSeen, ySeen)
			time.sleep(delay)
	else:
		verbalMemory()

def Typing():
	pyautogui.moveTo(5, 5)
	pyautogui.screenshot('text.png', region=(200, 380, 970, 150))  # screenshot text area to text.png
	subprocess.run(['C:/Program Files (x86)/Tesseract-OCR/tesseract', 'text.png', 'text-result', '--dpi', '70'])
	with open('text-result.txt', 'r', encoding='utf-8') as file:
		data = file.read().replace('\n', ' ')
		if (data[0] == '|' or data[0] == '['):
			data = data[1:]
		if(data[0] == '!'):
			data = data[1:]
		data = data.replace('|', 'I')
		data = data.lstrip()
		data = data.rstrip()
		print("TEXT:")
		print(data)
		pyautogui.moveTo(500, 450)
		pyautogui.click()
		pyautogui.write(data)
	pyautogui.moveTo(100, 100)


def OpenReaction():
	webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
	time.sleep(3)
	Reaction()

def OpenVerbalmemory():
	webbrowser.open('https://www.humanbenchmark.com/tests/verbal-memory', new=2)
	time.sleep(3)
	verbalMemory()

def OpenTyping():
	webbrowser.open('https://humanbenchmark.com/tests/typing', new=2)
	time.sleep(3)
	Typing()


def Main():
	choose = int(input("What test? \n1. Reaction Time\n2. Verbal Memory\n3. Typing\n"))
	if choose == 1:
		OpenReaction()
	if choose == 2:
		OpenVerbalmemory()
	if choose == 3:
		OpenTyping()


Main()