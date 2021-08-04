#include <iostream>
#include "ListaDoble.h"

using namespace std;

int main(){

    int d;
    ListaDoble lista;

    lista.insert(1);
    lista.insert(2);
    lista.insert(3);
    lista.insert(4);

    lista.getList();

    return 0;
}