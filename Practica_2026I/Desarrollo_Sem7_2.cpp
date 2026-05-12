#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Interfaz Estrategia
class EstrategiaOrdenamiento {
public:
    virtual void ordenar(vector<int>& datos) = 0;
    virtual ~EstrategiaOrdenamiento() {}
};

// Estrategia Concreta: Ordenamiento Burbuja
class OrdenamientoBurbuja : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        int n = datos.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (datos[j] > datos[j + 1]) {
                    swap(datos[j], datos[j + 1]);
                }
            }
        }
        cout << "Ordenado usando: Burbuja" << endl;
    }
};

// Estrategia Concreta: Quicksort (usando la función estándar de C++)
class OrdenamientoQuickSort : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        sort(datos.begin(), datos.end()); // Implementación eficiente de C++
        cout << "Ordenado usando: QuickSort" << endl;
    }
};

// Contexto: El objeto que usa las estrategias
class ListaDeDatos {
private:
    vector<int> datos;
    EstrategiaOrdenamiento* estrategia;

public:
    ListaDeDatos(const vector<int>& d) : datos(d), estrategia(nullptr) {}

    void setEstrategia(EstrategiaOrdenamiento* e) {
        estrategia = e;
    }

    void procesar() {
        if (estrategia) {
            estrategia->ordenar(datos);
            for (int x : datos) cout << x << " ";
            cout << endl;
        } else {
            cout << "Error: No se ha definido una estrategia." << endl;
        }
    }
};

int main() {
    vector<int> misDatos = {5, 2, 9, 1, 5, 6};

    ListaDeDatos lista(misDatos);
    OrdenamientoBurbuja burbuja;
    OrdenamientoQuickSort quick;

    // Usar Burbuja
    lista.setEstrategia(&burbuja);
    lista.procesar();

    // Cambiar dinámicamente a QuickSort
    lista.setEstrategia(&quick);
    lista.procesar();

    return 0;
}