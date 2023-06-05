
from interpreter import draw
from chessPictures import *
from picture import *
from pieces import *

imag=Picture(KNIGHT)
imag2=Picture(SQUARE)


"""
imag.horizontalRepeat(3)
print(len(KING[0]))
print(len(KING))
#imag.join(ROCK)
#imag2.join(ROCK)
imag.up(imag2.img)
imag.up(imag2.img)
#imag.horizontalMirror()

#print (imag)
"""
#imag.up(imag2.img)
#imag.up(imag2.img)
#imag.join(imag2.img)
#imag.join(imag2.img)
#imag.horizontalRepeat(2)
#imag.verticalRepeat(3)
#imagg=imag.verticalMirror()
imaggt=imag.horizontalMirror()
draw(imaggt)



