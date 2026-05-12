def validar_numeros(func):
    """Decorator que valida que los argumentos sean numéricos y no nulos."""
    def envoltura(*args, **kwargs):
        # Validación: Verificar que todos los argumentos sean int o float
        for arg in args:
            if not isinstance(arg, (int, float)):
                return f"Error en '{func.__name__}': El argumento {arg} no es un número."
        
        # Validación específica para división: evitar divisor cero
        if func.__name__ == "dividir" and args[1] == 0:
            return "Error: División por cero no permitida."
            
        return func(*args, **kwargs)
    return envoltura

@validar_numeros
def sumar(a, b):
    return a + b

@validar_numeros
def dividir(a, b):
    return a / b

# Pruebas de la implementación
if __name__ == "__main__":
    print(f"Suma válida: {sumar(10, 5)}")
    print(f"Suma inválida: {sumar(10, 'cinco')}")
    
    print(f"División válida: {dividir(20, 4)}")
    print(f"División por cero: {dividir(20, 0)}")