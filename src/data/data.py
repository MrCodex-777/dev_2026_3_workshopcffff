class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista = list(lista)  # Asegurarse de que sea una lista
        izquierda = 0
        derecha = len(lista) - 1
        while izquierda < derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1
        return lista

    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        lista = list(lista)  # Asegurarse de que sea una lista
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        
        lista = list(lista)
        resultado = []
        for item in lista:
            # Verificamos si existe un elemento con el mismo valor y el mismo tipo
            es_duplicado = False
            for r in resultado:
                if item == r and type(item) is type(r):
                    es_duplicado = True
                    break
            
            if not es_duplicado:
                resultado.append(item)
        return resultado
            
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        lista1 = list(lista1)  # Asegurarse de que sea una lista
        lista2 = list(lista2)  # Asegurarse de que sea una lista
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        # Agregar los elementos restantes
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        lista = list(lista)
        if not lista:  # Si la lista está vacía, la devolvemos tal cual
            return []
            
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        lista = list(lista)  # Asegurarse de que sea una lista
        n = len(lista) + 1  # El tamaño esperado de la lista completa
        suma_esperada = n * (n + 1) // 2  # Suma de la serie del 1 al n
        suma_actual = sum(lista)
        return suma_esperada - suma_actual

    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        conjunto1 = list(conjunto1)  # Asegurarse de que sea una lista
        conjunto2 = list(conjunto2)  # Asegurarse de que sea una lista
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []
        return {
            'push': lambda x: pila.append(x),
            'pop': lambda: pila.pop() if pila else None,
            'peek': lambda: pila[-1] if pila else None,
            'is_empty': lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []
        return {
            'enqueue': lambda x: cola.append(x),
            'dequeue': lambda: cola.pop(0) if cola else None,
            'peek': lambda: cola[0] if cola else None,
            'is_empty': lambda: len(cola) == 0
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        matriz = list(matriz)
        
        # 1. Si la matriz está vacía, devolvemos una lista vacía sin dar error
        if not matriz:
            return []
            
        # 2. Convertimos todas las filas internas a listas (por si el profe mandó tuplas)
        matriz = [list(fila) for fila in matriz]
        
        transpuesta = []
        for i in range(len(matriz[0])):
            nueva_fila = []
            for fila in matriz:
                nueva_fila.append(fila[i])
            transpuesta.append(nueva_fila)
            
        return transpuesta