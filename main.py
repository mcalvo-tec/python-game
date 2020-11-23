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
    partida.print_matriz_resultado()
    partida.save_game()

if __name__ == "__main__":
    main()