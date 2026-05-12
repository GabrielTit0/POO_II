from abc import ABC, abstractmethod

# 1. Definición de la Interfaz (Contrato para los Observadores)
class IUsuario(ABC):
    @abstractmethod
    def recibir_notificacion(self, emisor, mensaje):
        pass

    @property
    @abstractmethod
    def nombre(self):
        pass

# 2. Implementación de la Clase Concreta (El Observador)
class UsuarioChat(IUsuario):
    def __init__(self, nombre_usuario):
        self._nombre = nombre_usuario

    @property
    def nombre(self):
        return self._nombre

    def recibir_notificacion(self, emisor, mensaje):
        # Este método se ejecuta cuando el Sujeto notifica un cambio
        print(f" > [{self._nombre}] Mensaje de {emisor}: {mensaje}")

# 3. Clase Sujeto (La Sala de Chat que gestiona a los observadores)
class SalaChat:
    def __init__(self, nombre_sala):
        self.nombre_sala = nombre_sala
        self._usuarios = []

    def suscribir(self, usuario):
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)
            print(f"SISTEMA: {usuario.nombre} se ha unido a {self.nombre_sala}.")

    def desuscribir(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            print(f"SISTEMA: {usuario.nombre} ha salido de la sala.")

    def difundir(self, emisor_obj, mensaje):
        print(f"\n--- Canal: {self.nombre_sala} ---")
        for usuario in self._usuarios:
            # Condición para no enviarse el mensaje a uno mismo
            if usuario != emisor_obj:
                usuario.recibir_notificacion(emisor_obj.nombre, mensaje)

# 4. Bloque de Ejecución (Aquí se definen y usan las variables)
if __name__ == "__main__":
    # Primero definimos el sujeto
    sala_sistemas = SalaChat("Sistemas UNAP")
    
    # Segundo: Creamos e inicializamos las instancias de los usuarios
    # Esto evita el error de "indefinido"
    user_gabo = UsuarioChat("Gabriel")
    user_aldo = UsuarioChat("Aldo")
    user_maria = UsuarioChat("Maria")

    # Tercero: Los registramos en la sala
    sala_sistemas.suscribir(user_gabo)
    sala_sistemas.suscribir(user_aldo)
    sala_sistemas.suscribir(user_maria)

    # Cuarto: Enviamos mensajes usando las instancias creadas
    sala_sistemas.difundir(user_aldo, "No olviden enviar su práctica de POO.")
    sala_sistemas.difundir(user_gabo, "Recibido. ¿La entrega es por GitHub?")
    
    # Quinto: Probamos la desuscripción
    sala_sistemas.desuscribir(user_maria)
    sala_sistemas.difundir(user_aldo, "Maria salió, continuamos con la sesión.")