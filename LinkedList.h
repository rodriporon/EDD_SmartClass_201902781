#include <iostream>
#include "Node.h"
using namespace std;

class LinkedList
{
protected:
    Node *primero;
    Node *ultimo;

public:
    LinkedList()
    {
        primero = NULL;
        ultimo = NULL;
    }
    void insert(int index, int id, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);
    void getListF();
};

void LinkedList::insert(int index, int id, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
{
    Node *nuevo = new Node(index, carnet, nombre, descripcion, materia, fecha, estado);

    if (primero == NULL)
    {
        primero = nuevo;
        primero->setSiguiente(NULL);
        primero->setAtras(NULL);
        ultimo = primero;
    }
    else
    {
        ultimo->setSiguiente(nuevo);
        nuevo->setSiguiente(NULL);
        nuevo->setAtras(ultimo);
        ultimo = nuevo;
    }
}

void LinkedList::getListF()
{
    Node *actual = primero;
    if (primero != NULL)
    {
        while (actual != NULL)
        {
            cout << "[" << actual->getCarnet() << "]" << endl;
            actual = actual->getSiguiente();
        }
    }
    else
    {
        cout << "Empty List" << endl;
    }
}