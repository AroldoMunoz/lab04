from interpreter import draw
from chessPictures import *

imag=Picture(KNIGHT)

imag1=imag.join(KNIGHT)

imag2=imag.horizontalMirror(imag1)
draw(imag2)
imag3=imag1
imag3.up(imag2.img)

draw(imag)