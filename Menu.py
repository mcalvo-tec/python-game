from Partida import Partida

## **** BLOQUE PRINCIPAL ****
class Menu:
  _userRows = 0
  _userCols = 0
  _minSize = 0
  _maxSize = 0
  _canContinue = False
  _exit = False
  _initGame = False
  _game = None

  def __init__(self):
    """Constructor principal"""
    self._userRows = 0
    self._userCols = 0
    self._minSize = 5 
    self._maxSize = 10
    self._canContinue = False
    self._exit = False
    self._initGame = False

  #Validamos que el usuario no ingrese un valor entre el rango [minSize, maxSize]
  # keyWord: Posibles valores "Filas" o "Cols"
  def ValidData(self, keyWord):
    valueFromUser = 0

    while(True):
      try:
        num = int(input(f'Ingrese la cantidad de {keyWord} deseadas: '))
        #Validamos que _minSize <= valor <= _maxSize 
        if (num >= self._minSize and num <= self._maxSize):
          valueFromUser = num
          break
        else:
          print(f'\n*** Ingrese un valor que se encuentre en el rango de [{self._minSize}, {self._maxSize}]***\n')
      except (ValueError):
        print("Por favor ingrese un valor de tipo entero...")
    return valueFromUser

  def MenuPrincipal(self):
    print("==========================================")
    print("\t\tMenu\n")
    print("==========================================")
    print("1- Inicializar partida - Nuevo Juego\n")
    print("2- Imprimir la primera matriz\n")
    print("3- Imprimir la segunda matriz\n")
    print("4- Jugar y determinar ganador\n")
    print("5- Cargar la ultima partida jugada\n")
    print("6- Salir del programa\n")
    print("==========================================")
    try:
      num = int(input("Digite un opcion: "))
      try:
        if (num >= 1 and num <= 6):
          self.ExecuteAction(num)
      except:
        print("Opcion invalida. Intente nuevamente")
    except ValueError:
      print("Por favor ingrese un valor de tipo entero...")

  def ExecuteAction(self, option):
    if (option == 1):
      self.InicializarPartida()
    elif (option == 2):
      self.ImprimirMatriz(1)
    elif (option == 3):
      self.ImprimirMatriz(2)
    elif (option == 4): 
      self.Jugar()
    elif (option == 5):
      self.CargarUltimaPartida()
    elif (option == 6):
      self.TerminarJuego()

  def InicializarPartida(self):
    print("\n\n *** Inicializando nueva partida... ****\n")
    self._userRows = self.ValidData("Filas")
    self._userCols = self.ValidData("Columnas")
    self._game = Partida(self._userRows, self._userCols)
    print("\n\tCreando matriz 1...\n")
    print("\tCreando matriz 2...\n")
    print("\tCreando matriz resultado, iniciada con 0...\n")
    print("\n\t *** Partida inicializada! ****\n")
    self._initGame = True
    self.MenuPrincipal()

  def ImprimirMatriz(self, numMatriz):
    if self._initGame == False:
      print("\n\t*** Advertencia: No se ha inicializado una nueva partida. Inicie partida o seleccione jugar. ***\n")
    else:
      if numMatriz == 1:
        self._game.print_matriz_1()
      else:
        self._game.print_matriz_2()

    self.MenuPrincipal()

  def Jugar(self):
    if self._initGame == True:
      self._game.play()
      self._game.save_game()

    else:
      print("\n\n\t*** Advertencia: Debe inicializar partida antes de jugar!! ***\n")
      self.InicializarPartida()
      self._game.play()
      self._game.save_game()

    self.MenuPrincipal()

  def CargarUltimaPartida(self):
    self._game.load_game()
    self.MenuPrincipal()

  def TerminarJuego(self):
    exit()
