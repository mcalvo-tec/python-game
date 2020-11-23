from MatrixMano import MatrixMano #comentar
from MatrixResult import MatrixResult #comentar 
from Partida import Partida
from Mano import Mano #comentar

def main():
    #m = MatrixMano(3, 3)
    #m1 = Mano(2)
    #m.define_elem(0, 0, m1)
    #m.print_matrix() 

    #m2 = MatrixResult(3, 3)
    #m2.print_matrix()

    partida = Partida(3, 3)
    #partida.print_matriz_1()
    #partida.print_matriz_2()
    #partida.print_matriz_resultado()
    #partida._matrizResultado.define_elem(0,0,1)
    #partida._matrizResultado.define_elem(1,1,2)
    #partida._matrizResultado.define_elem(2,2,1)
    partida.play()
    partida.save_game()
    partida.load_game()

    #partida.print_matriz_resultado()

if __name__ == "__main__":
    main()