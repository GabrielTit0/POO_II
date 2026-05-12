class ComboFastFood:
    def __init__(self):
        self.hamburguesa = None
        self.bebida = None
        self.papas = None

    def __str__(self):
        return f"Combo: [Hamburguesa: {self.hamburguesa}, Bebida: {self.bebida}, Papas: {self.papas}]"

class ComboBuilder:
    def __init__(self):
        self.combo = ComboFastFood()

    def add_hamburguesa(self, tipo):
        self.combo.hamburguesa = tipo
        return self

    def add_bebida(self, tipo):
        self.combo.bebida = tipo
        return self

    def add_papas(self, tamaño):
        self.combo.papas = tamaño
        return self

    def build(self):
        return self.combo

# Uso del Builder para crear diferentes combos
if __name__ == "__main__":
    # Creamos un combo personalizado paso a paso
    combo_personalizado = (ComboBuilder()
                           .add_hamburguesa("Doble Carne con Queso")
                           .add_bebida("Coca-Cola Grande")
                           .add_papas("Grandes")
                           .build())

    # Creamos un combo más sencillo
    combo_simple = (ComboBuilder()
                    .add_hamburguesa("Pollo Crispy")
                    .add_bebida("Agua Mineral")
                    .build())

    print(combo_personalizado)
    print(combo_simple)