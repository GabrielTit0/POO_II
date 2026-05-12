#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Clase Base (Componente)
class Componente {
public:
    virtual void mostrar(int profundidad = 0) = 0;
    virtual ~Componente() {}
};

// Objeto Simple (Leaf): Archivo
class Archivo : public Componente {
private:
    string nombre;
public:
    Archivo(string n) : nombre(n) {}
    void mostrar(int profundidad = 0) override {
        for (int i = 0; i < profundidad; ++i) cout << "  ";
        cout << "- Archivo: " << nombre << endl;
    }
};

// Objeto Compuesto (Composite): Carpeta
class Carpeta : public Componente {
private:
    string nombre;
    vector<Componente*> hijos;
public:
    Carpeta(string n) : nombre(n) {}
    
    void agregar(Componente* c) {
        hijos.push_back(c);
    }

    void mostrar(int profundidad = 0) override {
        for (int i = 0; i < profundidad; ++i) cout << "  ";
        cout << "+ Carpeta: " << nombre << endl;
        for (auto h : hijos) {
            h->mostrar(profundidad + 1);
        }
    }

    ~Carpeta() {
        for (auto h : hijos) delete h;
    }
};

int main() {
    // Creamos la estructura
    Carpeta* raiz = new Carpeta("C:");
    Carpeta* documentos = new Carpeta("Mis Documentos");
    
    raiz->agregar(new Archivo("config.sys"));
    documentos->agregar(new Archivo("Tarea_POO.cpp"));
    documentos->agregar(new Archivo("Notas.txt"));
    
    Carpeta* imagenes = new Carpeta("Fotos_Puno");
    imagenes->agregar(new Archivo("LagoTiticaca.png"));
    
    // Anidamos carpetas
    documentos->agregar(imagenes);
    raiz->agregar(documentos);

    // Mostramos toda la estructura de forma uniforme
    cout << "Estructura de archivos:" << endl;
    raiz->mostrar();

    delete raiz; // El destructor se encarga de limpiar la memoria recursivamente
    return 0;
}