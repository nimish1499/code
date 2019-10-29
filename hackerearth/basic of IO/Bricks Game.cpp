#include <bits/stdc++.h>
using namespace std;
int main()
{
int n,i=1;
cin>>n;
while(n>0)
{
n = n-i;
if(n<=0)
{
cout<<"Patlu"<<endl;
break;
}
n = n-(2*i);
if(n<=0)
{
cout<<endl<<"Motu";
break;
}
i++;
}
return 0;
}
