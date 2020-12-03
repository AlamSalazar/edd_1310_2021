from array2d import array2d
from stack import Stack
class LaberintoADT:
    """
    0 pasillo , 1 pared , S salida , E entrada
    pasillo es una tupla((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    Entrada en una tupla(5,1)
    salida(2,5)
    """
    def __init__( self , rens , cols , pasillos , entrada , salida ):
        self.__laberinto = Array2D( rens , cols , '1' )
        for pasillo in pasillos:
              self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
            self.__set_entrada(entrada[0],entrada[1])
            self.set_salida(salida[0],salida[1])
            self.__camino = Stack()


    def to_string(self):
        self.__laberinto.to_string()

    #Establece entrada 'E' en la matriz, verificar limites perifericos
    def set_entrada( self , ren , col ):
        #terminar la validacion de las coordenadas
        self.__laberinto.set_item(ren,col,'E')

    #Establece salida 'S', dentro de los limites periericos de la matriz
    def set_salida( self , ren , col ):
        #Terminar las validaciones
        self.__laberinto.set_item(ren,col,'S')

    def es_salida(self,ren,col):
        return self.__laberinto.get_item(ren,col)=='S'

    def buscar_entrada(self):
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                tope = self.__camino.peek() #tupla  #tope=(2,1)
                if self.__laberinto.get_item(tope[0],tope[1]) == 'E':
                    self.__camino.push(tuple(renglon,columna))

    def set_pervia(self,pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #Aplicar reglas
        
