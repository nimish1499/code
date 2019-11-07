#include <iostream>
#include<math.h>
using namespace std;
int main() {
int t,c,s;
cin>>t;
while(t--){
int n ;
cin>>n;
c = 0 ;
s =sqrt(n);
for(int i = 1 ; i <= s ; i++){
if(n % i == 0)
{
c++;
if(i*i != n)
c++;
}
}

cout<<c<<endl;
}
return 0;
}
