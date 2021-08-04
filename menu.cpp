#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
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

            cout << "Ingrese la ruta del archivo de Usuarios" << endl;

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