def is_valid_move(x, y, board, n):
    if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
        return True
    return False

def print_solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='\t')
        print()

def solve_warnsdorf(n):
    # Inicializar el tablero con -1 (indicando que ninguna casilla ha sido visitada)
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Movimientos posibles del caballo en el tablero
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Empezar desde una casilla arbitraria (puedes cambiar las coordenadas iniciales si lo deseas)
    start_x = 0
    start_y = 0
    
    # Colocar el primer movimiento en el tablero
    board[start_x][start_y] = 0
    
    # Contador de movimientos
    move_count = 1
    
    # Recursivamente encontrar el recorrido
    if not solve_warnsdorf_util(n, board, start_x, start_y, move_x, move_y, move_count):
        print("No hay solución")
    else:
        print_solution(board)

def solve_warnsdorf_util(n, board, curr_x, curr_y, move_x, move_y, move_count):
    if move_count == n * n:
        return True
    
    # Intentar todos los movimientos siguientes desde la posición actual
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        
        if is_valid_move(new_x, new_y, board, n):
            board[new_x][new_y] = move_count
            if solve_warnsdorf_util(n, board, new_x, new_y, move_x, move_y, move_count + 1):
                return True
            
            # Si el movimiento no conduce a la solución, deshacerlo
            board[new_x][new_y] = -1
    
    return False

# Ejemplo de uso
n = 8  # Tamaño del tablero de ajedrez
solve_warnsdorf(n)
