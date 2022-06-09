#include <iostream>
#include <cmath>
#include "set"
#include "windows.h"
#include <map>

//#include "stdafx.h"

using namespace std;

#define LL long long

// Decryption with a known key
int main() {

    setlocale(LC_ALL, "Russian");

    const int n = 36;

        char A[n]={'А','Б','В','Г','Д','Е',
            'Ж','З','И','Й','К','Л',
            'М','Н','О','П','Р','С',
            'Т','У','Ф','Х','Ц','Ч',
            'Ш','Щ','Ъ','Ы','Ь','Э',
            'Ю','Я',' ',',','.','?'};
        map<char,char> NA;
        int N[n] = { 28,13,27,31,21,12,26,30,20,11,4,25,18,29,14,32,19,33,10,35,3,9,1,22,5,15,34,36,2,23,6,16,24,7,17,8 };
        for (int i = 0; i < n; i++)
        {
            //NA[A[N[i]]-1] = A[i];
            NA[A[i]] = A[N[i]-1];
            char c = 0;
            //if(i!=n-1)
            //cin >> c;
        }

        string str = "ОЮШЩЕКЩСМЙ.ХЯЙЦСФЩЕОЩФЦЕЦЪСОЮШЩЕКЩСЯЕЦЙЦЕМПСЙЕЦ.ОЮРЪСМР.ЩЙЩТС ЮРА.ОЦШЭЦРЩТСЯЦЕЦСРФЮ.ШАОПСМСОЦШЯХМНГСМЩОЮРУ";
        //cin >> str;
        //cout << str;
        string ans = "";
        for (int i = 0; i < str.length(); i++) {
            ans += NA[str[i]];
        }
        cout << ans;
    return 0;
}

//НЕДОЛГО СКРИПКА ВОЛНОВАЛА, НЕДОЛГО ПЛАКАЛСЯ КЛАРНЕТ, СТРОКОЙ ЧЕТЫРНАДЦАТОЙ ПАЛА ТВЕРДЫНЯ С НАДПИСЬЮ СОНЕТ.