    print("\n1. Crear Ejecutivo")
print("2. Crear Área")
print("3. Crear Tipo de Ticket")
print("4. Crear Criticidad")
print("5. Ver Tickets")
print("0. Cerrar sesión")

opcion = input("Seleccione una opción: ")

if opcion == '0':
    break
elif opcion == '5':
    input("Presione Enter para continuar...")  # Pausar para permitir que el usuario vea los resultados
else:
    print("Opción no válida")
    input("Presione Enter para continuar...") 