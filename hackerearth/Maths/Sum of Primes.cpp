#include<bits/stdc++.h>
using namespace std;
#define n 1000000
int main()
{
int t;
scanf("%d",&t);
long long int a[n+1];
for(int i=2;i<n;i++)
a[i]=1;
for(int i=2;i*i<=n;i++)
{
if(a[i]==1)
{
for(int j=2*i;j<=n;j=j+i)
{
a[j]=0;
}
}
}
a[1]=0;
for(int i=2;i<=n;i++)
{
if(a[i]==1)
a[i]=i+a[i-1];
else
a[i]=a[i-1];
}
while(t--)
{
int l,r;
scanf("%d %d",&l,&r);
printf("%lld\n",a[r]-a[l-1]);
}
}
