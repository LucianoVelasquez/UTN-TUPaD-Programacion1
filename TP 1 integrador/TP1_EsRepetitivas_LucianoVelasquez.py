#Ejercicio 1— “Caja del Kiosco”
def caja_kiosco():
    
    #Pedir nombre del cliente
    nombre_cliente = str(input("Introduzca su nombre: "))

    while not nombre_cliente.isalpha():
        print("Su nombre debe contener solo letras (sin simbolos ni espacios), vuelva a introducirlo.")
        nombre_cliente = str(input("Introduzca su nombre: "))


    #Pedir cantidad de productos comprados
    cant_product_comprados = input("Ingrese la cantidad de productos a comprar: ")

    while not cant_product_comprados.isdigit() and int(cant_product_comprados) != 0:
        print("La cantidad ingresada debe ser un numero positivo")
        cant_product_comprados = input("Ingrese nuvamente la cantidad de productos a comprar: ")

    #Por cada producto, pedir precio y validar descuento.
    precio = 0
    total = 0
    total_descuento = 0
    ahorro_total = 0
    promedio_por_producto = 0
    descuento = ""

    for i in range(int(cant_product_comprados)):
        
        precio = input(f"Introdusca el precio del producto n°{i+1}: ")
        while not precio.isdigit():
            precio = input("Introdusca nuevamente un numero mayor a 0: ")

        descuento = input("Tiene descuento?(S/N): ")
        while descuento.lower() != "s" and descuento.lower() != "n":
            descuento = input("Introdusca nuevamente, Tiene descuento?(S/N): ")

        print(f"Producto n°{i+1} Precio: {precio}   Descuento (S/N):{descuento}")

        total += int(precio)

        if(descuento == "s"):
            total_descuento += int(precio)-(int(precio)*0.1)
        else:
            total_descuento += int(precio)


    #Mostrar Resultados
    print(f"""g
    Cliente:{nombre_cliente}
    Cantidad de productos:{cant_product_comprados}
    Total sin duscuentos: ${total}
    Total con descuentos: ${total_descuento}
    Ahorro: ${total-total_descuento}
    Promedio por producto: ${(total_descuento / int(cant_product_comprados)):.2f}
    """)

    return

