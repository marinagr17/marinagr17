#1. Listar información: 
#Mostrar una lista de todos los platos disponibles en el menú, incluyendo el nombre, la categoria y el precio.
import json
with open ("archivojson.json","r") as archivo:
    datos=json.load(archivo)
#print(datos) con lo anterior importamos el archivo y lo abrimos en modo lectura (read)
def lista_platos (datos_menu):
    platos_disponibles={}
    for var in datos_menu["menu"]:
        a = var["disponible"]
        b = var["nombre_plato"]
        c = var["precio"]
        d = var["categoria"]
        if a==True:
            platos_disponibles[b]={c, d}
    return platos_disponibles

#2. Contar información: Contar cuantos platos están disponibles en el menú y 
#muestre cuantos platos hay en cada categoria. 
#Muestra también el numero de valoraciones de los clientes en todo el menú.
def contar_platos (datos_menu):
    cont=0
    cont_valoraciones=0
    platos_categoria={}

    for var in datos_menu["menu"]:
        a = var["disponible"]
        if a==True:
            cont=cont+1

        cont_valoraciones=cont_valoraciones+len(var["valoraciones"])

    categoria=var["categoria"]
    if categoria in platos_categoria:
        platos_categoria[categoria] =platos_categoria + 1
    else:
        platos_categoria[categoria] = 1

    print("Hay ", cont, "platos disponibles.")
    print("Hay ", cont_valoraciones, "valoraciones.")
    print("Número de platos por categoría:")
    for categoria, cantidad in platos_categoria.items():
        print(f"- {categoria}: {cantidad}")

    return

#3. Pedir al usuario una categoria de plato y mostrar todos los que están disponibles dentro de esa categoria.
def disponible_categoria (datos_menu):
    cat=input("Ingrese categoria: ")
    cat_list=[]
    categoria_existente = False
    for var in datos_menu["menu"]:
        if var["categoria"] == cat and var["disponible"]==True:
            cat_list.append(var["nombre_plato"])
            categoria_existente = True
    if not categoria_existente:
        print("La categoria ingresada no existe en el menú.")
    return cat_list
            

#4.Función que pida al usuario un ingrediente y muestre los platos 
#que contienen ese ingrediente en su lista. 
#Además, mostrará los platos vegetarianos y sin gluten disponibles.

def ingrediente_menu(datos_menu):
    ing = input("Introduce un ingrediente: ")
    platos_con_ingrediente = []
    platos_vegetarianos = []
    platos_sin_gluten = []
    ingrediente_existente = False
    for var in datos_menu["menu"]:
        if ing in var["ingredientes"]:
            platos_con_ingrediente.append(var["nombre_plato"])
            ingrediente_existente = True
        if var["vegetariano"]:
            platos_vegetarianos.append(var["nombre_plato"])
        if var["libre_de_gluten"]:
            platos_sin_gluten.append(var["nombre_plato"])
    if not ingrediente_existente:
        print("El ingrediente no existe en el menu.")
    mensaje_ingrediente = f"Los platos que contienen el ingrediente '{ing}' son: {platos_con_ingrediente}" 
    mensaje_vegetarianos = f"Los platos vegetarianos son: {platos_vegetarianos}"
    mensaje_sin_gluten = f"Los platos libres de gluten son: {platos_sin_gluten}"
    return mensaje_ingrediente, mensaje_vegetarianos, mensaje_sin_gluten

#5. Función que permita al usuario buscar platos por su precio dentro de un rango específico. 
#Además, muestra el nombre del plato, su categoría y el precio correspondiente.
def rango_precios(datos_menu):
    minimo=float(input("Introduce un precio minimo: "))
    maximo=float(input("Introduce un valor maximo: "))
    platos_rango={}
    for var in datos_menu["menu"]:
        b = var["nombre_plato"]
        c = var["precio"]
        d = var["categoria"]
        if var["precio"]>=minimo and var["precio"]<=maximo:
            platos_rango[b]={d, c}
    return platos_rango

#MENU
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

num=0
while num!=6:
    print(Fore.MAGENTA + "MENÚ:\n 1.Lista de platos disponibles.\n 2.Ver cuantos platos estan disponibles, cuantos tiene cada categoŕia y numero de valoraciones.\n 3.Ingrese categoria para ver disponibilidad.\n 4.Ingrese ingrediente para ver que platos lo llevan.\n 5.Introducir rango de precios.")
    num=int(input(Fore.CYAN + "Ingrese un numero: "))
    if num==1:
        menu=lista_platos(datos)
        print(menu)
    if num==2:
        lista_contar=contar_platos(datos)
        print(lista_contar)
    if num==3:
        categ=disponible_categoria(datos)
        print (categ)
    if num==4:
        ingrediente=ingrediente_menu(datos)
        print(ingrediente)
    if num==5:
        rango=rango_precios(datos)
        print("Plato(s) disponible(s) en el rango introducido: ", rango)
if num==6:
    print("Fin del programa.")
