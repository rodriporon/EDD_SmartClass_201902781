#include <iostream>

using namespace std;

class NodoD
{
protected:
    int index;
    string mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado;

    NodoD *siguiente;
    NodoD *anterior;

public:
    NodoD(int index, string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado) : index(index), mes(mes), dia(dia), hora(hora), carnet(carnet), nombre(nombre), descripcion(descripcion), materia(materia), fecha(fecha), estado(estado), siguiente(NULL), anterior(NULL)
    {
    }

    // getters

    int getIndex() const
    {
        return index;
    }
    string getMes() const
    {
        return mes;
    }
    string getDia() const
    {
        return dia;
    }
    string getHora() const
    {
        return hora;
    }
    string getCarnet() const
    {
        return carnet;
    }

    string getNombre() const
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

    NodoD *siguienteNodo()
    {
        return siguiente;
    }

    NodoD *anteriorNodo()
    {
        return anterior;
    }

    // setters

    void setSiguiente(NodoD *s)
    {
        siguiente = s;
    }

    void setAnterior(NodoD *a)
    {
        anterior = a;
    }
    void setIndex(int i)
    {
        index = i;
    }
    void setMes(string m)
    {
        mes = m;
    }
    void setDia(string d)
    {
        dia = d;
    }
    void setHora(string h)
    {
        hora = h;
    }
    void setCarnet(string c)
    {
        carnet = c;
    }

    void setNombre(string n)
    {
        nombre = n;
    }

    void setDescripcion(string d)
    {
        descripcion = d;
    }

    void setMateria(string m)
    {
        materia = m;
    }

    void setFecha(string f)
    {
        fecha = f;
    }

    void setEstado(string e)
    {
        estado = e;
    }
};