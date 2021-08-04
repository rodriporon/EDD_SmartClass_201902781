#include <iostream>

class NodoDoble
{
    protected:
        int value;
        NodoDoble* siguiente;
        NodoDoble* anterior;

    public:
        NodoDoble(int v)
        {
            value = v;
            siguiente = anterior = NULL;
        }

        int getValue() const
        {
            return value;
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