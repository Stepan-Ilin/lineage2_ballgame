
import cv2 as cv
import numpy as np

import  pytesseract
import cv2


from ahk import AHK
from ahk.window import Window


import time
ahk = AHK()
#win = Window(ahk, ahk_id='0x50536')

win = ahk.win_get(title='Asterios')

win.activate()
#while True:
 #   if keyboard.read_key() == "p":
 #       print("You pressed p")
      #  break
#

    #time.sleep(2)

   # print("Конец цикла")
x=310
y=510
ahk.click(x+win.rect[0],y+win.rect[1])
#time.sleep(0.1)
ahk.click()
ahk.mouse_drag(0, 40, relative=True)
ahk.click(x+win.rect[0]-274,y+win.rect[1]+40+165)

print(ahk.mouse_position)
cv2.waitKey(0)

ahk.click(x+win.rect[0]-274+10,y+win.rect[1]+40+165-127)
cv2.waitKey(0)
ahk.click(x+win.rect[0]-274+10,y+win.rect[1]+40+165-127-137)
cv2.waitKey(0)
ahk.click(x+win.rect[0]-274+10,y+win.rect[1]+40+165-127-127)
cv2.waitKey(0)
ahk.click(x+win.rect[0]-274+10,y+win.rect[1]+40+165-127-127+34)
cv2.waitKey(0)
#text = pytesseract.image_to_string(img)
#img = cv.imread('C:\\py.projects\\objects_la2\\S.jpg',0)
#img2 = img.copy()
#if ahk.image_search('C:\\py.projects\\objects_la2\\S.jpg', upper_bound=(145, 462), lower_bound=(164, 485)):
   # print(1)
#else:print(0)
# lower-right corner of search area
#ahk.pixel_get_color(148, 466)  # Get color of pixel located at coords (100, 100)
#ahk.pixel_search('0x9d6346')  # Get coords of the first pixel with specified color

print(ahk.mouse_position)


