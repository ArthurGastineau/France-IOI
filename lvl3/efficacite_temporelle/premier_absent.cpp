/*
    Name : Premier absent
    Author : Arthur G
    Date : 18 Aug 2021
*/

#include<bits/stdc++.h>

using namespace std;

int main()
{
    set<int> data;
    int P, N, eleve, min = 1;
    scanf("%d %d", &N, &P);
    for (int i = 1; i <= P; i++)
    {
        scanf("%d", &eleve);
        data.insert(eleve);
        if (i == N)
            printf("-1\n");
        else
        {
            if (min == eleve)
                for (set<int>::iterator it1 = data.begin(); it1 != data.end(); it1++)
                {
                    if (min != *it1)
                        break;
                    data.erase(min);
                    min++;
                }
            printf("%d\n", min);
        }
    }
    return 0;
}
