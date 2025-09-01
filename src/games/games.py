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
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        opciones = ["piedra", "papel", "tijera"]

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        
        if jugador1 == jugador2:
            return "empate"
        
        reglas = {
            "piedra": "tijera",   # piedra gana a tijera
            "tijera": "papel",    # tijera gana a papel
            "papel": "piedra"     # papel gana a piedra
        }

        if reglas[jugador1] == jugador2:
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
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        for c in range(3):
            if tablero[0][c] != " " and tablero[0][c] == tablero[1][c] == tablero[2][c]:
                return tablero[0][c]

        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            if all(" " not in fila for fila in tablero):  # solo validar si tablero completo
                return tablero[0][0]
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if all(" " not in fila for fila in tablero):  # solo validar si tablero completo
                return tablero[0][2]

        for fila in tablero:
            if " " in fila:
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
        # Validar límites del tablero
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
