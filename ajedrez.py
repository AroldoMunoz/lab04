
from interpreter import draw
from chessPictures import *
from picture import *
from pieces import *

imag=Picture(KING)
imag2=Picture(SQUARE)

print(len(KING[0]))
print(len(KING))
imag.join(ROCK)
imag2.join(ROCK)
imag.up(imag2.img)


#print (imag)

draw(imag)



