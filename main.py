import funciones as fn
while True:
    print("1. Registrar libro")
    print("2. Listar todos los libros") 
    print("3. Registrar venta")
    print("4. Imprimir reporte de ventas")
    print("5. Generar txt")
    print("6. Salir del Programa")
    opcion = int(input("Ingrese una Opcion: "))

    if opcion == 1:
        fn.registrar_libro()
    elif opcion == 2:
        fn.listar_todos_los_libros()
    elif opcion == 3:
        fn.registrar_venta()
    elif opcion == 4:
        fn.Imprimir_reporte_de_ventas()
    elif opcion == 5:
        fn.Generar_txt()
    elif opcion == 6:
        break
    