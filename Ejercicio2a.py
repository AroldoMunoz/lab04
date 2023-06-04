from interpreter import draw
from chessPictures import *

imag=Picture(KNIGHT)
imag.join(KNIGHT)

imag.up(imag.img)
draw(imag)