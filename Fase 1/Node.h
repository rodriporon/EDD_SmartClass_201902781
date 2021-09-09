#include <iostream>
using namespace std;

class Node
{
    protected:
    int index;
    string carnet, nombre, descripcion, materia, fecha, estado;
    Node* siguiente;
    Node* atras;

    public:
    Node(int index, string carnet, string nombre, string descripcion, string materia, string fecha, string estado)
    : carnet(carnet), nombre(nombre), descripcion(descripcion), materia(materia), fecha(fecha), estado(estado), siguiente(NULL), atras(NULL)
    {}

    //getters

    Node* getSiguiente()
    {
        return siguiente;
    }
    Node* getAtras()
    {
        return atras;
    }
    string getCarnet()
    {
        return carnet;
    }
    string getNombre()
    {
        return nombre;
    }
    string getDescripcion()
    {
        return descripcion;
    }
    string getMateria()
    {
        return materia;
    }
    string getFecha()
    {
        return fecha;
    }
    string getEstado()
    {
        return estado;
    }
    int getIndex()
    {
        return index;
    }

    // setters

    void setSiguiente(Node* siguiente)
    {
        siguiente = siguiente;
    }
    void setAtras(Node* atras)
    {
        atras = atras;
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
    void setIndex(int index)
    {
        index = index;
    }
};