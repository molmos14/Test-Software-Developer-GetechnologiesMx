''' 
    Manuel Olmos Antillón 

    1) ¿Qué es la programación orientada a objetos? En qué casos utilizarla?
        Esta programación es más usada en la parte de videojuegos ya que con ella puedes
        crear un objeto con ciertas características que hacen que pueda ser usado en 
        diferentes ocasiones. Pongamos el ejemplo de un personaje de videojuego, el cual 
        es de clase humano, que tiene como caracteristicas vida, color de ojos, color de piel,
        altura, etc. Esta no solo sirve para videojuegos ya que, puede ser usada en desarrollo
        de cualquier cosa, por que permite darle valores a algo y usarlo las veces que quieras.

    2) Si realizamos un sistema de inventarios para un supermercado desde 0, cuáles serían
    tus preguntas hacia el cliente?
        - Historial de los inventarios más recientes
        - Productos, precios 
        - cantidad en la que compras los productos
        - filtros que quisieras colocar para mejor visualizacion de los productos
        - ¿como lo quieres? (app movil, pagina web, aplicación escritorio)
        - funciones extras que te gustaria implementar una vez que funcione la beta
        - quieres que contenga un apartado de business intelligence para mejor toma de 
          decisiones en la empresa?
        
'''

########################################## Ejercicio 1 ######################################
# Realiza un programa, valida si es una fecha válida y formato. Formato esperado dd/MM/yyyy

def fecha_correcta(fecha):
    while True:
        list(fecha)
        dia = int(fecha[0] + fecha[1])
        mes = int(fecha[3] + fecha[4])
        año = fecha[6:]
        if 1 <= dia <= 31 and 1 <= mes <= 12 and len(año)== 4:
            print('Es una fecha válida')
            return fecha
            break
        else:
            fecha_correcta = input('Error en la fecha por favor digite una correcta\nDame una nueva fecha dd/MM/yyyy: ')
            return fecha_correcta
# fecha_correcta('14/66/2004')

########################################## Ejercicio 2 ######################################
# Realiza un programa, el usuario puede introducir una cadena de caracteres y le mostraras
# de salida cuántos números existen en la cadena.

def cuenta_digitos_en_cadena():
    cadena = list(input('Escribe la cadena a evaluar: '))
    numeros = 0
    for num in cadena:
        if num.isdigit():
            numeros += 1
    print(f'Tu cadena tiene: {numeros} numeros')

# cuenta_digitos_en_cadena()

########################################## Ejercicio 3 ######################################
'''
    Realiza un programa que despliega un menú con las siguientes opciones:
        - Registrar empleados, con las siguientes características: id, nombre,
        apellido paterno, apellido materno, fecha de nacimiento.
        - Obtener la edad de un empleado, pasando por parámetro de búsqueda el id.
        - Obtener lista de empleados por orden alfabético apellido.
        - Obtener lista de empleados por orden de edad.
'''
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    while True:
        pregunta = input('\nDesea utilizar el programa? y/n: ')
        if pregunta != 'n':
            num = menu()
            if num == 1:
                df = registrar_empleados()
            elif num == 2:
                edad_empleado(df)
            elif num == 3:
                listar_orden_alph(df)
            elif num == 4:
                listar_por_edad(df)
        else:
            print('\nVuelva Pronto!\n')
            break

def menu():
    print('''
        1) Registrar empleado (nombre, apellido paterno, apellido materno, fecha nacimiento)   
        2) Obtener edad con base al id
        3) Filtrar empleados por apellido en orden alfabético
        4) Filtrar empleados por edad 
    ''')
    num = int(input('Elija la funcion que desea ocupar: '))
    return num

def registrar_empleados():
    DataFrame = pd.DataFrame(columns = ['Nombre','ApellidoP','ApellidoM','fechaNacimiento','edad'])
    cuantos = int(input('\nCuantos empleados desea agregar?: '))

    for i in range(cuantos):
        apellidoP = input('\nDame el primer apellido del empleado: ')
        apellidoM = input('Dame el segundo apellido del empleado: ')
        nombre = input('Dame el nombre del empleado: ')
        nacimiento = fecha_correcta(input('Dame la fecha dd/MM/yyyy: '))
        fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        años = edad.years
        DataFrame = DataFrame.append(pd.DataFrame({'Nombre': [nombre], 'ApellidoP': [apellidoP], 'ApellidoM': [apellidoM], 'fechaNacimiento': [nacimiento],'edad': [años]}),ignore_index=True)

    print(f'\n{DataFrame}')
    return DataFrame

def edad_empleado(df):
    print(df)
    pos = int(input('Dame el id de la persona que quieres obtener su edad: '))
    fecha = df.iloc[pos]['fechaNacimiento']
    fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fecha_nacimiento)
    print(f'{edad.years} años')

def listar_orden_alph(df):
    print(df.sort_values(by =['ApellidoP','ApellidoM']))

def listar_por_edad(df):
    print(df.sort_values(by =['edad'], ascending = [False]))

if __name__ == '__main__':
    main()