#include <iostream>
using namespace std;

unsigned int hammingweight(unsigned int n)
{
    unsigned int c =0;
    while(n)
    {
        c+=n & 1;
        n >>=1;
    }
    return c;
}

int main()
{
    int t;//the number of testcases
    cin >> t;
    while(t-- >0)
    {
        unsigned int n;
        cin >> n;
        cout << hammingweight(n)<<endl;
    }
    return 0;
}