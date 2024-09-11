class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def EsVacio(self):
        return self.raiz is None

    def EsHoja(self, nodo):
        return nodo.izq is None and nodo.der is None

    def InsertarNodo(self, x):
        if self.raiz is None:
            self.raiz = Nodo(x)
        else:
            self._insertar(self.raiz, x)

    def _insertar(self, nodo, x):
        if x < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(x)
            else:
                self._insertar(nodo.izq, x)
        else:
            if nodo.der is None:
                nodo.der = Nodo(x)
            else:
                self._insertar(nodo.der, x)

    def BuscarX(self, x):
        return self._buscar(self.raiz, x)

    def _buscar(self, nodo, x):
        if nodo is None:
            return False
        if nodo.valor == x:
            return True
        elif x < nodo.valor:
            return self._buscar(nodo.izq, x)
        else:
            return self._buscar(nodo.der, x)

    def InOrden(self):
        return self._inorden(self.raiz, [])

    def _inorden(self, nodo, recorrido):
        if nodo:
            self._inorden(nodo.izq, recorrido)
            recorrido.append(nodo.valor)
            self._inorden(nodo.der, recorrido)
        return recorrido

    def PostOrden(self):
        return self._postorden(self.raiz, [])

    def _postorden(self, nodo, recorrido):
        if nodo:
            self._postorden(nodo.izq, recorrido)
            self._postorden(nodo.der, recorrido)
            recorrido.append(nodo.valor)
        return recorrido

    def PreOrden(self):
        return self._preorden(self.raiz, [])

    def _preorden(self, nodo, recorrido):
        if nodo:
            recorrido.append(nodo.valor)
            self._preorden(nodo.izq, recorrido)
            self._preorden(nodo.der, recorrido)
        return recorrido

# Ejemplo de uso
arbol = ArbolBinario()
arbol.InsertarNodo(5)
arbol.InsertarNodo(3)
arbol.InsertarNodo(7)
arbol.InsertarNodo(2)
arbol.InsertarNodo(4)
arbol.InsertarNodo(6)
arbol.InsertarNodo(8)

print("InOrden:", arbol.InOrden())  # Salida: [2, 3, 4, 5, 6, 7, 8]
print("PostOrden:", arbol.PostOrden())  # Salida: [2, 4, 3, 6, 8, 7, 5]
print("PreOrden:", arbol.PreOrden())  # Salida: [5, 3, 2, 4, 7, 6, 8]
print("Buscar 4:", arbol.BuscarX(4))  # Salida: True
print("Buscar 10:", arbol.BuscarX(10))  # Salida: False
print("EsVacio:", arbol.EsVacio())  # Salida: False
