from abc import ABC, abstractmethod

# 1. Interfaz Command
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass

# 2. El Receptor (La clase que realmente hace el trabajo)
class Documento:
    def __init__(self):
        self.contenido = ""

    def escribir(self, texto):
        self.contenido += texto

    def borrar_ultimo(self, texto):
        # Elimina el texto que se agregó por última vez
        if self.contenido.endswith(texto):
            self.contenido = self.contenido[:-len(texto)]

    def __str__(self):
        return f"Contenido actual: '{self.contenido}'"

# 3. Comando Concreto para Escribir
class EscribirComando(Comando):
    def __init__(self, documento, texto):
        self.documento = documento
        self.texto = texto

    def ejecutar(self):
        self.documento.escribir(self.texto)

    def deshacer(self):
        self.documento.borrar_ultimo(self.texto)

# 4. El Invocador (Gestiona el historial)
class Editor:
    def __init__(self):
        self.historial = []

    def ejecutar_comando(self, comando):
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer_ultimo(self):
        if self.historial:
            comando = self.historial.pop()
            comando.deshacer()
        else:
            print("Nada que deshacer.")

# --- Prueba del Editor ---
if __name__ == "__main__":
    mi_doc = Documento()
    mi_editor = Editor()

    # Realizamos algunas acciones
    cmd1 = EscribirComando(mi_doc, "Hola ")
    cmd2 = EscribirComando(mi_doc, "Gabriel. ")
    cmd3 = EscribirComando(mi_doc, "Aprendiendo Patrones.")

    mi_editor.ejecutar_comando(cmd1)
    mi_editor.ejecutar_comando(cmd2)
    mi_editor.ejecutar_comando(cmd3)
    
    print(mi_doc)

    # Probamos el Deshacer (Undo)
    print("\n--- Deshaciendo última acción ---")
    mi_editor.deshacer_ultimo()
    print(mi_doc)

    print("\n--- Deshaciendo otra acción ---")
    mi_editor.deshacer_ultimo()
    print(mi_doc)