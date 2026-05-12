# Interfaz esperada por el cliente (Pagos en Soles)
class PagoSoles:
    def realizar_pago(self, monto):
        pass

# Clase existente (Legacy/Externa) que solo maneja Dólares
class ServicioPagoDolares:
    def procesar_transaccion(self, monto_usd):
        print(f"Procesando pago externo por ${monto_usd:.2f} USD")

# Adaptador que convierte la interfaz de Dólares a Soles
class AdaptadorPago(PagoSoles):
    def __init__(self, servicio_dolares, tipo_cambio):
        self.servicio_dolares = servicio_dolares
        self.tipo_cambio = tipo_cambio

    def realizar_pago(self, monto_soles):
        # Realiza la lógica de conversión
        monto_usd = monto_soles / self.tipo_cambio
        print(f"Adaptando pago de S/ {monto_soles:.2f} a USD...")
        self.servicio_dolares.procesar_transaccion(monto_usd)

# Ejecución del sistema
if __name__ == "__main__":
    # El servicio que ya tenemos
    servicio_externo = ServicioPagoDolares()
    
    # Creamos el adaptador con un tipo de cambio (ejemplo: 3.75)
    # Esto permite que el servicio externo "hable" en Soles
    pasarela_pagos = AdaptadorPago(servicio_externo, 3.75)
    
    # El cliente usa la interfaz en Soles sin preocuparse por la conversión interna
    pasarela_pagos.realizar_pago(100.00)