#include <iostream>
#include <sstream>

using namespace std;

int getIndexMonth(string month)
{
    switch (stoi(month))
    {
    case 7:
        return 0;
        break;

    case 8:
        return 1;
        break;

    case 9:
        return 2;
        break;

    case 10:
        return 3;
        break;

    case 11:
        return 4;
        break;

    default:
        return -1;
        break;
    }
}

int getIndexDay(string day)
{
    switch (stoi(day))
    {
    case 1:
        return 0;
        break;

    case 2:
        return 1;
        break;

    case 3:
        return 2;
        break;

    case 4:
        return 3;
        break;

    case 5:
        return 4;
        break;

    case 6:
        return 5;
        break;

    case 7:
        return 6;
        break;

    case 8:
        return 7;
        break;

    case 9:
        return 8;
        break;

    case 10:
        return 9;
        break;

    case 11:
        return 10;
        break;

    case 12:
        return 11;
        break;

    case 13:
        return 12;
        break;

    case 14:
        return 13;
        break;

    case 15:
        return 14;
        break;

    case 16:
        return 15;
        break;

    case 17:
        return 16;
        break;

    case 18:
        return 17;
        break;

    case 19:
        return 18;
        break;

    case 20:
        return 19;
        break;

    case 21:
        return 20;
        break;

    case 22:
        return 21;
        break;

    case 23:
        return 22;
        break;

    case 24:
        return 23;
        break;

    case 25:
        return 24;
        break;
    case 26:
        return 25;
        break;
    case 27:
        return 26;
        break;
    case 28:
        return 27;
        break;
    case 29:
        return 28;
        break;

    case 30:
        return 29;
        break;

    default:
        return -1;
        break;
    }
}

int getIndexHour(string hour)
{
    switch (stoi(hour))
    {
    case 8:
        return 0;
        break;

    case 9:
        return 1;
        break;
    case 10:
        return 2;
        break;
    case 11:
        return 3;
        break;
    case 12:
        return 4;
        break;
    case 13:
        return 5;
        break;
    case 14:
        return 6;
        break;
    case 15:
        return 7;
        break;
    case 16:
        return 8;
        break;

    default:
        return -1;
        break;
    }
}