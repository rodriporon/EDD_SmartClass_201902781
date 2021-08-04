#include <iostream>
#include "Nodo.h"
#include "Lista.h"

int main() {
    int d;
    Lista lista;

    cout << "Elementos de la lista, termina con -1" << endl;

    do {
        cin >> d;
        lista.insert(d);
    } while (d != -1);

    cout << "Elementos de la lista" <<endl;
    lista.getList();

    
    return 0;
}