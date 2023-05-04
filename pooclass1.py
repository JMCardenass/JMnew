class Motos:
    def __init__(self,color,cilindraje,categoria):
        self.color=color
        self.cilindraje=cilindraje
        self.categoria=categoria
        self.is_running=False
    def start_engine(self):
        self.is_running = True
        print("Vehiculo encendido")

    def stop_engine(self):
        self.is_running = False
        print("Vehiculo apagado")

    def change_color(self,new_color):
        self.color = new_color
        print("El color del vehiculo ha sido modificado a", {new_color})

vehiculo1=Motos("rojo","150","deportiva")
print("vehiculo1.color, vehiculo1.cilindraje, vehiculo1.categoria")
vehiculo1.start_engine()
vehiculo1.change_color("azul")
vehiculo1.stop_engine()