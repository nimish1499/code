#include <stdio.h>

int main()
{
int l,w[1000],h[1000],n;
scanf("%d",&l);
scanf("%d",&n);
for(int i=0;i<n;i++)
{
scanf("%d %d",&w[i],&h[i]);
}
for(int i=0;i<n;i++)
{
if((w[i]>l && h[i]>l && w[i]!=h[i]) || (w[i]>l && h[i]==l) || (w[i]==l && h[i]>l))
printf("CROP IT\n");
else if(w[i]<l || h[i]<l || (w[i]>l && h[i]<l) || (w[i]<l && h[i]>l))
printf("UPLOAD ANOTHER\n");
else if((w[i]==l && h[i]==l) || w[i]==h[i] || (w[i]>l && h[i] >l && w[i]==h[i]))
printf("ACCEPTED\n");
}
return 0;
}
