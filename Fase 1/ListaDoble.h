#include <iostream>
#include "Nodo.h"
using namespace std;

class ListaD
{
protected:
    Nodo* primero;
    Nodo* ultimo;
public:
    ListaD(){
        primero = NULL;
        ultimo = NULL;
    }
    void insert(int index, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);
    void getList();
    void showL();

};

void ListaD::insert(int index, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
{
    Nodo* nuevo = new Nodo(index, carnet, nombre, descripcion, materia, fecha, estado);

    if (primero == NULL)
    {
        primero = nuevo;
        primero->setSiguiente(NULL);
        primero->setAtras(NULL);
        ultimo = primero;
        cout << nuevo->getCarnet() << endl;
    } else
    {
        ultimo->setSiguiente(nuevo);
        nuevo->setSiguiente(NULL);
        nuevo->setAtras(ultimo);
        ultimo = nuevo;
        cout << nuevo->getCarnet() << endl;
    }

}

void ListaD::getList()
{
    Nodo *actual;
    actual = primero;
    
    if (primero != NULL)
    {
        
        while (actual != NULL)
        {
            cout << "[" << actual->getCarnet() <<  "]" << endl;
            actual = actual->getSiguiente();
        }
        
    } else {
        cout << "Empty List" << endl;
    }
    
} 

