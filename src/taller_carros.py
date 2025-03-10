carros = ["sentra", "corolla", "civic", "jetta", "aveo", "mustang"]
ACCIONES = """
Acciones:
1) Agregar un carro
2) Eliminar un carro
3) Ordenar el inventario
4) Salir
"""
BIENVENIDA = "BIENVENIDO , CON ESTE PROGRAMA PODRAS "
DESPEDIDA = "ADIOS ESPERO VERTE PRONTO POR ACA"
carro= ["carro1","carro2","carro3","carro4"]
def iniciar_taller():
    for carro in carros:    
        print(carro.title())
        print(ACCIONES)

    decision= int(input("Dime qué opción deseas realizar: ").strip())
    if decision == 1:
        dato1=(input("pon aqui el nombre de algun carro que desees agregar"))
        carro.append(dato1)
    elif decision == 2:
                print("hola soy el 2")
    else:
                print("pon una opcion valida")
    
print(DESPEDIDA)