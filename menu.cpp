#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include "ListaDoble.h"
#include "Cola.h"
#include "Verify.h"
#include "NodoMatriz.h"
#include "GetIndex.h"

using namespace std;

int main()
{

    ListaDoble *listaUsuarios = new ListaDoble();

    Cola *colaErrores = new Cola();

    NodoMatriz *matriz[5][30][9];
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                matriz[i][j][k] = NULL;
            }
        }
    }

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

            string carnet = "";
            string DPI = "";
            string nombre = "";
            string carrera = "";
            string correo = "";
            string password = "";
            int creditos = 0;
            int edad = 0;

            ifstream archivo;
            string rutaUsuarios;
            string texto;
            string value;

            cin.ignore();

            cout << "Ingrese la ruta del archivo de Usuarios" << endl;
            getline(cin, rutaUsuarios, '\n');

            cout << "La ruta es: " << rutaUsuarios << endl;

            archivo.open(rutaUsuarios, ios::in);

            if (archivo.fail())
            {
                cout << "No se puedo abrir el archivo" << endl;
                exit(1);
            }

            int contador = 0;
            int id_errores = 0;
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
                            carnet = value;
                            if (isCarnet(carnet) == false)
                            {
                                cout << "El carnet " << carnet << " no es válido" << endl;
                                colaErrores->encolar(id_errores, "Estudiante", "Carnet inválido");
                                break;
                            }
                            break;

                        case 1:
                            DPI = value;
                            if (isDPI(DPI) == false)
                            {
                                cout << "El DPI " << DPI << " no es válido" << endl;
                                colaErrores->encolar(id_errores, "Estudiante", "DPI inválido");
                                break;
                            }

                            break;

                        case 2:
                            nombre = value;
                            break;

                        case 3:
                            carrera = value;
                            break;

                        case 4:
                            password = value;
                            break;

                        case 5:

                            creditos = atoi(value.c_str());
                            break;

                        case 6:
                            edad = atoi(value.c_str());
                            break;

                        case 7:
                            correo = value;
                            if (isCorreo(correo) == false)
                            {
                                cout << "El Correo " << correo << " no es válido" << endl;
                                colaErrores->encolar(id_errores, "Estudiante", "Correo inválido");
                                break;
                            }

                            break;

                        default:
                            break;
                        }

                        contador_value++;
                    }

                    listaUsuarios->insert(carnet, DPI, nombre, carrera, correo, password, creditos, edad);
                    //id_errores++;
                }

                contador++;
            }

            listaUsuarios->getList();

            archivo.close();
        }

        break;

        case 2:

        {
            string mes = "";
            string dia = "";
            string hora = "";
            string carnet = "";
            string nombre = "";
            string descripcion = "";
            string materia = "";
            string fecha = "";
            string estado = "";

            ifstream archivo;
            string rutaTareas;
            string texto;
            string value;

            cin.ignore();

            cout << "Ingrese la ruta del archivo de Tareas" << endl;
            getline(cin, rutaTareas, '\n');

            cout << "La ruta es: " << rutaTareas << endl;

            archivo.open(rutaTareas, ios::in);

            if (archivo.fail())
            {
                cout << "No se pudo abrir el archivo" << endl;
                exit(1);
            }

            int contador = 0;
            int id_errores = 0;
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
                            mes = value;
                            break;

                        case 1:
                            dia = value;
                            break;

                        case 2:
                            hora = value;
                            break;

                        case 3:
                            carnet = value;
                            break;

                        case 4:
                            nombre = value;
                            break;

                        case 5:

                            descripcion = value;
                            break;

                        case 6:
                            materia = value;
                            break;

                        case 7:
                            fecha = value;
                            break;

                        case 8:
                            estado = value;
                            break;

                        default:
                            break;
                        }

                        contador_value++;
                    }

                    //Insertar valores en la matriz
                    cout << "Indices ingresados a la matriz: "
                         << "mes: " << mes << " dia: " << dia << " hora: " << hora << endl;
                    cout << "Valores devueltos por función getIndex: "
                         << "mes: " << getIndexMonth(mes) << " dia: " << getIndexDay(dia) << " hora: " << getIndexHour(hora) << endl;
                    matriz[getIndexMonth(mes)][getIndexDay(dia)][getIndexHour(hora)] = new NodoMatriz(mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado);
                    //id_errores++;
                }

                contador++;
            }

            //Inicializando la matriz de 3 dimensiones

            archivo.close();

            /* cout << matriz[0][0][0]->getCarnet() << endl;
            cout << matriz[0][0][0]->getMes() << endl; */

            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 30; j++)
                {
                    for (int k = 0; k < 9; k++)
                    {
                        if (matriz[i][j][k] != NULL)
                        {
                            cout << matriz[i][j][k]->getCarnet() << endl;
                        }
                        
                    }
                }
            }
        }

        break;

        case 3:
        {
            int option_3;
            bool rep_3 = true;

            do
            {
                cout << "\n\n ---Ingreso Manual--- " << endl;
                cout << "1- Usuarios" << endl;
                cout << "2- Tareas" << endl;
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
                        cout << "\n\n1- Ingresar" << endl;
                        cout << "2- Modificar" << endl;
                        cout << "3- Eliminar" << endl;
                        cout << "4- Regresar" << endl;

                        cout << "Seleccione una opción: ";
                        cin >> optionStudent;

                        switch (optionStudent)
                        {
                        case 1:
                        {

                            string carnet = "";
                            string DPI = "";
                            string nombre;
                            string carrera;
                            string correo;
                            string password;
                            int creditos = 0;
                            int edad = 0;

                            cout << "\n\n ---Ingresar---" << endl;

                            cout << "Carnet: ";
                            getline(cin, carnet, '\n');
                            cin.ignore();

                            cout << "DPI: ";
                            getline(cin, DPI, '\n');

                            cout << "Nombre: ";
                            getline(cin, nombre, '\n');

                            cout << "Carrera: ";
                            getline(cin, carrera, '\n');

                            cout << "Correo: ";
                            getline(cin, correo, '\n');

                            cout << "Password: ";
                            getline(cin, password, '\n');

                            cout << "Creditos: ";
                            cin >> creditos;

                            cout << "Edad: ";
                            cin >> edad;
                            cin.ignore();

                            listaUsuarios->insert(carnet, DPI, nombre, carrera, correo, password, creditos, edad);

                            listaUsuarios->getList();
                        }

                        break;

                        case 2:
                        {
                            cin.ignore();

                            string search_DPI;

                            cout << "\n\n ---Modificar---" << endl;
                            cout << "Ingrese el DPI: ";
                            getline(cin, search_DPI, '\n');

                            listaUsuarios->modify(search_DPI);

                            listaUsuarios->getList();
                        }

                        break;
                        case 3:

                        {
                            cin.ignore();

                            string delete_DPI;

                            cout << "\n\n ---Eliminar---" << endl;
                            cout << "Ingrese el DPI: ";
                            getline(cin, delete_DPI, '\n');

                            listaUsuarios->deleteUser(delete_DPI);

                            listaUsuarios->getList();
                        }

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