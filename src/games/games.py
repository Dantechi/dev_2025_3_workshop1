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
        j1 = jugador1.strip().lower()
        j2 = jugador2.strip().lower()

        #si eligieron lo mismo , empate 
        if j1 == j2:
            return "empate"
        
        #juego general 
        if (j1=="piedra" and j2=="tijera") or (j1=="tijera" and j2=="papel") or (j1=="papel" and j2=="piedra"):
            return "jugador 1"
        else:
            return "jugador 2"
           
    
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
        # Revisar filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        # Revisar columnas
        for c in range(3):
            if tablero[0][c] != " " and tablero[0][c] == tablero[1][c] == tablero[2][c]:
                return tablero[0][c]

        # Revisar diagonales
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        # Si no hay ganador y aún hay espacios, el juego continúa
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si no hay ganador y no hay espacios, es empate
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
        combinacion = []
        i = 0
        while len(combinacion) < longitud:
            combinacion.append(colores_disponibles[i % len(colores_disponibles)])
            i += 1
        return combinacion
    
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
        # No moverse de casilla
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Debe ser misma fila o misma columna
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Debe haber una pieza en el origen (opcional, pero útil)
        if tablero[desde_fila][desde_col] == " ":
            return False

        # Calcular el paso (dirección) a recorrer
        paso_fila = 0
        if hasta_fila > desde_fila:
            paso_fila = 1
        elif hasta_fila < desde_fila:
            paso_fila = -1

        paso_col = 0
        if hasta_col > desde_col:
            paso_col = 1
        elif hasta_col < desde_col:
            paso_col = -1

        # Revisar que el camino intermedio esté libre (sin incluir destino)
        f = desde_fila + paso_fila
        c = desde_col + paso_col
        while f != hasta_fila or c != hasta_col:
            if tablero[f][c] != " ":
                return False
            f += paso_fila
            c += paso_col

        # Si llegamos aquí, el camino está libre y el movimiento es en línea recta
        return True