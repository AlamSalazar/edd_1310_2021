class Nodo:
    def __init__( self , value , siguiente = None):
        self.data = value       #Falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__( self ):   #Se crea el constructor
        self.__head = None  #Como cuando se crea la lista está vacia, entonces apunta a entonces apunt a None

    def is_empty( self ):
        return self.__head == None

    def append( self, value):
        nuevo = Nodo( value )
        if self.__head == None: #self.is_empty()
            self.__head = nuevo
        else:
            curr_node = self.__head
                curr_node = curr_node.siguiente
                while curr_node.siguiente != None: #verifica si se llegó al final
            curr_node.siguiente = nuevo

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data}-> ", end="")
            curr_node = curr_node.siguiente
        print("")

    def remove( self , value ):
        curr_node = self.__head
        if self.__head.data == value: #Comprueba si es en el primer dato
            self.__head = self.__head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print("El dato no existe en la lista")

    def prepend( self , value ):
        nuevo = Nodo( value , self.__head )
        self.__head = nuevo

    def tail( self ):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get( self , posicion=None ):  #Por defecto regresa último
        curr_node = self.__head
        contador = 0  #Sirve para conseguir un dato
        dato = None
        if posicion == None:
            dato = self.tail().data
        if posicion != None:
            while contador != posicion:
                contador +=1
                dato = curr_node
                curr_node = curr_node.siguiente
        return dato

    def tamanio( self ):
        curr_node = self.__head
        tam = 0
        while curr_node != None:
            curr_node = curr_node.siguiente
            tam+=1
        return tam
