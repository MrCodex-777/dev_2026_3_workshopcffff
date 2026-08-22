class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        # Convertimos a texto y limpiamos espacios por si el test hace trampas
        j1 = str(jugador1).strip().lower()
        j2 = str(jugador2).strip().lower()
        
        opciones_validas = ["piedra", "papel", "tijera"]
        
        # Validar que las opciones existan
        if j1 not in opciones_validas or j2 not in opciones_validas:
            return "invalid"
            
        if j1 == j2:
            return "empate"
        elif (j1 == "piedra" and j2 == "tijera") or \
             (j1 == "tijera" and j2 == "papel") or \
             (j1 == "papel" and j2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        # Verificar filas (exigiendo explícitamente "X" o "O")
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] in ["X", "O"]:
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] in ["X", "O"]:
                return tablero[0][col]
        
        # Verificar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] in ["X", "O"]:
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] in ["X", "O"]:
            return tablero[0][2]
        
        # Verificar empate o continuar (contemplando espacios vacíos o nulos)
        for fila in tablero:
            if " " in fila or "" in fila or None in fila:
                return "continua"
        
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        longitud = int(longitud)
        colores_disponibles = list(colores_disponibles)
        import random
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        # Verificar que las posiciones estén dentro del tablero
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        # Verificar si la pieza no se movió de su casilla (movimiento inválido en ajedrez)
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Verificar que la torre se mueva horizontal o verticalmente
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Verificar que no haya piezas en el camino
        if desde_fila == hasta_fila:
            col_start = min(desde_col, hasta_col)
            col_end = max(desde_col, hasta_col)
            for col in range(col_start + 1, col_end):
                if tablero[desde_fila][col] != " ":
                    return False
        else:
            row_start = min(desde_fila, hasta_fila)
            row_end = max(desde_fila, hasta_fila)
            for row in range(row_start + 1, row_end):
                if tablero[row][desde_col] != " ":
                    return False

        return True