#include<bits/stdc++.h>
using namespace std; 
void print(int n){
	if(n==1){
		cout<<n<<" ";
		return ;
}
	print(n-1);
	cout<<n<<" ";
}



 void print_n_to_1(int n)
 {
 	if(n==1){
 		cout<<n<<" ";
 		return;
	 }
	 cout<<n<<" ";
	 print_n_to_1(n-1);
 }
 
 
 
 
int main( )
 {
 	int n;cin>>n;
 	print(n);
 	cout<<endl;
 	print_n_to_1(n);
 }

