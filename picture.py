from colors import *
class Picture:
  
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    #for value in self.img:
  #  	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, chess):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    ny=len(self.img)
    nx=len(self.img[0])
    nny=len(chess)
    nnx=len(chess[0])
    nuevo=self.img
    for j in range(0,nny):
      for i in range(0,nnx):
        nuevo[j]=nuevo[j]+chess[j][i]
        
    """nny=len(chess)
    nuevo=self.img
    for j in range(0,nny):
        nuevo[j]=nuevo[j]+chess[j]
    return nuevo"""


  def up(self, chess):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        debajo de la figura actual """
    nny=len(chess)
    nuevo=self.img
    for j in range(0,nny):
        nuevo.append(chess[j])
    return nuevo

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
