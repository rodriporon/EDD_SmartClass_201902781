#include <iostream>
#include "NodoDoble.h"

using namespace std;

class ListaDoble
{
protected:
    NodoDoble *first;
    NodoDoble *last;

public:
    ListaDoble()
    {
        first = NULL;
        last = NULL;
    }

    bool isEmpty();
    void insert(int carnet, long long int DPI, string nombre, string carrera, string password, int creditos, int edad);
    NodoDoble* getNode();
    void getList();
    
};

bool ListaDoble::isEmpty()
{
    return first == NULL;
}

NodoDoble* ListaDoble::getNode()
{
    return NULL;
}

void ListaDoble::insert(int carnet, long long int DPI, string nombre, string carrera, string password, int creditos, int edad)
{
    NodoDoble *newNode = new NodoDoble(carnet, DPI, nombre, carrera, password, creditos, edad);

    if (isEmpty())
    {
        first = newNode;
        first->setSiguiente(first);
        first->setAnterior(first);
        last = first;
    }
    else
    {
        last->setSiguiente(newNode);
        newNode->setSiguiente(first);  
        newNode->setAnterior(last);
        last = newNode;
        first->setAnterior(last);
    }
}

void ListaDoble::getList()
{
    NodoDoble* aux;
    aux = first;
    
    if (first != NULL)
    {
        do
        {
            cout <<"["<< "Nombre: " << aux->getCarnet() << " Carrera: " << aux->getCarrera() << "] ";
            aux = aux->siguienteNodo();
        } while (aux != first);
        
    }
    else
    {
        cout << "Empty List";
    }
}