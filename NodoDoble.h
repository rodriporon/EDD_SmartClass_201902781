#include <iostream>

using namespace std;

class NodoDoble
{
    protected:
        int carnet, creditos, edad;
        string nombre, carrera, correo, password, DPI;

        NodoDoble* siguiente;
        NodoDoble* anterior;

    public:
        NodoDoble(int carnet, string DPI, string nombre, string carrera, string correo, string password, int creditos, int edad):
        carnet(carnet), DPI(DPI), nombre(nombre), carrera(carrera), correo(correo), password(password), creditos(creditos), edad(edad), siguiente(NULL), anterior(NULL)
        {}

        int getCarnet() const
        {
            return carnet;
        }

        string getDPI() const
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

        string getCorreo() const
        {
            return correo;
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