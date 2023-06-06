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
    for value in self.img:
      vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    horizon=[]
    n=len(self.img)
    nn=len(self.img[0])
    
    for i in range(n):
      horizon.append([])
      for j in range(nn):
        horizon[i].append(self.img[i][nn-1-j])
    return horizon
    """ Devuelve el espejo horizontal de la imagen """
    

  def negative(self):
    
    """ Devuelve un negativo de la imagen """
    return self._invColor

  def join(self, chess):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    """ny=len(self.img)
    nx=len(self.img[0])
    nny=len(chess)
    nnx=len(chess[0])
    nuevo=self.img
    for j in range(0,nny):
      for i in range(0,nnx):
        nuevo[j]=nuevo[j]+chess[j][i]
        """
    nny=len(chess)
    nuevo=self.img
    for j in range(0,nny):
        nuevo[j]=nuevo[j]+chess[j]
        
    return nuevo


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
    chess=self.img
    nny=len(chess)
    nuevo=self.img
    for i in range(n):
      for j in range(0,nny):
          nuevo[j]=nuevo[j]+chess[j]
        
    return nuevo
    
    """horiz=[]
      
    
    for i in range(0,n):
      horiz.append(self.img)"""
    """
    for i in range(0,n):
      horiz.join(self)
      """
    
  def verticalRepeat(self, n):
    verti=[]
    #pri=self.img
    for i in range(0,n):
      verti=verti+self.img
    return verti
  
    

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario
    sentido horario """

    horizon=[]
    n=len(self.img)
    nn=len(self.img[0])
    
    for i in range(n):
      horizon.append([])
      for j in range(nn):
        horizon[i].append(self.img[nn-1-j][i])
    return horizon
   
