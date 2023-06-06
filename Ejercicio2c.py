from interpreter import draw
from chessPictures import *

imag = Picture(QUEEN)

image=imag.horizontalRepeat(2)
#image=imag.verticalRepeat(3)


draw(image)
