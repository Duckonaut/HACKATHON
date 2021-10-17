#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;

int main()
{
    string konie[4];
    int cant_attack = 0;
    cin >> konie[0] >> konie[1];
    cin >> konie[2] >> konie[3];
    for (int i=0; i < 1; ++i)
    {
        if (((konie[i][0] < 65 || konie[i][0] > 72) && (konie[i][0] < 97 || konie[i][0] > 104)) ||
        konie[i][1] > 56 || konie[i][1] < 49 || konie[i].size() != 2)
        {
            cout << "BLAD";
            return 0;
        }
    }
    for (int i=0; i < 2; ++i)
    {
        for (int j=2; j<4; ++j)
        {
            if (konie[i][0] + 1 == konie[j][0] && konie[i][1] + 2 == konie[j][1]) {}
            else if (konie[i][0] + 2 == konie[j][0] && konie[i][1] + 1 == konie[j][1]) {}
            else if (konie[i][0] + 2 == konie[j][0] && konie[i][1] - 1 == konie[j][1]) {}
            else if (konie[i][0] + 1 == konie[j][0] && konie[i][1] - 2 == konie[j][1]) {}
            else if (konie[i][0] - 2 == konie[j][0] && konie[i][1] + 1 == konie[j][1]) {}
            else if (konie[i][0] - 1 == konie[j][0] && konie[i][1] + 2 == konie[j][1]) {}
            else if (konie[i][0] - 2 == konie[j][0] && konie[i][1] - 1 == konie[j][1]) {}
            else if (konie[i][0] - 1 == konie[j][0] && konie[i][1] - 2 == konie[j][1]) {}
            else
            {
                cant_attack++;
            }
        }
    }
    if (cant_attack == 4)
    {
        cout << "NIE";
    }
    else cout << "TAK";

    return 0;
}
