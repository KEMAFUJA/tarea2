class Nodo:
    """Clase que representa un nodo de un árbol binario de búsqueda."""
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def __repr__(self):
        return f"Nodo({self.valor})"

class ArbolBinarioBusqueda:
    """Clase que representa un árbol binario de búsqueda."""

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un valor en el árbol binario de búsqueda."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        """Método recursivo para insertar un valor en el árbol binario de búsqueda."""
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def eliminar(self, valor):
        """Elimina un valor del árbol binario de búsqueda."""
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        """Método recursivo para eliminar un valor en el árbol binario de búsqueda."""
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Nodo con solo un hijo o sin hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Nodo con dos hijos: obtener el sucesor inorden
            temp = self._encontrar_minimo(nodo.derecho)
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.valor)
        
        return nodo

    def _encontrar_minimo(self, nodo):
        """Encuentra el nodo con el valor mínimo en un árbol."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def in_orden(self):
        """Realiza un recorrido in-orden del árbol."""
        return self._in_orden_recursivo(self.raiz, [])

    def _in_orden_recursivo(self, nodo, resultado):
        """Método recursivo para el recorrido in-orden."""
        if nodo is not None:
            self._in_orden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._in_orden_recursivo(nodo.derecho, resultado)
        return resultado

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(20)
arbol.insertar(15)
arbol.eliminar(10)  # Elimina el nodo con valor 10

print("In Orden:", arbol.in_orden())  # Verifica el estado del árbol después de la eliminación
