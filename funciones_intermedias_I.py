#1   Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Cambie el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0] = 15
print(x)
# Cambie el apellido del primer estudiante de 'Jordan' a 'Bryant'
students[0]['last_name'] = "Bryant"
print(students)
# En el directorio_deportes, cambia "Messi" por "Andrés".
sports_directory['soccer'][0] = 'Andres'
print( sports_directory['soccer'])
# Cambiar el valor en z de 20 a 30
z[0]['y'] = 30
print(z)

#2   Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada 
# diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_dictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#3   Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar: 
# Michael
# John
# Mark
# KB
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):

        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',estudiantes)

# Y iterateDictionary2('last_name', estudiantes) debería generar:
# Jordan
# Rosales
# Guillen
# Tonel
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('last_name',estudiantes)

#4   Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas,imprima el nombre 
# de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada 
# clave. Por ejemplo:
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)

# salida:
#7 UBICACIONES
# San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
    
#8 INSTRUCTORES
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon
