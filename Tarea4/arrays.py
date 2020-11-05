class Array:
    def __init__( self, tam ):
        self.__nTrabajador = [ 0 for x in range (tam) ]
        self.__nombre = [ 0 for x in range (tam) ]
        self.__paterno = [ 0 for x in range (tam) ]
        self.__materno = [ 0 for x in range (tam) ]
        self.__horasExtra = [ 0 for x in range (tam) ]
        self.__sueldoBase = [ 0 for x in range (tam) ]
        self.__anoIngreso = [ 0 for x in range (tam) ]

    def set( self , dato, position):
        try:
            self.__nTrabajador[ position ] = dato[position][0]
            self.__nombre[ position ] = dato[position][1]
            self.__paterno[ position ] = dato[position][2]
            self.__materno[ position ] = dato[position][3]
            self.__horasExtra[ position ] = dato[position][4]
            self.__sueldoBase[ position ] = dato[position][5]
            self.__anoIngreso[ position ] = dato[position][6]

        except Exception as e:
             print(f"Error : {e}")
             
    def get_nTrabajador( self, position):
        try:
            dato = self.__nTrabajador[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_nTrabajador( self , dato, position):
        try:
            self.__nTrabajador[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
             
    def get_nombre( self, position):
        try:
            dato = self.__nombre[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_nombre( self , dato, position):
        try:
            self.__nombre[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
    
    def get_paterno( self, position):
        try:
            dato = self.__paterno[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_paterno( self , dato, position):
        try:
            self.__paterno[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
             
    def get_materno( self, position):
        try:
            dato = self.__materno[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_materno( self , dato, position):
        try:
            self.__materno[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
             
    def get_horasExtra( self, position):
        try:
            dato = self.__horasExtra[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_horasExtra( self , dato, position):
        try:
            self.__horasExtra[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
    
    def get_sueldoBase( self, position):
        try:
            dato = self.__sueldoBase[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_sueldoBase( self , dato, position):
        try:
            self.__sueldoBase[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
             
    def get_anoIngreso( self, position):
        try:
            dato = self.__anoIngreso[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_anoIngreso( self , dato, position):
        try:
            self.__anoIngreso[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
             
    def get_length( self ):
        return len( self.__nTrabajador )
    
    def clear( self, dato):
        self.__nTrabajador = [ dato for x in range (len(self.__nTrabajador	)) ]
        self.__nombre = [ dato for x in range (len(self.__nombre	)) ]
        self.__paterno = [ dato for x in range (len(self.__paterno	)) ]
        self.__materno = [ dato for x in range (len(self.__materno	)) ]
        self.__horasExtra = [ dato for x in range (len(self.__horasExtra	)) ]
        self.__sueldoBase = [ dato for x in range (len(self.__sueldoBase	)) ]
        self.__anoIngreso = [ dato for x in range (len(self.__anoIngreso	)) ]

    def __iter__( self ):
        return IteradorArreglo( self.__nTrabajador )
    


class IteradorArreglo:
    def __init__( self, arr ):
        self.__arr = arr
        self.__indice = 0
    
    def __iter__( self ):
        return self
    
    def __next__( self ):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
    



