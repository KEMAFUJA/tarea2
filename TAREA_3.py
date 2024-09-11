class Nodo:
    """Clase que representa un nodo de un árbol binario."""
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    # Métodos getter y setter para 'valor'
    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    # Métodos getter y setter para 'izquierdo'
    def get_izquierdo(self):
        return self.izquierdo

    def set_izquierdo(self, izquierdo):
        self.izquierdo = izquierdo

    # Métodos getter y setter para 'derecho'
    def get_derecho(self):
        return self.derecho

    def set_derecho(self, derecho):
        self.derecho = derecho


class ArbolBinario:
    """Clase que representa un árbol binario con métodos para buscar, insertar y otras operaciones."""

    def __init__(self):
        self.raiz = None

    # Getter para la raíz
    def get_raiz(self):
        return self.raiz

    # Setter para la raíz
    def set_raiz(self, raiz):
        self.raiz = raiz

    def es_vacio(self):
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def es_hoja(self, nodo):
        """Verifica si un nodo es una hoja."""
        return nodo.izquierdo is None and nodo.derecho is None

    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        nuevo_nodo = Nodo(valor)
        if self.es_vacio():
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        """Método recursivo para insertar un nodo."""
        if nuevo_nodo.valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)

    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual, valor):
        """Método recursivo para buscar un valor."""
        if actual is None or actual.valor == valor:
            return actual
        if valor < actual.valor:
            return self._buscar_recursivo(actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(actual.derecho, valor)

    def altura(self, nodo=None):
        """Calcula la altura del árbol."""
        if nodo is None:
            return -1  # El árbol vacío tiene altura -1
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    def cantidad(self):
        """Devuelve la cantidad total de nodos en el árbol."""
        return self._cantidad_recursiva(self.raiz)

    def _cantidad_recursiva(self, nodo):
        """Método recursivo para contar los nodos."""
        if nodo is None:
            return 0
        return 1 + self._cantidad_recursiva(nodo.izquierdo) + self._cantidad_recursiva(nodo.derecho)

    def amplitud(self):
        """Devuelve el número máximo de nodos en un nivel del árbol."""
        if self.raiz is None:
            return 0
        max_nivel = 0
        cola = [self.raiz]
        while cola:
            max_nivel = max(max_nivel, len(cola))
            siguiente_nivel = []
            for nodo in cola:
                if nodo.izquierdo:
                    siguiente_nivel.append(nodo.izquierdo)
                if nodo.derecho:
                    siguiente_nivel.append(nodo.derecho)
            cola = siguiente_nivel
        return max_nivel

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

    def pre_orden(self):
        """Realiza un recorrido pre-orden del árbol."""
        return self._pre_orden_recursivo(self.raiz, [])

    def _pre_orden_recursivo(self, nodo, resultado):
        """Método recursivo para el recorrido pre-orden."""
        if nodo is not None:
            resultado.append(nodo.valor)
            self._pre_orden_recursivo(nodo.izquierdo, resultado)
            self._pre_orden_recursivo(nodo.derecho, resultado)
        return resultado

    def post_orden(self):
        """Realiza un recorrido post-orden del árbol."""
        return self._post_orden_recursivo(self.raiz, [])

    def _post_orden_recursivo(self, nodo, resultado):
        """Método recursivo para el recorrido post-orden."""
        if nodo is not None:
            self._post_orden_recursivo(nodo.izquierdo, resultado)
            self._post_orden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)
        return resultado


if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(20)
    arbol.insertar(15)

    print("In Orden:", arbol.in_orden())
    print("Pre Orden:", arbol.pre_orden())
    print("Post Orden:", arbol.post_orden())
    print("Altura del árbol:", arbol.altura())
    print("Cantidad de nodos:", arbol.cantidad())
    print("Amplitud del árbol:", arbol.amplitud())
