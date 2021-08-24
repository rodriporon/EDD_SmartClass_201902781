#include <iostream>
#include <cstring>
#include <regex>

using namespace std;

bool isDPI(string DPI)
{
    if (DPI.length() == 13)
    {
        return true;
    }
    return false;
}

bool isCarnet(string carnet)
{
    if (carnet.length() == 9)
    {
        return true;
    }
    return false;
}

bool isCorreo(string correo)
{
    const regex remail("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(com|es|org))");

    if (regex_match(correo, remail))
    {
        return true;
    }
    return false;
    
}

bool isHora(string hora)
{
    if (stoi(hora) >= 8 && stoi(hora) <= 16)
    {
        return true;
    }
    return false;
    
}
