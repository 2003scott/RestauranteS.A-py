op=0
op1=0
op2=0
op3=0
suma=0

while op!=4:
    print("!","-"*30,"!")
    print("!"," "*7,"RESTAURANTE S.A"," "*6,"!")
    print("!"," "*12,"MENU"," "*12,"!")
    print("!","-"*30,"!")
    print("! 1 | Desayuno"," "*17,"!")
    print("! 2 | Almuerzo"," "*17,"!")
    print("! 3 | Cena"," "*21,"!")
    print("! 4 |","-"*8,"SALIR","-"*11,"!")
    op = int(input("Que Desear Tomar <1-4>: "))
    while op<1 or op>4:
        print("Error,  opcion no habilitada")
        op = int(input("Que Desear Tomar <1-4>: "))
    if op==1:
        while op1 != 8:
            print("!","-"*30,"!")
            print("!"," "*12,"DESAYUNO"," "*12,"!")
            print("!","-"*30,"!")
            print("! 1 | Cafe","            4.50"," "*4,"!")
            print("! 2 | Chocolate","       5.00"," "*4,"!")
            print("! 3 | Jugo de Fresa","   9.00"," "*4,"!")
            print("! 4 | Jugo de Papaya","  8.00"," "*4,"!")
            print("! 5 | Pan con Pollo","   7.00"," "*4,"!")
            print("! 6 | Pan con Jamon","   7.00"," "*4,"!")
            print("! 7 | Pan con Totilla"," 7.00"," "*4,"!")
            print("! 8 |","-"*8,"SALIR","-"*11,"!")
            op1=int(input("Elija una Opcion <1-8> :"))
            while op1<1 or op1>8:
                print("Error,  opcion no habilitada")
                op1=int(input("Elija una Opcion <1-8> :"))
            if op1==1:
                Cafe= 4.50
                suma += Cafe
                print("Cafe agregado")
            elif op1==2:
                Chocolate = 5.00
                suma +=Chocolate
                print("Chocolate Compera agreado al carito")
            elif op1==3:
                Jugo_de_Fresa =9.00
                suma += Jugo_de_Fresa
                print("Jugo de Fresa agreado al carito")
            elif op1==4:
                Jugo_de_Papaya =8.00
                suma += Jugo_de_Papaya
                print("Jugo de Papaya agreado al carito")
            elif op1==5:
                Pan_con_Pollo =7.00
                suma += Pan_con_Pollo
                print("Pan con Pollo agreado al carito")
            elif op1==6:
                Pan_con_Jamon =7.00
                suma += Pan_con_Jamon
                print("Pan con Jamon agreado al carito")
            elif op1==7:
                Pan_con_Totilla =7.00
                suma += Pan_con_Totilla
                print("Pan con Totilla agreado al carito")
            else:
                print("<-")
                break
    elif op==2:
        while op2 != 8:
            print("!","-"*30,"!")
            print("!"," "*12,"ALMUERZO"," "*12,"!")
            print("!","-"*30,"!")
            print("!","-"*30,"!")
            print("! 1 | Cafe","            4.50"," "*4,"!")
            print("! 2 | Chocolate","       5.00"," "*4,"!")
            print("! 3 | Jugo de Fresa","   9.00"," "*4,"!")
            print("! 4 | Jugo de Papaya","  8.00"," "*4,"!")
            print("! 5 | Pan con Pollo","   7.00"," "*4,"!")
            print("! 6 | Pan con Jamon","   7.00"," "*4,"!")
            print("! 7 | Pan con Totilla"," 7.00"," "*4,"!")
            print("! 8 |","-"*8,"SALIR","-"*11,"!")
            op2=int(input("Elija una Opcion <1-8> :"))
            while op2<1 or op2>8:
                print("Error,  opcion no habilitada")
                op2=int(input("Elija una Opcion <1-8> :"))
            if op2==1:
                Cafe= 4.50
                suma += Cafe
                print("Cafe agregado")
            elif op2==2:
                Chocolate = 5.00
                suma +=Chocolate
                print("Chocolate Compera agreado al carito")
            elif op2==3:
                Jugo_de_Fresa =9.00
                suma += Jugo_de_Fresa
                print("Jugo de Fresa agreado al carito")
            elif op2==4:
                Jugo_de_Papaya =8.00
                suma += Jugo_de_Papaya
                print("Jugo de Papaya agreado al carito")
            elif op2==5:
                Pan_con_Pollo =7.00
                suma += Pan_con_Pollo
                print("Pan con Pollo agreado al carito")
            elif op2==6:
                Pan_con_Jamon =7.00
                suma += Pan_con_Jamon
                print("Pan con Jamon agreado al carito")
            elif op2==7:
                Pan_con_Totilla =7.00
                suma += Pan_con_Totilla
                print("Pan con Totilla agreado al carito")
            else:
                print("<-")
                break
    elif op==3:
        while op3 !=7:
            print("!","-"*30,"!")
            print("!"," "*12,"CENA"," "*12,"!")
            print("!","-"*30,"!")
            print("! 1 | Pizza Expres","    9.50"," "*4,"!")
            print("! 2 | Ensalada Compera","7.50"," "*4,"!")
            print("! 3 | Garpacho","        6.00"," "*4,"!")
            print("! 4 | Caldo de Gallina","6.00"," "*4,"!")
            print("! 5 | Pollo al Horno","  5.50"," "*4,"!")
            print("! 6 | Menestron","       4.00"," "*4,"!")
            print("! 7 |","-"*8,"SALIR","-"*11,"!")
            print("!","-"*30,"!")
            op3=int(input("Elija una Opcion <1-7> :"))
            while op3<1 or op3>7:
                print("Error,  opcion no habilitada")
                op3=int(input("Elija una Opcion <1-7> :"))
            if op3==1:
                Pizza_Expres= 9.50
                suma += Pizza_Expres
                print("Pizza Expres agregado")
            elif op3==2:
                Ensalada_Compera = 7.50
                suma +=Ensalada_Compera
                print("Ensalada Compera agreado al carito")
            elif op3==3:
                Garpacho =6.00
                suma += Garpacho
                print("Garpacho agreado al carito")
            elif op3==4:
                Caldo_de_Gallina =6.00
                suma += Caldo_de_Gallina
                print("Caldo de Gallinaa agreado al carito")
            elif op3==5:
                Pollo_al_Horno =5.50
                suma += Pollo_al_Horno
                print("Pollo al Horno agreado al carito")
            elif op3==6:
                Menestron =4.00
                suma += Menestron
                print("Menestron agreado al carito")
            else:
                print("<-")
                break
    elif op==4:
        if suma >= 1 :
            print("Gracias por su preferencia le desea buen dia ‘RESTAURANTE S.A’")
            print("!","-"*30,"!")
            print("Subtotal :      ",suma)
            igv = suma * 0.18
            print("Igv :           ",igv)
            total = suma + igv
            print("Total a Pagar : ",total)
            print("Gracias por tu compra")
            print("!","-"*30,"!")
        else :
            print("Gracias por su preferencia le desea buen dia ‘RESTAURANTE S.A’")
print("2003scott")

