#include <iostream>
#include <cmath>
#include "set"
#include "windows.h"
#include <map>

//#include "stdafx.h"

using namespace std;

#define LL long long

int main() {

    setlocale(LC_ALL, "Russian");

    const int n = 33;

        char A[n]={'А','Б','В','Г','Д','Е',
            'Ж','З','И','Й','К','Л',
            'М','Н','О','П','Р','С',
            'Т','У','Ф','Х','Ц','Ч',
            'Ш','Щ','Ъ','Ы','Ь','Э',
            'Ю','Я','_'};
        map<int,char> NA;
        map<int, char> AN;
        for(int i=0; i<33;i++){
            NA[i] = A[i];
            AN[A[i]] = i;
        }
        int N[n] = {17,11,14,13};
        string str = "ЮРНЯАЩСНЪЭУМТРЩЗЕКПТАРХМЯПУЛЮЖУМЮРНЯАРП_ЪЭУМУПЮ_ФКАМЯЬЦЪЛКЭЭЩТЫНЮЖУМЩКРМВУВ_ОКЮТЫЮНОАЩЯНПКЩХБЭЬЧРШУМУРЮИВРНГВЩНПСЧЦМ_ЩЩЫЧРЫМЩЬ_ЫЫ";

        //cin >> str;
        //cout << str;
        //Ключ-Слово: СЛОН
        string ans = "";
        for (int i = 0; i < str.length(); i++) {
            //cout << (int)str[i]<<" ";
            if((AN[str[i]] - N[i % 4])>=0)
                ans+= NA[(AN[str[i]] - N[i % 4]) % n];
            else
                ans += NA[(AN[str[i]] - N[i % 4]+n) % n];
        }
        cout << ans;
        //17,11,14,13
    return 0;
}