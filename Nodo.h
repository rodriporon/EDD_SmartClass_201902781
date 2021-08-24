#include <iostream>

using namespace std;

class Nodo
{
protected:
    int index;
    string carnet, nombre, descripcion, materia, fecha, estado;
    Nodo *anterior;
    Nodo *siguiente;

public:
    Nodo(int index, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
        : index(index), carnet(carnet), nombre(nombre), descripcion(descripcion), materia(materia), fecha(fecha), estado(estado), anterior(NULL), siguiente(NULL)
    {
    }
    Nodo *getSiguiente()
    {
        return siguiente;
    }
    Nodo *getAtras()
    {
        return anterior;
    }
    string getCarnet() const
    {
        return carnet;
    }

    string getNombre()
    {
        return nombre;
    }

    string getDescripcion() const
    {
        return descripcion;
    }
    string getMateria() const
    {
        return materia;
    }
    string getFecha() const
    {
        return fecha;
    }
    string getEstado() const
    {
        return estado;
    }

    void setCarnet(string carnet)
    {
        carnet = carnet;
    }

    void setNombre(string nombre)
    {
        nombre = nombre;
    }

    void setDescripcion(string descripcion)
    {
        descripcion = descripcion;
    }
    void setMateria(string materia)
    {
        materia = materia;
    }
    void setFecha(string fecha)
    {
        fecha = fecha;
    }
    void setEstado(string estado)
    {
        estado = estado;
    }
    void setSiguiente(Nodo *siguiente)
    {
        siguiente = siguiente;
    }
    void setAtras(Nodo *atras)
    {
        atras = atras;
    }
};