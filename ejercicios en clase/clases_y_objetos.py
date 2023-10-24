class Motorcicle:
    is_new = True
    
    def __init__(self, color, patent, tank_capacity, wheel_number, brand, model, fab_date, top_speed, wheight):
        self.color = color
        self.patent = patent
        self.tank_capacity = tank_capacity
        self.wheel_number = wheel_number
        self.brand = brand
        self.model = model
        self.fab_date = fab_date
        self.top_speed = top_speed
        self.wheight = wheight
        self.engine = False
        self.price = None
    def start_engine (self):
        if self.engine:
            print("El motor ya estaba en marcha")
        else:
            self.engine = True
            print("El motor estaba apagado, encendiendo")
    def stop_engine (self):
        if self.engine:
            self.engine == False
            print("Deteniendo el motor")
        else:
            print("El motor ya estaba detenido")
    def price_check (self):
        return self.price

        #MAIN
option = 0
moto1 = Motorcicle("Rojo", "ACG176", 10, 2, "KTM", "Duke", 2022, 180, 30)
valor_moto1 = 17500
moto2 = Motorcicle("Azul", "GAW195", 10, 2, "BENELLI", "TRK 502", 2023, 210, 55)


while option != 1 and option != 2:
    option = int(input("Ingrese porque moto desea consultar: (1) KTM | (2) BENELLI: "))
#Moto 1
if option == 1:
    engine_op = 0
    print(f"Ficha tecnica de la motocicleta {moto1.brand}")
    print(f"Marca: {moto1.brand} | Modelo: {moto1.model} | Año de Fabricacion: {moto1.fab_date} | Color: {moto1.color} | Velocidad punta: {moto1.top_speed} | Peso: {moto1.wheight} | Capacidad del tanque de nafta: {moto1.tank_capacity} | Tamaño de las ruedas: {moto1.wheel_number} | Patente: {moto1.patent} | Es nueva: {Motorcicle.is_new}")
    while engine_op != 1 and engine_op != 2:
        engine_op = int(input("Desea arrancar o detener el motor? (1) ARRANCAR | (2) DETENER "))
    if engine_op == 1:
        moto1.start_engine()
    elif engine_op == 2:
        moto1.stop_engine()
#Moto 2
elif option == 2:
    engine_op = 0
    print(f"Ficha tecnica de la motocicleta {moto2.brand}")
    print(f"Marca: {moto2.brand} | Modelo: {moto2.model} | Año de Fabricacion: {moto2.fab_date} | Color: {moto2.color} | Velocidad punta: {moto2.top_speed} | Peso: {moto2.wheight} | Capacidad del tanque de nafta: {moto2.tank_capacity} | Tamaño de las ruedas: {moto2.wheel_number} | Patente: {moto2.patent} | Es nueva: {Motorcicle.is_new}")
    while engine_op != 1 and engine_op != 2:
        engine_op = int(input("Desea arrancar o detener el motor? (1) ARRANCAR | (2) DETENER "))
    if engine_op == 1:
        moto1.start_engine()
    elif engine_op == 2:
        moto1.stop_engine()

#Precio
price_op = int(input("De que moto desea saber el precio: KTM (1) | BENELLI (2): "))

if price_op == 1:
    moto1.price = valor_moto1
    print(f"El valor de la {moto1.brand} {moto1.model} es de ${moto1.price_check()}")
elif price_op == 2:
    print(f"El valor de la {moto2.brand} {moto2.model} es de ${moto2.price_check()}")
