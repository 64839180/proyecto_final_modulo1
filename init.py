from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.eliminar import DeleteImage
file = File()
file._data_load('covid/images')
#file.show_data()
    
while True:
    print("-" * 54)
    print("\nGestionar imagenes de COVID-19 Radiography Database:\n")
    print("       1: Agregar nueva imagen")
    print("       2: Modificar imagen")
    print("       3: Eliminar imagen")
    print("       0: Salir\n")
    print("-" * 54)

    try:
        opcion = int(input("Opcion: "))

        if opcion == 1:
            print("Selecionaste Opcion 1")
            p = ProcessImage()
            p.copiar()       
        
        elif opcion == 2:
            print("Selecionaste Opcion 2")
        elif opcion == 3:
            print("Seleccionaste Opción 3")
            d = DeleteImage(file.data)  # Pasar los datos cargados
            d.list_images()  # Mostrar imágenes disponibles
            image_id = input("Ingrese el ID de la imagen a eliminar: ")
            d.delete(image_id)  # Eliminar la imagen
        elif opcion == 0:
            print("Selecionaste Opcion 0")
            break
        else:       
            print("Opcion no valida seleccione una opcion de la lista")
    except Exception as e:
        print("Opcion no valida seleccione una opcion de la lista")
        print("\nError: ", e, "\n")
