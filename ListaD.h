#include <iostream>
#include "NodoD.h"
#include "GetIndex.h"

using namespace std;

class ListaD
{
protected:
    NodoD *first;
    NodoD *last;

public:
    ListaD()
    {
        first = NULL;
        last = NULL;
    }

    bool isEmpty();
    void insert(int index, string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);
    void modify(int index, string mes, string dia, string hora);
    bool searchIndex(int search_index);
    bool isNull(int index, string mes, string dia, string hora);
    void deleteTask(int index);
    void getList();
};

bool ListaD::isEmpty()
{
    return first == NULL;
}

void ListaD::modify(int index, string mes, string dia, string hora)
{
    int cfinded = 0;
    NodoD *search;

    search = first;

    if (first != NULL)
    {
        do
        {
            if (search->getIndex() == index)
            {
                cout << "\n\n Tarea encontrada " << endl;

                int index_cj;
                string mes_b = mes;
                string dia_b = dia;
                string hora_b = hora;
                string carnet, nombre, descripcion, materia, fecha, estado;

                int opt_modify;
                bool rep_modify = true;

                do
                {

                    cout << "1- Mes" << endl;
                    cout << "2- Día" << endl;
                    cout << "3- Hora" << endl;
                    cout << "4- Carnet" << endl;
                    cout << "5- Nombre" << endl;
                    cout << "6- Descripción" << endl;
                    cout << "7- Materia" << endl;
                    cout << "8- Fecha" << endl;
                    cout << "9- Estado" << endl;
                    cout << "10- SALIR" << endl;

                    cout << "\n\n Seleccione la opción que desea modificar: ";
                    cin >> opt_modify;

                    cin.ignore();

                    switch (opt_modify)
                    {
                    case 1:
                    {
                        cout << "Mes: ";
                        getline(cin, mes_b, '\n');
                        cin.ignore();

                        search->setMes(mes);
                        index_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                        search->setIndex(index_cj);
                    }
                    break;

                    case 2:
                    {
                        cout << "Día: ";
                        getline(cin, dia_b, '\n');

                        search->setDia(dia);
                        index_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                        search->setIndex(index_cj);
                    }
                    break;

                    case 3:
                    {
                        cout << "Hora: ";
                        getline(cin, hora_b, '\n');

                        search->setHora(hora);
                        index_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                        search->setIndex(index_cj);
                    }
                    break;

                    case 4:
                    {
                        cout << "Carnet: ";
                        getline(cin, carnet, '\n');

                        search->setCarnet(carnet);
                    }
                    break;

                    case 5:
                    {
                        cout << "Nombre: ";
                        getline(cin, nombre, '\n');

                        search->setNombre(nombre);
                    }
                    break;

                    case 6:
                    {
                        cout << "Descripción: ";
                        getline(cin, descripcion, '\n');

                        search->setDescripcion(descripcion);
                    }
                    break;

                    case 7:
                    {
                        cout << "Materia: ";
                        getline(cin, materia, '\n');

                        search->setMateria(materia);
                    }
                    break;

                    case 8:
                    {
                        cout << "Fecha: ";
                        getline(cin, fecha, '\n');

                        search->setFecha(fecha);
                    }
                    break;

                    case 9:
                    {
                        cout << "Estado: ";
                        getline(cin, estado, '\n');

                        search->setEstado(estado);
                    }
                    break;

                    case 10:

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
            cout << "No se encontró la Tarea en la posición seleccionada." << endl;
        }
    }
    else
    {
        cout << "Empty List";
    }
}

void ListaD::insert(int index, string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
{
    NodoD *newNode = new NodoD(index, mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado);

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

bool ListaD::searchIndex(int search_index)
{
    NodoD *search;
    search = first;
    int cfinded = 0;

    if (first != NULL)
    {
        do
        {
            if (search->getIndex() == search_index)
            {
                cfinded = -1;
                cout << search->getCarnet() << " " << search->getMes() << endl;
                return true;
            }
            search = search->siguienteNodo();

        } while (search != first && cfinded == 0);
    }
    return false;
}

bool ListaD::isNull(int index, string mes, string dia, string hora)
{
    NodoD *search;
    search = first;
    int cfinded = 0;

    if (first != NULL)
    {
        do
        {
            if (search->getIndex() == index)
            {
                cfinded = -1;
                if (search->getCarnet() == "-1")
                {
                    cin.ignore();
                    string carnet, nombre, descripcion, materia, fecha, estado;

                    /*                     cout << "Mes: ";
                    getline(cin, mes, '\n');
                    search->setMes(mes);

                    cout << "Dia: ";
                    getline(cin, dia, '\n');
                    search->setDia(dia);

                    cout << "Hora: ";
                    getline(cin, hora, '\n');
                    search->setHora(hora); */
                    search->setMes(mes);
                    search->setDia(dia);
                    search->setHora(hora);

                    cout << "Carnet: ";
                    getline(cin, carnet, '\n');
                    search->setCarnet(carnet);

                    cout << "Nombre: ";
                    getline(cin, nombre, '\n');
                    search->setNombre(nombre);

                    cout << "Descripcion: ";
                    getline(cin, descripcion, '\n');
                    search->setDescripcion(descripcion);

                    cout << "Materia: ";
                    getline(cin, materia, '\n');
                    search->setMateria(materia);

                    cout << "Fecha: ";
                    getline(cin, fecha, '\n');
                    search->setFecha(fecha);

                    cout << "Estado: ";
                    getline(cin, estado, '\n');
                    search->setEstado(estado);
                    cin.ignore();

                    return true;
                }
            }
            search = search->siguienteNodo();

        } while (search != first && cfinded == 0);
    }
    return false;
}

void ListaD::deleteTask(int index)
{
    NodoD *search;

    search = first;
    int cfinded = 0;
    int confirm;

    if (first != NULL)
    {
        do
        {
            if (search->getIndex() == index)
            {
                cout << "Tarea encontrada" << endl;

                cout << "\n1- Sí" << endl;
                cout << "2- No" << endl;
                cout << "¿Está seguro que desea eliminar la tarea con nombre " << search->getNombre() << "?: ";
                cin >> confirm;

                if (confirm == 1)
                {
                    search->setMes("-1");
                    search->setDia("-1");
                    search->setHora("-1");
                    search->setCarnet("-1");
                    search->setNombre("-1");
                    search->setDescripcion("-1");
                    search->setMateria("-1");
                    search->setFecha("-1");
                    search->setEstado("-1");

                    cfinded = -1;
                } else if (confirm == 2)
                {
                    cout << "No se eliminó al usuario" << endl;
                } else {
                    cout << "Elija una opción correcta" << endl;
                }


                
            }
            search = search->siguienteNodo();

        } while (search != first && cfinded == 0);

        if (cfinded == 0)
        {
            cout << "La posición ingresada no se encontró" << endl;
        }
        else
        {
            cout << "Tarea eliminada" << endl;
        }
    }
    else
    {
        cout << "Empty list" << endl;
    }
}

void ListaD::getList()
{
    NodoD *aux;
    aux = first;

    if (first != NULL)
    {
        do
        {
            cout << "["
                 << "Index: " << aux->getIndex() << " Carnet: " << aux->getCarnet() << " Nombre: " << aux->getNombre() << " Descripción: " << aux->getDescripcion() << " Materia: " << aux->getMateria() << " Fecha: " << aux->getFecha() << " Estado: " << aux->getEstado() << "]" << endl;
            aux = aux->siguienteNodo();
        } while (aux != first);
    }
    else
    {
        cout << "Empty List";
    }
}
