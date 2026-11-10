import tkinter as tk

# clase Usuario

class Usuario:
    def __init__(self):
        self.usuario_ingresado = "Software FJ"
        password_ingresada = "123456"

    def validar(self, usuario_ingresado, password_ingresada):
        return usuario_ingresado == self.usuario_ingresado and password_ingresada == self.password_ingresada
        
class Integral__gestion__clientes:
    def __init__(self, reservas_de_sala, alquiler_de_equipos, asesorias_especializadas):
        self.reservas_de_sala = reservas_de_sala
        self.alquiler_de_equipos = alquiler_de_equipos
        self.asesorias_especializadas = asesorias_especializadas

def main():
    reservas_de_sala = input("Ingrese las reservas de sala: ")
    alquiler_de_equipos = input("Ingrese el alquiler de equipos: ")
    asesorias_especializadas = input("Ingrese las asesorías especializadas: ")

    integral_gestion_clientes = Integral__gestion__clientes(reservas_de_sala, alquiler_de_equipos, asesorias_especializadas)

    print("Reservas de sala:", integral_gestion_clientes.reservas_de_sala)
    print("Alquiler de equipos:", integral_gestion_clientes.alquiler_de_equipos)
    print("Asesorías especializadas:", integral_gestion_clientes.asesorias_especializadas)

main()
