#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

class Cola
{
private:
    class Nodo
    {
    public:
        int id;
        string tipo;
        string descripcion;
        Nodo *siguiente;
    };

    Nodo *primero;
    Nodo *ultimo;

public:
    Cola();
    void encolar(int id, string nombre, string edad);
    void mostrar();
    void crearDOT();
    void desencolar();
    string crearNodos(Nodo *base);
    string recorrer(Nodo *primero);
    void graficar();
    bool vacia();
};

Cola::Cola()
{
    primero = NULL;
    ultimo = NULL;
}

void Cola::encolar(int id, string tipo, string descripcion)
{
    Nodo *newNodo;
    newNodo = new Nodo();
    newNodo->tipo = tipo;
    newNodo->descripcion = descripcion;
    newNodo->id = id;

    newNodo->siguiente = NULL;
    if (primero == NULL)
    {
        primero = newNodo;
        ultimo = newNodo;
    }
    else
    {
        ultimo->siguiente = newNodo;
        ultimo = newNodo;
    }
}

void Cola::mostrar()
{
    Nodo *error = primero;
    while (error != NULL)
    {
        cout << "[Id: " << error->id << " -Error de tipo: " << error->tipo << " -Descripción: " << error->descripcion << "]" << endl;
        error = error->siguiente;
    }
}

void Cola::desencolar()
{
    if (primero != NULL)
    {
        int id = primero->id;
        Nodo *eliminar = primero;
        if (primero == ultimo)
        {
            primero = NULL;
            ultimo = NULL;
        }
        else
        {
            primero = primero->siguiente;
        }

        delete eliminar;
        cout << "El error con id: " << id << " ha sido desencolado" << endl;
    }
    else
    {

        cout << "La cola está vacía" << endl;
    }
}

string Cola::recorrer(Nodo* primero)
{
    string grafo = "";
    if (primero != NULL)
    {
        if (primero->siguiente != NULL)
        {
            grafo += "\tNodo" + to_string(primero->id) + "->" + "Nodo" + to_string(primero->siguiente->id) + "; \n";
        }
        grafo += "\n \tNodo" + to_string(primero->id) + "[shape=box, style=filled, color=skyblue, label= \"-Id: " + to_string(primero->id) + "\n" + "-Tipo: " + primero->tipo + "\n" + "-Descripcion: " + primero->descripcion + "\"] \n";
        grafo += recorrer(primero->siguiente);
        
    }
    return grafo;
}

bool Cola::vacia()
{
    if (primero == NULL)
    {
        return true;
    }
    return false;
    
}

void Cola::graficar()
{
    string grafica = "";
    ofstream archivo;
    archivo.open("Reportes\\Cola.dot");
    archivo << "digraph {\n rankdir=TB;\n";
    grafica = recorrer(primero);
    archivo << grafica;
    archivo << "}\n";
    archivo.close();

    system("dot -Tpng Reportes\\Cola.dot -o Reportes\\Cola.png -Gcharset=latin1");
    system("Reportes\\Cola.png");
}