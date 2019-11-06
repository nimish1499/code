#include<iostream>
using namespace std;
int max1=100; int top=-1;
 void push(int a[],int);
 void display(int a[]);
 void pop(int[]);
 int main()


 {

     int ar[100];
     int x;

   cout<<" element to push";
   cin>>x;
    while(x!=-1){   push(ar,x);
    cin>>x;}
      display(ar);
      pop(ar);
      display( ar);
 }
  void push( int ar[],int x){

if(top==(max1-1))
   {

     cout<<"overflow";}
     else  top=top+1;
    // cout<<top<<" ";
     ar[top]=x;

    }
    void display(int ar[])
    {
         for( int i=0; i<=top;i++)
         {
              cout<<ar[i]<<" ";

         }
    }void pop( int ar[]){
    if(top==-1)
        cout<<"empty";
    else
     {cout<<"popo element"<<ar[top]<<"\n";

        top=top-1;}

}
