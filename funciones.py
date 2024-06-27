libros = []
ventas = []
titulo = []
valorlibro = []
genero = ['noficcion','ficcion','ciencia']
def registrar_libro():
    libros.append = input("Ingrese el Autor")
    titulo.append = input("Ingrese el titulo")
    genero.append = input("Ingrese el genero")
    valorlibro.append = int(input("Ingrese el valor del libro"))
    ({
    'libros': libros,
    'titulo': titulo,
    'genero': genero,
    'ValorLibro':valorlibro
    })

def listar_todos_los_libros():
    for i in (libros,ventas,titulo,valorlibro):
        print("")
def registrar_venta():
    print("registro de venta en proceso...")
    input("Ingrese el libro que llevara",libros)
    input("El valor del este libro es de",valorlibro)
#  Registrar venta: Para registrar una venta se requiere lo siguiente: Título del libro, Cantidad
#     vendida, precio por unidad y precio final. Debe validar que el título exista en el inventario y
#     que la cantidad no exceda el stock disponible. Simule una boleta estándar


def Imprimir_reporte_de_ventas():
    print("")
#     Para imprimir el reporte de ventas, el usuario puede seleccionar
# imprimir todos o por un género en específico. Estos géneros deben estar previamente
# definidos en una colección de Python en el código y por lo menos deben ser tres, por ejemplo:
# "Ficción", "No Ficción", "Ciencia".



def Generar_txt():
    print("")
    # Generar TXT: Debe exportar a un archivo txt con el registro de las ventas

