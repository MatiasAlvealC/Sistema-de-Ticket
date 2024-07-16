import os
# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'posix':  # Unix/Linux/MacOS
        _ = os.system('clear')
    elif os.name == 'nt':  # Windows
        _ = os.system('cls')