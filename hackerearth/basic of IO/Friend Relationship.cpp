#include <iostream>

using namespace std;

int main() {
int t,n;
cin>>t;
for(int i=0;i<t;i++)
{
cin>>n;
int a=1,b=n-1;
while(a!=n+1 && b!=-1)
{
for(int k=0;k<a;k++)
{
cout<<"*";
}
for(int k=0;k<b;k++)
{
cout<<"#";
}
for(int k=0;k<b;k++)
{
cout<<"#";
}
for(int k=0;k<a;k++)
{
cout<<"*";
}
cout<<endl;
a++;
b--;
}
cout<<endl;
}
}
