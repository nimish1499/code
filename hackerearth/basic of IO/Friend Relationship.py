Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #include <iostream>

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
