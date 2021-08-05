#include <iostream>

using namespace std;

class NodoDoble
{
    protected:
        int carnet, creditos, edad;
        long long int DPI;
        string nombre, carrera, password;

        NodoDoble* siguiente;
        NodoDoble* anterior;

    public:
        NodoDoble(int carnet, int DPI, string nombre, string carrera, string password, int creditos, int edad):
        carnet(carnet), DPI(DPI), nombre(nombre), carrera(carrera), password(password), creditos(creditos), edad(edad), siguiente(NULL), anterior(NULL)
        {}

        int getCarnet() const
        {
            return carnet;
        }

        long long int getDPI() const
        {
            return DPI;
        }

        string getNombre() const
        {
            return nombre;
        }

        string getCarrera() const
        {
            return carrera;
        }

        string getPassword() const
        {
            return password;
        }

        int getCreditos() const
        {
            return creditos;
        }

        int getEdad() const
        {
            return edad;
        }

        NodoDoble* siguienteNodo()
        {
            return siguiente;
        }

        NodoDoble* anteriorNodo()
        {
            return anterior;
        }

        void setSiguiente(NodoDoble* s)
        {
            siguiente = s;
        }

        void setAnterior(NodoDoble* a)
        {
            anterior = a;
        }
};