#Ejercicio 2 — “Acceso al Campus y Menú Seguro
def acceso_seguro():

    #Iniciar variables
    usuario_correcta = "alumno"
    clave_correcta = "python123"
    opcion = 0

    #Pedir credeciales.
    for i in range(3):
        user = input("Ingrese el usuario: ")
        passowrd = input("Ingrese contrasenia: ")
        print(f"""Intento {i+1}/3
                usuario: {user}
                clave: {passowrd}""")
        if(user == usuario_correcta and passowrd == clave_correcta):
            print("Acceso concedido.")
            break
        else:
            print("Usuario o Contrasenia incorrectos.")

        if (i == 2):
            return  print("Cuenta Bloqueada.")    

    #Mostrar menu
    while opcion != "4":
        opcion = input(f"""
            1. Ver estado de inscripción
            2. Cambiar clave 
            3. Mostrar mensaje motivacional 
            4. Salir
        """)

        if(not opcion.isdigit()):
            print("Debe ser un numero")
        elif(opcion == "1" ):
            print("Incripto")
        elif(opcion == "2"):
            clave_correcta = input("Ingrese nueva clave: ")

            if(len(clave_correcta) < 6):
                print("debe tener mínimo 6 caracteres")

        elif(opcion == "3"):
            print("Tu puedes!!")        
        elif(opcion > "4"):
            print("Fuera de rango.")    

    return
  

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)
def agenda_turnos():

    #Variables
    lunes1 = "Libre"
    lunes2 = "Libre"
    lunes3 = "Libre"
    lunes4 = "Libre"
    martes1 = "Libre"
    martes2 = "Libre"
    martes3 = "Libre"
    nombre_operador = input("Nombre del operador: ")
    nombre_paciente = ""
    opcion = "0"
    contador_lunes = 0
    contador_martes = 0
    dia_mas_turnos = 0

    #Menu
    while opcion != "5":
        print("-"*80)
        opcion = input(f"""
            1. Reservar turno
            2. Cancelar turno (por nombre)
            3. Ver agenda del día
            4. Ver resumen general
            5. Cerrar sistema
        """)
        print("-"*80)

        #Reserva de turnos
        if(opcion == "1"):
            dia = input("Ingrese el dia del turno (Lunes/Martes): ")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            
            while not nombre_paciente.isalpha():
                nombre_paciente = input("Ingrese nombre de paciente (SOLO LETRAS): ")

            if(dia.lower() == "lunes" ):
                if(lunes1 == "Libre"):
                    lunes1 = f"Lunes Turno 1 - Nombre de paciente: {nombre_paciente}"
                    contador_lunes += 1
                elif(lunes2 == "Libre"):
                    lunes2 = f"Lunes Turno 2 - Nombre de paciente: {nombre_paciente}"
                    contador_lunes += 1
                elif(lunes3 == "Libre"):
                    lunes3 = f"Lunes Turno 3 - Nombre de paciente: {nombre_paciente}"
                    contador_lunes += 1
                elif(lunes4 == "Libre"):
                    lunes4 = f"Lunes Turno 4 - Nombre de paciente: {nombre_paciente}"
                    contador_lunes += 1
                else:
                    print("No hay turnos disponibles para el Lunes")          
            elif(dia.lower() == "martes"):
                if(martes1 == "Libre"):
                    martes1 = f"Martes Turno 1 - Nombre de paciente: {nombre_paciente}"
                    contador_martes += 1
                elif(martes2 == "Libre"):
                    martes2 = f"Martes Turno 2 - Nombre de paciente: {nombre_paciente}"
                    contador_martes += 1
                elif(martes3 == "Libre"):
                    martes3 = f"Martes Turno 3 - Nombre de paciente: {nombre_paciente}"
                    contador_martes += 1
                else:
                    print("No hay turnos disponibles para el Martes")     
            else:
                print("Error, Los turnos son los dias Lunes y Martes")
        #Canselar turno        
        elif(opcion == "2"):
            dia = input("Ingrese el dia del turno a cancelar (Lunes/Martes): ")
            nombre_paciente = input("Ingrese el nombre del paciente: ")

            while not nombre_paciente.isalpha():
                nombre_paciente = input("Ingrese nombre de paciente (SOLO LETRAS): ")

            if(dia.lower() == "lunes"):
                if(lunes1 != "Libre" and nombre_paciente in lunes1):
                    lunes1 = "Libre"
                    contador_lunes -= 1
                elif(lunes2 != "Libre" and nombre_paciente in lunes2):
                    lunes2 = "Libre"
                    contador_lunes -= 1
                elif(lunes3 != "Libre" and nombre_paciente in lunes3):
                    lunes3 = "Libre"
                    contador_lunes -= 1
                elif(lunes4 != "Libre" and nombre_paciente in lunes4):
                    lunes4 = "Libre"
                    contador_lunes -= 1
                else:
                    print(f"No existen turnos para el paciente {nombre_paciente} el dia Lunes")          
            elif(dia.lower() == "martes"):
                if(martes1 != "Libre" and nombre_paciente in martes1):
                    martes1 = "Libre"
                    contador_martes =-1
                elif(martes2 != "Libre" and nombre_paciente in martes2):
                    martes2 = "Libre"
                    contador_martes =-1
                elif(martes3 != "Libre" and nombre_paciente in martes3):
                    martes3 = "Libre"
                    contador_martes =-1
                else:
                    print(f"No existen turnos para el paciente {nombre_paciente} el dia Martes")        
            else:
                print("Error, Los turnos son los dias Lunes y Martes")
        #Ver agenda del dia        
        elif(opcion == "3"):
                dia = input("Ingrese el dia del turno (Lunes/Martes): ")
                if (dia == "lunes"):
                    print(f"""
                        Turnos del Lunes:
                        {lunes1}
                        {lunes2}
                        {lunes3}
                        {lunes4}
                    """)
                else:
                    print(f"""
                        Turnos del Martes:
                        {martes1}
                        {martes2}
                        {martes3}
                    """)
        #Ver resumen general.   
        elif(opcion == "4"):

            if(contador_lunes == contador_martes):
                dia_mas_turnos = "Empate"
            elif(contador_lunes > contador_martes):
                dia_mas_turnos = "Lunes"
            else:
                dia_mas_turnos = "Martes"    

            print(f"""
                Turnos del Lunes:
                {lunes1}
                {lunes2}
                {lunes3}
                {lunes4}
                Turnos del Martes:
                {martes1}
                {martes2}
                {martes3}
                Dias con mas turnos:
                {dia_mas_turnos}
            """)
    return

