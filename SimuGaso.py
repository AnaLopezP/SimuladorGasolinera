import random
from threading import *
# Llegan coches cada T min máx (T es 15 min)
# N surtidores de combustible (N es 1)
# Bajar y llenar el depósito entre 5 y 10 min
# 1 caja. Tres minutos para pagar
# Cada coche es un hilo. Habrán 50 coches
# Calcular tiempo medio desde que un coche entra hasta que sale
  

'''
Necesitamos una cola
Clase cliente
Clase gasolinera
'''

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)
    
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
        
    def esta_vacia(self):
        return self.items == []

class Cliente(Thread):
    def __init__(self, id, estado):
        self.estado = None
        self.id = id
        self.tiempo_llenar = random.randint(5, 10)
        self.tiempo_llegada = random.randint(0, 15)
        self.tiempo_cola = 3

    def llegar(self):
        pass

    def llenar(self):
        pass

    def pagar(self):
        pass