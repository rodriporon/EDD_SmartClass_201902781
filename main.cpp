#include <iostream>
#include "ListaDoble.h"

using namespace std;

int main(){

    ListaDoble lista;

    lista.insert(201902781, 3065713820401, "Rodrigo Porón", "Ingeniería en Sistemas", "password123", 120, 22);
    lista.insert(201902245, 3065713820401, "Rodolfo Porón", "Ingeniería Industrial", "password123", 120, 22);

    lista.getList();

    return 0;
}