#Ejercicio 4 — “Escape Room: La Bóveda”
def boveda():
    #Variables
    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    agente = ""
    opcion = ""
    count_forzar = 0
    bloqueo_alarma = False
    input_numero = 0

    #Pedir Nombre del agente
    agente = input("Introduzca nombre del agente: ")

    while not agente.isalpha():
        agente = input("Introduzca nombre del agente (solo letras): ")

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo_alarma:

        if(alarma and tiempo <= 3):
            bloqueo_alarma = True
            break

        #Menu
        print("-"*80)
        opcion = input(f"""
            1 - Forzar cerradura
            2 - Hackear panel
            3 - Descansar
        """)
        print("-"*80)

        if(not opcion.isdigit()):
            continue

        #Forzar cerradura
        if(opcion == "1" ):
            energia -=20
            tiempo -=2
            count_forzar += 1

            if(count_forzar >= 3):
                print("La cerradura se trabó, alarma activada.")
                alarma = True
                continue

            if(energia < 40):
                input_numero = int(input("Ingrese un numero del 1 al 3: "))
                while input_numero < 0 or input_numero > 3:
                    input_numero = int(input("Ingrese nuevamente un numero del 1 al 3: "))
                if(input_numero == "3"):
                    alarma = True   
                    print("La cerradura se trabó, alarma activada.") 

            if(not alarma):
                cerraduras_abiertas += 1
                print("Se abrio una ceradura.")
        #Hackear panel        
        elif(opcion == "2"):
            count_forzar = 0
            energia -=10
            tiempo -=3
            letra = ""

            for i in range(4):
                letra = input("Ingrese una letra: ")
                while len(letra) > 1 or not letra.isalpha():
                    letra = input("Debe se una letra: ")

                codigo_parcial += letra
                print("*"*10)
                print(f"Progreso del codigo {codigo_parcial}")
                print("*"*10)
                if(len(codigo_parcial) >= 8 and cerraduras_abiertas < 3 and tiempo > 0 and energia > 0):
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
                    print("Se abrio una ceradura.")
        #Descansar            
        elif(opcion == "3"):
            count_forzar = 0
            if alarma :
                energia += 5
                tiempo -= 1
            else:
                if(energia < 100 ):
                    tiempo -= 1
                    energia += 15    
                else:
                    tiempo -= 1
                    print("Energia al maximo.")   

    if(bloqueo_alarma):
        print("Se bloqueo la alarma, DERROTA")
    elif(energia <= 0 or tiempo <= 0):
        print("Te quedaste sin tiempo o energia, DERROTA")
    else:
        print("VICTORIA!!!")  
                               
    return

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador 
def arena():
    #Variables e inicializacion
    nombre_jugador = ""
    player1_vida = 100
    player2_vida = 100
    pociones_vida = 3
    player1_danio_base = 15
    player2_danio_base = 12
    turno_player1 = True
    player1_opcion = "0"

    #Pedir nombre del gladiador.
    print("================ BIENVENIDO A LA ARENA ====================")
    nombre_jugador = input("Ingrese el nombre del jugador: ")

    while not nombre_jugador.isalpha():
        print("Error: Solo se permiten letras")
        nombre_jugador = input("Ingrese nuevamente el nombre del jugador: ")

    print("========== INICIO DE COMBATE ==========")
    while player1_vida > 0 and player2_vida > 0:
        

        if(turno_player1):
            player1_opcion = input(f"""
                Tu vida restante: {player1_vida}
                Vida del enemigo: {player2_vida}
                Posicones restantes: {pociones_vida}
                ------------------------------------
                1. Ataque Pesado
                2. Ráfaga Veloz
                3. Curar
            """)

            #Validar opciones de entrada
            while not player1_opcion.isdigit() or int(player1_opcion) > 3 or int(player1_opcion) <= 0:
                player1_opcion = input("Error, Ingrese una opcion correcta: ")


            if(player1_opcion == "1"):
                
                if(player2_vida < 20):
                    player2_vida = int(player2_vida - (player1_danio_base*1.5))
                    print(f"Atacaste al enemigo por {player1_danio_base*1.5} puntos de daño!")
                else:
                    player2_vida = player2_vida - player1_danio_base
                    print(f"Atacaste al enemigo por {player1_danio_base} puntos de daño!")

            elif(player1_opcion == "2"):
                
                for i in range(3):
                    player2_vida -= 5
                    print("Golpe conectado por 5 de daño") 

            else:
                
                if(pociones_vida > 0 ):
                    pociones_vida -= 1
                    player1_vida += 30
                else:
                    print("No te quedan pociones de vida!")

            turno_player1 = not turno_player1
        else:
            player1_vida = player1_vida - player2_danio_base
            print("El enemigo te ataco por 12 puntos de daño!")
            turno_player1 = not turno_player1
            print("-"*80)
            print("         ------------ NUEVO TURNO ------------")


    #Evaluar victoria.
    if(player1_vida > 0):
        print(F"VICTORIA!! {nombre_jugador} a ganado la batalla.")   
    elif(player1_vida >= 0):
        print(f"Derrota!!. Has caido en combate.")            
                

    return  
arena()    