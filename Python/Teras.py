import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#custom_config = r'--oem 3 --psm 13'
import cv2
import pyscreenshot as ps
import numpy
from mss import mss
from PIL import Image
from ahk import AHK
ahk = AHK()

win = ahk.win_get(title='Asterios')
win.activate()
#img = Image.open("C:\py.projects\objects_la2\ext.png")
from pyscreenshot.plugins.msswrap import sct


#img = cv2.imread("C:\py.projects\objects_la2\\ty777777.png",cv2.IMREAD_GRAYSCALE)
#cv2.imwrite("C:\py.projects\objects_la2\\ry6666666.png", ps.grab())

    # Part of the screen to capture
box_sorry = {"left": win.rect[0]+22, "width":26, "top": win.rect[1]+390, "height": 12}
img_sorry_color = numpy.array(mss().grab(box_sorry))
img_sorry_gray = cv2.cvtColor(img_sorry_color,cv2.COLOR_BGR2GRAY)
cv2.imshow("OpenCV/Numpy normal", img_sorry_gray)
text_sorry = pytesseract.image_to_string(img_sorry_gray) #, config=custom_config)
print(text_sorry)

cv2.waitKey(0)

x=310
y=510

if text_sorry=='Sorry\n':
    ahk.click(x + win.rect[0] - 274 + 10, y + win.rect[1] + 40 + 165 - 127 - 127 + 34)
    print(ahk.mouse_position)
cv2.waitKey(0)