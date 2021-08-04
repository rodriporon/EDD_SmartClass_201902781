#include <iostream>
#include "Nodo.h"

using namespace std;

class Lista
{
protected:
    Node *first;

public:
    Lista()
    {
        first = NULL;
    }

    bool isEmpty();
    void insertListHeader(int value);
    void insert(int value);
    void getList();
};

bool Lista::isEmpty()
{
    return first == NULL;
}

void Lista::insertListHeader(int value)
{
    Node *newNode;
    newNode = new Node(value);
    newNode->setNext(first);
    first = newNode;
}

void Lista::insert(int value)
{
    Node *newNode;
    newNode = new Node(value);

    if (isEmpty())
    {
        first = newNode;
    }
    else
    {
        Node *aux;
        aux = first;
        while (first->getNext() != NULL)
        {
            first = first->getNext();
        }
        first->setNext(newNode);
        first = aux;
    }
}

void Lista::getList()
{
    Node *aux;
    aux = first;
    while (aux != NULL)
    {
        cout << aux->getValue() << endl;
        aux = aux->getNext();
    }
}