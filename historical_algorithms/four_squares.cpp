#include <iostream>
#include <cmath>
#include "set"
#include "windows.h"

//#include "stdafx.h"

using namespace std;

#define LL long long

const int m = 6, n = 6;

//Knowing the key of 4 squares
// (3 are obtained from one according to the rules described below),
// decrypting the message

void print(char arr[n][m]) {
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << arr[i][j]<<' ';
        }
        cout << endl;
    }
}

int main() {

    setlocale(LC_ALL, "Russian");
    //cout << 'А';

        char NTL[6][6]={{'Г','Д','Е','Ж','З','И'},
            {'Й','К','Л','М','Н','О'},
            {'П','Р','С','Т','У','Ф'},
            {'Х','Ц','Ч','Ш','Щ','Ъ'},
            {'Ы','Ь','Э','Ю','Я',' '},
            {',','.','?','А','Б','В'}
        };
        char NTR[6][6];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                NTR[i][j] = NTL[(i + 1) % 6][(j + 1) % 6];
            }
        }


        char NBL[6][6];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                NBL[i][j] = NTL[(i + 4) % 6][(j + 4) % 6];
            }
        }


        char NBR[6][6];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                NBR[i][j] = NTL[(i + 5) % 6][(j + 5) % 6];
            }
        }

        const string str = "З?ЩВКББТНЙШЦБМРДРГЙОДЪ";
        cout << "Original:\n" << str << endl;

        cout << "Top left" << endl;
        print((char[n][m])NTL);
        cout << "Top right:"<<endl;
        print((char[n][m])NTR);
        cout <<"Bottom left"<< endl;
        print((char[n][m])NBL);
        cout <<"Bottom right"<< endl;
        print((char[n][m])NBR);
        cout << endl;

        
        string ans = "";

        int I = 0, J = 0;
        for (int i = 0; i < str.length(); i++) {
            bool T = true;
            if (i % 2 == 0) {
                for (int j = 0; j < n&& T; j ++) {
                    for (int k = 0; k < m; k++) {
                        if (str[i] == NTR[j][k]) {
                            I = j;
                            J = k;
                            T = false;
                            break;
                        }
                    }
                }
            }
            else {
                for (int j = 0; j < n&& T; j ++) {
                    for (int k = 0; k < m; k++) {
                        if (str[i] == NBL[j][k]) {
                            ans += NTL[I][k];
                            ans += NBR[j][J];
                            T = false;
                            break;
                        }
                    }
                }
            }
        }
        cout <<"Answer:\n"<< ans;
        //print(N);

    return 0;
}

//БЕРЕГИ ЧЕСТЬ СМОЛОДУ.