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
    void insert(int value);
    void getList();
};

bool ListaDoble::isEmpty()
{
    return first == NULL;
}

void ListaDoble::insert(int value)
{
    NodoDoble *newNode = new NodoDoble(value);

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
            cout <<"["<<aux->getValue()<<"] ";
            aux = aux->siguienteNodo();
        } while (aux != first);
        
    }
    else
    {
        cout << "List Empty";
    }
}