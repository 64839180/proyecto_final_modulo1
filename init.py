from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.eliminar import DeleteImage

file = File()
file._data_load('covid/images')
# file.show_data()

while True:
    print("-" * 54)
    print("\nGestionar imágenes de COVID-19 Radiography Database:\n")
    print("       1: Agregar nueva imagen")
    print("       2: Modificar imagen")
    print("       3: Eliminar imagen")
    print("       0: Salir\n")
    print("-" * 54)

    try:
        opcion = int(input("Opción: "))
        if opcion == 1:
            print("Seleccionaste Opción 1")
            p = ProcessImage()
            p.copiar()       
        elif opcion == 2:
            print("Seleccionaste Opción 2")
            
        elif opcion == 3:
            print("Seleccionaste Opción 3")
            d = DeleteImage(file.images)  
            d.list_images()
            image_id = input("Ingrese el ID de la imagen a eliminar: ")
            d.delete(image_id)
        elif opcion == 0:
            print("Seleccionaste Opción 0")
            break
        else:       
            print("Opción no válida, seleccione una opción de la lista")
    except ValueError:
        print("Opción no válida, ingrese un número.")
    except Exception as e:
        print("Opción no válida, seleccione una opción de la lista")
        print("\nError: ", e, "\n")