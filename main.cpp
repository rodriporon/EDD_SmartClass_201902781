#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int option;
    bool rep = true;

    do {

        

        cout << "\n\n Menú " << endl;

        cout << "1- Carga de Usuarios" << endl;
        cout << "2- Carga de Tareas" << endl;
        cout << "3- Ingreso Manual" << endl;
        cout << "4- Reportes" << endl;
        cout << "5- Salir" << endl;

        cout << "Seleccione una opción: ";
        cin >> option;

        switch (option) {
            case 1:


            break;
            
            case 2:

            break;

            case 3:

            break;

            case 4:

            break;

            case 5:

            rep = false;
            break;

        }
    } while (rep);
    system("pause");

}