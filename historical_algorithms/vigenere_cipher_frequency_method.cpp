#include <iostream>
#include <cmath>
#include "set"
#include "windows.h"
#include <map>
#include <vector>
#include <set>
//#include "stdafx.h"

using namespace std;

#define LL long long

//Нахождение ключ-слова для сообщения частотным методом


int main() {

    setlocale(LC_ALL, "Russian");

    const int n = 35;

    char A[n] = {
        'А','Б','В','Г','Д','Е',
        'Ж','З','И','Й','К','Л',
        'М','Н','О','П','Р','С',
        'Т','У','Ф','Х','Ц','Ч',
        'Ш','Щ','Ъ','Ы','Ь','Э',
        'Ю','Я','_',',','.'};
    map<int, char> AN;
    for (int i = 0; i < n; i++) {
        AN[A[i]] = i;
    }
    string str = "ОАЫЦОЮЖ.ХЮЕООАКЦЗАТОЕЫХЯУЙРЮСДЖУЮУСЮИЬЖЩА_РФОЪНЙАНБ..ТСООЩНЦМЫЦСАИОЪАМЧЖОГЪКБЫСОПИООНЮРСОЙЪКБЫ_АСЫЧЮЛЫЦЦФОЫОЪЮЪАЛСЬОРЮЪОФЮХЩШЬЫСНЫСШДАМС.ЫЛНКЕСГАКЬАБЫФЦХГЫОФ_ЧТС.ЦЙМЫЪАЛРИ";
 

    int m = 10;
    map<int, set<pair<pair<int,string>,int>>> Gramms;
    for (int  i = 0; i < str.length(); i++)
    {
        for (int j = i + 2; j < str.length(); j++)
        {
            for (int k = 2; k < m; k++)
            {
                if (str.substr(i, k) == str.substr(j, k) && i + k < j && j + k < str.length()) {

                    Gramms[k].insert({{ i, str.substr(i, k) }, j});
                }
                else
                {
                    break;
                }
            }
            //cout << str.substr(i, i + 2) << " " << str.substr(j, j + 2)<<endl;
        }
    }

    for (auto i = Gramms.begin(); i !=Gramms.end(); i++)
    {
        cout << i->first<<"-gramm: \n";
        for (auto j = i->second.begin(); j != i->second.end(); j++)
        {
            //Где встретились в первый и во второй разы, сама m-грамма и разница между индексами.
            cout << j->first.first<<" "<< j->second<<" "<<j->first.second <<" "<< j->second-j->first.first<< "\n";
        }
        cout << "\n";
    }

    //Предполагается исходя из НОД разницы между словами, что длина ключ-слова=4

    const int M = 4;
    
    vector<string> T;
    T.resize(M);
    for (int  i = 0; i < str.length(); i++)
    {
        T[i % M] += str[i];
    }

    for (int i = 0; i < M; i++)
    {
        cout << T[i] << endl;
    }

    vector<map<char, int>>count_of_letters;
    count_of_letters.resize(M);

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < T[i].length(); j++)
        {
            count_of_letters[i][T[i][j]]++;
        }
    }

    for (int i = 0; i < M; i++)
    {
        cout << i+1 << "-ая подстрока:\n";
        for (auto j = count_of_letters[i].begin(); j !=count_of_letters[i].end(); j++)
        {
            cout << j->first << " " << j->second<<endl;
        }
        cout << endl;
    }

    //Например, во второй подстроке "Ы" встречается 10 раз. Можно сделать предположение, что в эту букву перешёл пробел. Тогда обратным действием: 
    // "Ы"=27 (с нуля счёт)
    //32+x=27=> x=-5=>x=30=> x=Ю
    //27-х=32=>x=-5=>x=30

    //1-ая: "О"=14,
    //x+32=14=> x=-18=>x=17>x=C
    //x+18=14=> x=-4=>x=31

    //4-ая: "О"=14 x=С

    //3-я:
    //x+32=26=>x=-6=>x=29=>x=' ' -----
    //x+32=17=>x=-15=20=>x='Ф'

    //По факту, был просто перебор слов из 4-х букв со 2-ой буквой "Ю"
    string key = "ГЮЙС";
    int N[M] = {AN[key[0]],AN[key[1]],AN[key[2]],AN[key[3]]};

    string ans = "";
    cout << endl;
    for (int i = 0; i < str.length(); i++) {
        //cout << (int)str[i]<<" ";
        if ((AN[str[i]] - N[i % M]) >= 0)
            ans += A[(AN[str[i]] - N[i % M]) % n];
        else
            ans += A[(AN[str[i]] - N[i % M] + n) % n];
    }
    cout << ans<<endl;
    return 0;
}