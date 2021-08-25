#include <iostream>
#include <fstream>
#include "ListaD.h"
#include "ListaDobleCircular.h"
using namespace std;

void escribirArchivo()
{
    ListaDoble *listaUsuarios = new ListaDoble();
    int cantidad;
    string Texto = "";
    string carnet;
    cantidad = listaUsuarios->getCantidad();

    listaUsuarios->getList();
    string nombreArchivo = "Reportes\\Estudiantes.txt";
    ofstream archivo;
    archivo.open(nombreArchivo.c_str(), fstream::out);
    archivo << "¿Elements?" << endl;

    for (int i = 0; i <= cantidad; i++)
    {
        carnet = listaUsuarios->getCarnet(i);
        Texto = listaUsuarios->getText(carnet);
        archivo << Texto << endl;
        cout << Texto << endl;
        cout << carnet << endl;
    }

    
    archivo << "¿$Elements?" << endl;

    archivo.close();
    cout << "Archivo escrito correctamente" << endl;
};
