import mysql.connector


def conectar():
    global my_db, cursor
    my_db = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        database = 'tienda'
    )
    cursor = my_db.cursor()



def menu2(isActived, cursor):
    while isActived == True:
        print(f'Bienvenido, {nombre.title()}.')
        opcMenu2 = input('Seleccione una opción: \n 1.1 Ver usuarios \n 1.2 Modificar usuarios \n 1.3 Eliminar usuarios \n'+ '2.1 Crear producto \n 2.2 Ver productos \n 2.3 Buscar producto \n' + '3.1 Registrar ventas \n 3.2 Imprimir factura de venta \n 3.3 Ver compras por cliente \n'+'4. Salir \n')
        match opcMenu2:
            case '1.1':
                print('Listado de usuarios')
                cursor.execute('SHOW TABLES')
                for x in cursor:
                    print(x)
                print('------')
                print('------')
                print('------')
                pass
            case '1.2':
                print('Modificar usuarios')
                pass
            case '1.3':
                print('Eliminar usuarios')
                pass
            case '2.1':
                print('Crear producto')
                pass
            case '2.2':
                print('Ver productos')
                pass
            case '2.3':
                print('Buscar producto')
                pass
            case '3.1':
                print('Registrar ventas')
                pass
            case '3.2':
                print('Imprimir factura de venta')
                pass
            case '3.3':
                print('Ver compras por cliente')
                pass
            case '4':
                print('Salir')
                pass
            case _:
                print('Seleccione una opción válida')
        opcMenu2 = input('Seleccione una opción: \n 1.1 Ver usuarios \n 1.2 Modificar usuarios \n 1.3 Eliminar usuarios \n'+ '2.1 Crear producto \n 2.2 Ver productos \n 2.3 Buscar producto \n' + '3.1 Registrar ventas \n 3.2 Imprimir factura de venta \n 3.3 Ver compras por cliente \n'+'4. Salir \n')


print('Bienvenido')
opcion = int(input('Seleccione una opción: \n 1. Formulario \n 2. Login \n 3. Salir \n '))

isActived = False

while opcion != 3:
    try:
        match opcion:
            case 1:
                print('Formulario')
                nombre = input('Digite su nombre: ')
                conectar()
                pass
            case 2:
                print('Login')
                menu2(True, cursor)
                pass
            case 3:
                print('Salir')
            case _:
                print('Ingrese una opción válida')
                pass
        opcion = int(input('Seleccione una opción: \n 1. Formulario \n 2. Login \n 3. Salir \n '))
    except:
        print('Ingrese solo números')



