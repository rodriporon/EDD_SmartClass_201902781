#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include "ListaDobleCircular.h"
#include "ListaD.h"
#include "Cola.h"
#include "LinkedList.h"
#include "Verify.h"
#include "NodoMatriz.h"
#include "GetIndex.h"

using namespace std;

int main()
{

    ListaDoble *listaUsuarios = new ListaDoble();

    ListaD *listaTareas = new ListaD();

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

    /*     listaTareas->insert("201902781", "Rodrigo Porón", "Nada", "mate", "212", "no");
    listaTareas->getList(); */

    int id_errores = 0;
    int option;
    bool rep = true;

    do
    {

        cout << "\n\n ---Menú--- " << endl;
        cout << "1- Carga de Usuarios" << endl;
        cout << "2- Carga de Tareas" << endl;
        cout << "3- Ingreso Manual" << endl;
        cout << "4- Reportes" << endl;
        cout << "5- Cola Errores" << endl;
        cout << "6- Salir" << endl;

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
                                id_errores++;
                                break;
                            }
                            break;

                        case 1:
                            DPI = value;
                            if (isDPI(DPI) == false)
                            {
                                cout << "El DPI " << DPI << " no es válido" << endl;
                                colaErrores->encolar(id_errores, "Estudiante", "DPI inválido");
                                id_errores++;
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
                                id_errores++;
                                break;
                            }

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

            //listaUsuarios->getList();

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
            int contador_value;

            while (!archivo.eof())
            {

                bool carnetFinded = false;

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
                            carnetFinded = listaUsuarios->searchCarnet(carnet);
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
                            if (isFecha(fecha) == false)
                            {
                                cout << "La fecha " << fecha << " no es válida" << endl;
                                colaErrores->encolar(id_errores, "Tarea", "Fecha inválida");
                                id_errores++;
                                break;
                            }
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
                    if (carnetFinded)
                    {
                        //             i=mes              j=dia            z=hora
                        matriz[getIndexMonth(mes)][getIndexDay(dia)][getIndexHour(hora)] = new NodoMatriz(mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado);
                    }
                    else
                    {
                        colaErrores->encolar(id_errores, "Tarea", "Carnet no registrado previamente");
                        id_errores++;
                    }
                }

                contador++;
            }

            archivo.close();

            /* cout << matriz[0][0][0]->getCarnet() << endl;
            cout << matriz[0][0][0]->getMes() << endl; */
            int column_major;
            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 30; j++)
                {
                    for (int k = 0; k < 9; k++)
                    {
                        column_major = j + 30 * (k + 9 * i);
                        //cout << column_major << endl;
                        //m   d  h
                        if (matriz[i][j][k] != NULL)
                        {

                            listaTareas->insert(column_major, matriz[i][j][k]->getMes(), matriz[i][j][k]->getDia(), matriz[i][j][k]->getHora(), matriz[i][j][k]->getCarnet(), matriz[i][j][k]->getNombre(), matriz[i][j][k]->getDescripcion(), matriz[i][j][k]->getMateria(), matriz[i][j][k]->getFecha(), matriz[i][j][k]->getEstado());
                        }
                        else
                        {
                            listaTareas->insert(column_major, "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1");
                        }
                    }
                }
            }
            //listaTareas->graficar();
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

                            //listaUsuarios->getList();
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
                        {
                            cout << "\n\n ---Ingresar---" << endl;
                            int index;

                            string mes_b, dia_b, hora_b;
                            int insertar_cj;
                            cin.ignore();
                            cout << "Ingrese las posiciones en los que desea guardar la tarea: " << endl;
                            cout << "Mes: ";
                            getline(cin, mes_b, '\n');
                            cout << "Dia: ";
                            getline(cin, dia_b, '\n');
                            cout << "Hora: ";
                            getline(cin, hora_b, '\n');

                            insertar_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                            if (listaTareas->isNull(insertar_cj, mes_b, dia_b, hora_b))
                            {
                                cout << "Tarea agregada con éxito" << endl;
                            }
                            else
                            {
                                cout << "La tarea no se pudo agregar" << endl;
                            }
                        }

                        break;

                        case 2:

                        {

                            cout << "\n\n ---Modificar---" << endl;
                            cin.ignore();

                            int index_cj;
                            string mes_b, dia_b, hora_b;

                            cout << "\n\n ---Modificar---" << endl;
                            cout << "Ingrese los siguientes datos: ";
                            cout << "Mes: ";
                            getline(cin, mes_b, '\n');

                            cout << "Día: ";
                            getline(cin, dia_b, '\n');

                            cout << "Hora: ";
                            getline(cin, hora_b, '\n');

                            index_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                            listaTareas->modify(index_cj, mes_b, dia_b, hora_b);
                        }

                        break;
                        case 3:
                        {
                            cin.ignore();
                            int index_cj;
                            string mes_b, dia_b, hora_b;

                            cout << "\n\n ---Eliminar---" << endl;
                            cout << "Ingrese los siguientes datos: ";
                            cout << "Mes: ";
                            getline(cin, mes_b, '\n');

                            cout << "Día: ";
                            getline(cin, dia_b, '\n');

                            cout << "Hora: ";
                            getline(cin, hora_b, '\n');

                            index_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                            listaTareas->deleteTask(index_cj);
                            cin.ignore();
                        }
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
        {
            int optionReports;
            bool repReports = true;

            do
            {
                cout << "\n\n ---Reportes---" << endl;
                cout << "1- Reporte sobre la Lista de Estudiantes" << endl;
                cout << "2- Reporte sobre la Lista de Tareas Linealizadas" << endl;
                cout << "3- Búsqueda en Estructura Linealizada" << endl;
                cout << "4- Búsqueda de Posición en Lista Linealizada" << endl;
                cout << "5- Cola Errores" << endl;
                cout << "6- Código generado de Salida" << endl;
                cout << "7- Salir" << endl;

                cout << "Seleccione una opción: ";
                cin >> optionReports;

                switch (optionReports)
                {
                case 1:
                {
                    cout << "\n\n ---Lista de Estudiantes---" << endl;
                    listaUsuarios->graficar();
                    break;
                }

                case 2:
                {
                    cout << "\n\n ---Lista de Tareas Linealizadas---" << endl;
                    listaTareas->graficar();

                    break;
                }

                case 3:
                {
                    cout << "\n\n ---Búsqueda en Estructura Linealizada ---" << endl;
                    cin.ignore();
                    string mes_b, dia_b, hora_b;
                    int buscar_cj;

                    cout << "Mes: ";
                    getline(cin, mes_b, '\n');
                    cout << "Dia: ";
                    getline(cin, dia_b, '\n');
                    cout << "Hora: ";
                    getline(cin, hora_b, '\n');

                    buscar_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                    listaTareas->searchIndex(buscar_cj);
                }
                break;

                case 4:
                {
                    cout << "\n\n ---Búsqueda de Posición en Lista Linealizada---" << endl;
                    cin.ignore();
                    string mes_b, dia_b, hora_b;
                    int buscar_cj;

                    cout << "Mes: ";
                    getline(cin, mes_b, '\n');
                    cout << "Dia: ";
                    getline(cin, dia_b, '\n');
                    cout << "Hora: ";
                    getline(cin, hora_b, '\n');

                    buscar_cj = getIndexDay(dia_b) + 30 * (getIndexHour(hora_b) + 9 * getIndexMonth(mes_b));
                    cout << "La posición linealizada es: " << buscar_cj << endl;
                }

                break;

                case 5:
                {
                    cout << "\n\n ---Cola de Errores---" << endl;
                    colaErrores->graficar();
                    break;
                }

                case 6:
                {
                    cout << "\n\n ---Código Generado de Salida---" << endl;
                    if (colaErrores->vacia())
                    {
                        int cantidad;
                        string Texto = "";
                        string Texto_t = "";
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
                            archivo << Texto;
                            Texto_t = listaTareas->getText(carnet);
                            archivo << Texto_t;
                        }

                        archivo << "¿$Elements?" << endl;

                        archivo.close();
                        cout << "Archivo escrito correctamente" << endl;
                    }
                    else
                    {
                        cout << "Tiene errores en su archivo" << endl;
                    }

                    break;
                }

                case 7:
                    repReports = false;
                    break;

                default:
                    break;
                }

            } while (repReports);
        }

        break;

        case 5:
        {
            int optionErrores;
            bool repErrores = true;

            do
            {
                cin.ignore();
                cout << "\n\n ---Los errores en la cola son los siguientes: ---" << endl;
                colaErrores->mostrar();

                cout << "\n\n: Opciones de la cola:" << endl;
                cout << "1- Desencolar error" << endl;
                cout << "2- Salir" << endl;

                cout << "Seleccione la opción que desee efectuar: ";
                cin >> optionErrores;

                switch (optionErrores)
                {
                case 1:
                {
                    colaErrores->desencolar();
                    break;
                }

                case 2:
                    repErrores = false;
                    break;
                default:
                    cout << "Seleccione una opción correcta" << endl;
                    break;
                }
            } while (repErrores);

            cout << "\n\n ---Los errores en la cola son los siguientes: ---" << endl;
            colaErrores->mostrar();

            cout << "\n\n: ---" << endl;
            cout << "1- Desencolar error" << endl;

            cout << "Seleccione la opción que desee efectuar: ";
            cin >> optionErrores;

            break;
        }

        case 6:

            rep = false;
            break;

        default:
            cout << "Ingrese una opción válida" << endl;
            break;
        }
    } while (rep);
    system("pause");
}
