#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include "ListaDoble.h"

using namespace std;

int main()
{

    ListaDoble *listaUsuarios = new ListaDoble();

    int option;
    bool rep = true;

    do
    {

        cout << "\n\n ---Menú--- " << endl;
        cout << "1- Carga de Usuarios" << endl;
        cout << "2- Carga de Tareas" << endl;
        cout << "3- Ingreso Manual" << endl;
        cout << "4- Reportes" << endl;
        cout << "5- Salir" << endl;

        cout << "Seleccione una opción: ";
        cin >> option;

        switch (option)
        {
        case 1:
        {

            ifstream archivo;
            string rutaUsuarios;
            string texto;
            string value;

            int carnet = 0;
            string DPI = "";
            string nombre = "";
            string carrera = "";
            string correo = "";
            string password = "";
            int creditos = 0;
            int edad = 0;

            cout << "Ingrese la ruta del archivo de Usuarios" << endl;
            cin >> rutaUsuarios;

            cout << "La ruta es: " << rutaUsuarios << endl;

            archivo.open(rutaUsuarios, ios::in);

            if (archivo.fail())
            {
                cout << "No se puedo abrir el archivo" << endl;
                exit(1);
            }

            int contador = 0;

            int contador_value;

            while (!archivo.eof())
            {

                getline(archivo, texto);
                //cout << "..........." << endl;

                stringstream input_stringstream(texto);

                contador_value = 0;

                if (contador != 0)
                {

                    while (getline(input_stringstream, value, ','))
                    {
                        //cout << value << endl;

                        switch (contador_value)
                        {
                        case 0:
                            carnet = atoi(value.c_str());
                            break;

                        case 1:
                            DPI = value;
                            break;

                        case 2:
                            nombre = value;
                            break;

                        case 3:
                            carrera = value;
                            break;

                        case 4:
                            correo = value;
                            break;

                        case 5:
                            password = value;
                            break;

                        case 6:
                            creditos = atoi(value.c_str());
                            break;

                        case 7:
                            edad = atoi(value.c_str());
                            break;

                        default:
                            break;
                        }

                        contador_value++;
                    }

                    listaUsuarios->insert(carnet, DPI, nombre, carrera, correo, password, creditos, edad);
                }

                contador++;
            }

            listaUsuarios->getList();

            archivo.close();
        }

        break;

        case 2:

            cout << "Ingrese la ruta del archivo de Tareas" << endl;

            break;

        case 3:
        {
            int option_3;
            bool rep_3 = true;

            do
            {
                cout << "\n\n ---Ingreso Manual--- " << endl;
                cout << "1- Ingreso de Estudiante" << endl;
                cout << "2- Ingreso de Tarea" << endl;
                cout << "3- Salir" << endl;

                cout << "Seleccione una opción: " << endl;
                cin >> option_3;

                switch (option_3)
                {
                case 1:
                {
                    int optionStudent;
                    bool repStudent = true;

                    do
                    {
                        cout << "1- Ingresar" << endl;
                        cout << "2- Modificar" << endl;
                        cout << "3- Eliminar" << endl;
                        cout << "4- Regresar" << endl;

                        cout << "Seleccione una opción: ";
                        cin >> optionStudent;

                        switch (optionStudent)
                        {
                        case 1:

                            cout << "\n\n ---Ingresar---" << endl;

                            break;

                        case 2:

                            cout << "\n\n ---Modificar---" << endl;

                            break;
                        case 3:

                            cout << "\n\n ---Eliminar---" << endl;

                            break;

                        case 4:

                            repStudent = false;
                            break;

                        default:

                            cout << "Ingrese una opción válida" << endl;
                            break;
                        }

                    } while (repStudent);
                }

                break;

                case 2:

                {
                    int optionTasks;
                    bool repTasks = true;

                    do
                    {
                        cout << "1- Ingresar" << endl;
                        cout << "2- Modificar" << endl;
                        cout << "3- Eliminar" << endl;
                        cout << "4- Regresar" << endl;

                        cout << "Seleccione una opción: ";
                        cin >> optionTasks;

                        switch (optionTasks)
                        {
                        case 1:

                            cout << "\n\n ---Ingresar---" << endl;

                            break;

                        case 2:

                            cout << "\n\n ---Modificar---" << endl;

                            break;
                        case 3:

                            cout << "\n\n ---Eliminar---" << endl;

                            break;

                        case 4:

                            repTasks = false;
                            break;

                        default:

                            cout << "Ingrese una opción válida" << endl;
                            break;
                        }

                    } while (repTasks);
                }

                break;

                case 3:
                    rep_3 = false;
                    break;

                default:
                    cout << "Ingrese una opción válida" << endl;
                    break;
                }

            } while (rep_3);
        }
        break;

        case 4:

            break;

        case 5:

            rep = false;
            break;

        default:
            cout << "Ingrese una opción válida" << endl;
            break;
        }
    } while (rep);
    system("pause");
}