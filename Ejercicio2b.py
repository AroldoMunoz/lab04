from interpreter import draw
from chessPictures import *


imag = Picture(KNIGHT)
imagv = imag.join(imag.img)

imagvv=imag.horizontalMirror()


final=imag.up(imagvv)
draw(final)
