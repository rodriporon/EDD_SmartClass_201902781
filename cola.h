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
        cout << "[Error de tipo: " << error->tipo << " Descripción: " << error->descripcion << "]" << endl;
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
        cout << "El error con id: "<< id << " ha sido desencolado" << endl;
    }
    else
    {

        cout << "La cola está vacía" << endl;
    }
}
