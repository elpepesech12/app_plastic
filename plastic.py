import os
import time
op_menu=""
tipo_producto=""
producto=""
cantidad=0
precio=0
tipo_cliente=""
cliente=""
subtotal=0
total=0
efectivo=""
descuento=0
mensaje=""

total_recaudado=0
total_productos_vendidos=0
total_productos_vendidos_tazas=0
total_productos_vendidos_llaveros=0
total_productos_vendidos_poleras=0

while True:
    os.system("cls")
    op_menu=str(input('''
    1.- Venta productos
    2.- Ver estadisticas
    3.- Salir de la app
    \nSeleccione una opcion:                  
                      '''))
    
    if op_menu=="1":
        os.system("cls")
        tipo_producto=str(input('''
        |    Producto  | Valor   | Valor |
        |              | General | Socio |
        |--------------|---------|-------|
        |1.- Tazón     | $800    | $500  |
        |2.- Llavero   | $500    | $300  |
        |3.- Polera    | $5.000  | $3.000|
        |    Estampada |---------|-------|
        |--------------|
        \nSeleccione el tipo de producto que desea:                                 
                                '''))
        
        cantidad=int(input("Que cantidad llevará?"))
        total_productos_vendidos=total_productos_vendidos+cantidad
        if tipo_producto=="1":
            total_productos_vendidos_tazas=total_productos_vendidos_tazas+cantidad
            producto="Tazón"
            print(f"Usted selecciono {producto}")
            tipo_cliente=str(input("¿Es socio? S/N")).upper()
            if tipo_cliente=="S":
                precio=500
                cliente="Socio"
            else:
                precio=800
                cliente="General"
                
        if tipo_producto=="2":
            total_productos_vendidos_llaveros=total_productos_vendidos_llaveros+cantidad
            producto="Lavero"
            print(f"Usted selecciono {producto}")
            tipo_cliente=str(input("¿Es socio? S/N")).upper()
            if tipo_cliente=="S":
                precio=300
                cliente="Socio"
            else:
                precio=500
                cliente="General"
                
        if tipo_producto=="3":
            total_productos_vendidos_poleras=total_productos_vendidos_poleras+cantidad
            producto="Polera estampada"
            print(f"Usted selecciono {producto}")
            tipo_cliente=str(input("¿Es socio? S/N")).upper()
            if tipo_cliente=="S":
                precio=3000
                cliente="Socio"
            else:
                precio=5000
                cliente="General"
        
        subtotal=precio*cantidad
        total=precio*cantidad
        os.system("cls")
        efectivo=str(input("Cancela en efectivo S/N")).upper()
        if efectivo=="S":
            descuento=subtotal*0.20
            total=total-descuento
            mensaje="Pago en efectivo 20%"
        else:
            mensaje="no se aplicó descuento"
            descuento=0
            total=total
            
        os.system("cls")
        
        print(f'''
        Producto: {producto} 
        Cantidad solicitada: {cantidad} | Tipo cliente: {cliente} 
        Subtotal: {subtotal}
        Descuento: {mensaje} ${descuento}
        Total a pagar: ${total}    
              ''')
        total_recaudado=total_recaudado+total
        os.system("pause")
        
    if op_menu=="2":
        os.system("cls")
        print(f'''
        ======= Estadisticas =====
        Total Productos vendidos: {total_productos_vendidos}
         - Total Tazas Vendidas: {total_productos_vendidos_tazas}
         - Total Llaveros vendidos: {total_productos_vendidos_llaveros}
         - Total Poleras vendidas: {total_productos_vendidos_poleras}
        Total recaudado: {total_recaudado}    
              ''')
        os.system("pause")
         
    if op_menu=="3":
        os.system("cls")
        salir=str(input("Seguro que deseas salir? S/N:")).upper()
        if salir=="S":
            print("Saliendo de la app....")
            time.sleep(2)
            break
        else:
            print("Volviendo a la app")
            op_menu="0"
            time.sleep(2)
            
            
        
            
            
        
        
        
                
    
                
    
                
    