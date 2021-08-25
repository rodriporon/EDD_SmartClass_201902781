#pragma once
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
    void insert(string carnet, string DPI, string nombre, string carrera, string correo, string password, int creditos, int edad);
    NodoDoble *getNode();
    void modify(string modify_DPI);
    bool searchCarnet(string search_carnet);
    void deleteUser(string delete_DPI);
    void getList();
    string getText(string carnet);
    void graficar();
    int getCantidad();
    string recorrer();
    string getCarnet(int pos);
};

bool ListaDoble::isEmpty()
{
    return first == NULL;
}

NodoDoble *ListaDoble::getNode()
{
    return NULL;
}

void ListaDoble::modify(string modify_DPI)
{
    int cfinded = 0;
    NodoDoble *search;

    search = first;

    if (first != NULL)
    {
        do
        {
            if (search->getDPI() == modify_DPI)
            {
                cout << "\n\n DPI encontrado " << endl;

                string carnet = "";
                string DPI = "";
                string nombre;
                string carrera;
                string correo;
                string password;
                int creditos = 0;
                int edad = 0;

                int opt_modify;
                bool rep_modify = true;

                do
                {

                    cout << "1- Carnet" << endl;
                    cout << "2- DPI" << endl;
                    cout << "3- Nombre" << endl;
                    cout << "4- Carrera" << endl;
                    cout << "5- Correo" << endl;
                    cout << "6- Password" << endl;
                    cout << "7- Créditos" << endl;
                    cout << "8- Edad" << endl;
                    cout << "9- SALIR" << endl;

                    cout << "\n\n Seleccione la opción que desea modificar: ";
                    cin >> opt_modify;

                    cin.ignore();

                    switch (opt_modify)
                    {
                    case 1:
                    {
                        cout << "Carnet: ";
                        getline(cin, carnet, '\n');
                        cin.ignore();

                        search->setCarnet(carnet);
                    }
                    break;

                    case 2:
                    {
                        cout << "DPI: ";
                        getline(cin, DPI, '\n');

                        search->setDPI(DPI);
                    }
                    break;

                    case 3:
                    {
                        cout << "Nombre: ";
                        getline(cin, nombre, '\n');

                        search->setNombre(nombre);
                    }
                    break;

                    case 4:
                    {
                        cout << "Carrera: ";
                        getline(cin, carrera, '\n');

                        search->setCarrera(carrera);
                    }
                    break;

                    case 5:
                    {
                        cout << "Correo: ";
                        getline(cin, correo, '\n');

                        search->setCorreo(correo);
                    }
                    break;

                    case 6:
                    {
                        cout << "Password: ";
                        getline(cin, password, '\n');

                        search->setPassword(password);
                    }
                    break;

                    case 7:
                    {
                        cout << "Creditos: ";
                        cin >> creditos;

                        search->setCreditos(creditos);
                    }
                    break;

                    case 8:
                    {
                        cout << "Edad: ";
                        cin >> edad;
                        cin.ignore();

                        search->setEdad(edad);
                    }
                    break;

                    case 9:

                        opt_modify = false;

                        break;

                    default:

                        cout << "Ingrese una opción válida" << endl;
                        break;
                    }

                } while (opt_modify);

                cfinded = -1;
            }

            search = search->siguienteNodo();
        } while (search != first && cfinded == 0);
        if (cfinded == 0)
        {
            cout << "El DPI ingresado no se encontró" << endl;
        }
    }
    else
    {
        cout << "Empty List";
    }
}
void ListaDoble::insert(string carnet, string DPI, string nombre, string carrera, string correo, string password, int creditos, int edad)
{
    NodoDoble *newNode = new NodoDoble(carnet, DPI, nombre, carrera, correo, password, creditos, edad);

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

bool ListaDoble::searchCarnet(string search_carnet)
{
  NodoDoble *search;
  search = first;
  int cfinded = 0;

    if (first != NULL)
    {
        do
        {
            if (search->getCarnet() == search_carnet)
            {
                cfinded = -1;
                return true;
            }
            search = search->siguienteNodo();

            
        } while (search != first && cfinded == 0);

        
        
    }
    return false;
}

void ListaDoble::deleteUser(string delete_DPI)
{
    NodoDoble *search;
    NodoDoble *delete_User;

    search = first;
    delete_User = NULL;
    int cfinded = 0;
    int confirm;

    if (first != NULL)
    {
        do
        {
            if (search->getDPI() == delete_DPI)
            {
                cout << "DPI encontrado" << endl;

                cout << "\n1- Sí" << endl;
                cout << "2- No" << endl;
                cout << "¿Está seguro que desea eliminar a " << search->getNombre() << "?: ";
                cin >> confirm;

                if (confirm == 1)
                {
                    if (search == first)
                    {
                        first = first->siguienteNodo();
                        first->setAnterior(last);
                        last->setSiguiente(first);
                    }
                    else if (search == last)
                    {
                        last = last->anteriorNodo();
                        first->setAnterior(last);
                        last->setSiguiente(first);
                    }
                    else
                    {
                        delete_User->setSiguiente(search->siguienteNodo());
                        search->siguienteNodo()->setAnterior(delete_User);
                    }

                    cfinded = -1;
                } else if (confirm == 2)
                {
                    cout << "No se eliminó al usuario" << endl;
                } else {
                    cout << "Elija una opción correcta" << endl;
                }


                
            }
            delete_User = search;
            search = search->siguienteNodo();

        } while (search != first && cfinded == 0);

        if (cfinded == 0)
        {
            cout << "El DPI ingresado no se encontró" << endl;
        }
        else
        {
            free(delete_User);
            cout << "Usuario eliminado" << endl;
        }
    }
    else
    {
        cout << "Empty list" << endl;
    }
}

void ListaDoble::getList()
{
    NodoDoble *aux;
    aux = first;

    if (first != NULL)
    {
        do
        {
            cout << "["
                 << "Carnet: " << aux->getCarnet() << "DPI: " << aux->getDPI() << "Nombre: " << aux->getNombre() << " Carrera: " << aux->getCarrera() << "Password: " << aux->getPassword() << "Creditos: " << aux->getCreditos() << "Edad: " << aux->getEdad() << "Correo: " << aux->getCorreo() << "]" << endl;
            aux = aux->siguienteNodo();
        } while (aux != first);
    }
    else
    {
        cout << "Empty List";
    }
}

int ListaDoble::getCantidad()
{
    int cantidad = 0;
    NodoDoble *aux;
    aux = first;

    if (first != NULL)
    {
        do
        {
            cantidad++;
            aux = aux->siguienteNodo();
        } while (aux != first);
    }
    return cantidad;
}

string ListaDoble::getCarnet(int pos)
{
    NodoDoble *aux;
    aux = first;
    int position = 0;
    if (first != NULL)
    {
        do
        {
            if (position == pos)
            {
                return aux->getCarnet();
            }
            aux = aux->siguienteNodo();
            position++;
        } while (aux != first);
        
    }
    return "-0";
}

string ListaDoble::getText(string carnet)
{
    string Texto = "";
    NodoDoble *aux;
    aux = first;

    if (first != NULL)
    {
        do
        {
            if (aux->getCarnet() == carnet)
            {
                Texto += "\t¿element type=\"user\"?\n";
                Texto+= "\t\t¿item Carnet = \""+aux->getCarnet() +"\" $?\n";
                Texto+= "\t\t¿item DPI = \""+aux->getDPI() +"\" $?\n";
                Texto+= "\t\t¿item Nombre = \""+aux->getNombre() +"\" $?\n";
                Texto+= "\t\t¿item Carrera = \""+aux->getCarrera() +"\" $?\n";
                Texto+= "\t\t¿item Password = \""+aux->getPassword() +"\" $?\n";
                Texto+= "\t\t¿item Creditos = "+ to_string(aux->getCreditos())  +" $?\n";
                Texto+= "\t\t¿item Edad = "+ to_string(aux->getEdad())  +" $?\n";
                Texto+="\t¿element?\n";
                return Texto;
            }
            
            aux = aux->siguienteNodo();
        } while (aux != first);
    }
    return Texto;
}

void ListaDoble::graficar()
{
    string grafica = "";
    ofstream archivo;
    archivo.open("Reportes\\ListaDobleCircular.dot");
    archivo << "digraph {\n rankdir=TB;\n";
    grafica = recorrer();
    archivo << grafica;
    archivo << "}\n";
    archivo.close();

    system("dot -Tpng Reportes\\ListaDobleCircular.dot -o Reportes\\ListaDobleCircular.png -Gcharset=latin1");
    system("Reportes\\ListaDobleCircular.png");
    
}

string ListaDoble::recorrer()
{
    string grafo = "";
    NodoDoble *aux = first;
    if (first != NULL)
    {
        do
        {
                
            grafo += "\tNodo" + aux->getDPI() + "->" + "\tNodo" + aux->siguienteNodo()->getDPI() + "[constraint=false]; \n";

            grafo += "\tNodo" + aux->getDPI() + "->" + "\tNodo" + aux->siguienteNodo()->getDPI() + "[dir=back, constraint=false]; \n";

            grafo += "\n \tNodo" + aux->getDPI() + "[shape=box,style=filled,color=skyblue , label = \"-Carnet: " + aux->getCarnet() + "\n -DPI: " + aux->getDPI() + "\n -Nombre: " + aux->getNombre() + "\n -Carrera: " + aux->getCarrera() + "\n -Password: " + aux->getPassword() + "\n -Creditos: " + to_string(aux->getCreditos()) + "\n -Edad: " + to_string(aux->getEdad()) + "\n -Edad: " + aux->getCorreo() + " \"] \n";
            aux = aux->siguienteNodo();
        } while (aux != first);
    }
    return grafo;
}