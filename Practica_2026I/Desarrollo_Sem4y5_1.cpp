#include <iostream>

using namespace std;

class Config {
private:
    // Puntero estático que almacenará la instancia única 
    static Config* instance;

    // Constructor privado para evitar instanciación externa 
    Config() {
        cout << "Configuracion: Cargando recursos por unica vez..." << endl;
    }

public:
    // Método estático para obtener la instancia [cite: 21]
    static Config* getInstance() {
        if (instance == nullptr) {
            instance = new Config(); // Lazy initialization [cite: 23]
        }
        return instance;
    }

    void showMessage() {
        cout << "Accediendo a la configuracion global." << endl;
    }

    // Evitar que se pueda copiar la instancia
    Config(const Config&) = delete;
    void operator=(const Config&) = delete;
};

// Inicialización del puntero estático [cite: 27]
Config* Config::instance = nullptr;

int main() {
    // Intentamos obtener la instancia dos veces [cite: 30, 32]
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();

    obj1->showMessage();
    obj2->showMessage();

    // Verificamos si ambas variables apuntan a la misma dirección de memoria [cite: 36]
    cout << "Son la misma instancia? " << (obj1 == obj2 ? "Si" : "No") << endl;
    cout << "Direccion obj1: " << obj1 << endl;
    cout << "Direccion obj2: " << obj2 << endl;

    return 0;
}