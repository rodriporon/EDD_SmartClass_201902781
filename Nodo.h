#ifndef _NODO_H
#define _NODO_H
class Node
{
    protected:
        int value;
        Node* next;

    public:
        Node(int v) : value(v), next(0) { }

        Node(int r, Node* n) : value(r), next(n) { }

        int getValue() 
        {
            return value;
        }

        Node* getNext()
        {
            return next;
        }

        void setNext(Node* n)
        {
            next = n;
        }
};

#endif