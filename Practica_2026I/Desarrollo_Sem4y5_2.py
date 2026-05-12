from abc import ABC, abstractmethod

# Interfaz común para todos los transportes
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Clases concretas que implementan la interfaz
class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera en un camión."

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar en un contenedor."

class Avion(Transporte):
    def entregar(self):
        return "Entrega por aire mediante carga aérea."

# Clase Factory que centraliza la creación
class Factory:
    @staticmethod
    def get_transporte(tipo):
        tipo = tipo.lower()
        if tipo == "camion":
            return Camion()
        elif tipo == "barco":
            return Barco()
        elif tipo == "avion":
            return Avion()
        else:
            raise ValueError(f"El tipo de transporte '{tipo}' no está disponible.")

# Prueba de la implementación
if __name__ == "__main__":
    # El cliente solo interactúa con la Factory
    medios = ["camion", "barco", "avion"]
    
    for medio in medios:
        t = Factory.get_transporte(medio)
        print(f"Pedido: {t.entregar()}")