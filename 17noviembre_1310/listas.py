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
        while curr_node.data != value and curr_node.siguiente != None:  #Primero se recorre la lista buscando el elemento a eliminar
            curr_node = curr_node.siguiente
        if curr_node.data == value:
