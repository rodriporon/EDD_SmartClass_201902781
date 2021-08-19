#include <iostream>
#include <string>


using namespace std;

class NodoMatriz
{
    private:
        int id;
        string mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado;

    public:
        NodoMatriz();
        NodoMatriz(string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);

        string getMes();
        string getDia();
        string getHora();
        string getCarnet();
        string getNombre();
        string getDescripcion();
        string getMateria();
        string getFecha();
        string getEstado();

        void setMes(string mes);
        void setDia(string dia);
        void setHora(string hora);
        void setCarnet(string carnet);
        void setNombre(string nombre);
        void setDescripcion(string descripcion);
        void setMateria(string materia);
        void setFecha(string fecha);
        void setEstado(string estado);

};

NodoMatriz::NodoMatriz()
{
    this->mes = "-1";
    this->dia = "-1";
    this->hora = "-1";
    this->carnet = "-1";
    this->nombre = "-1";
    this->descripcion = "-1";
    this->materia = "-1";
    this->fecha = "-1";
    this->estado = "-1";
}

NodoMatriz::NodoMatriz(string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
{
    this->mes = mes;
    this->dia = dia;
    this->hora = hora;
    this->carnet = carnet;
    this->nombre = nombre;
    this->descripcion = descripcion;
    this->materia = materia;
    this->fecha = fecha;
    this->estado = estado;
}

string NodoMatriz::getMes()
{
    return this->mes;
}

string NodoMatriz::getDia()
{
    return this->dia;
}

string NodoMatriz::getHora()
{
    return this->hora;
}

string NodoMatriz::getCarnet()
{
    return carnet;
}

string NodoMatriz::getNombre()
{
    return this->nombre;
}

string NodoMatriz::getDescripcion()
{
    return this->descripcion;
}

string NodoMatriz::getMateria()
{
    return this->materia;
}

string NodoMatriz::getFecha()
{
    return this->fecha;
}

string NodoMatriz::getEstado()
{
    return this->estado;
}

void NodoMatriz::setMes(string mes)
{
    this->mes = mes;
}

void NodoMatriz::setDia(string dia)
{
    this->dia = dia;
}

void NodoMatriz::setHora(string hora)
{
    this->hora = hora;
}

void NodoMatriz::setCarnet(string carnet)
{
    this->carnet = carnet;
}

void NodoMatriz::setNombre(string nombre)
{
    this->nombre = nombre;
}

void NodoMatriz::setDescripcion(string descripcion)
{
    this->descripcion = descripcion;
}

void NodoMatriz::setMateria(string materia)
{
    this->materia = materia;
}

void NodoMatriz::setFecha(string fecha)
{
    this->fecha = fecha;
}

void NodoMatriz::setEstado(string estado)
{
    this->estado = estado;
}