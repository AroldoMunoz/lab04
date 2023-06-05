from interpreter import draw
from chessPictures import *

imag = Picture(QUEEN)

image=imag.horizontalRepeat(3)
#image=imag.verticalRepeat(3)


draw(image)
