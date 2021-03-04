//https://codeforces.com/problemset/problem/456/A

#include <iostream>
using namespace std;

int main(){
  long int n,price,quality,one=0,two=0;
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>price>>quality;
    if(price<quality)one+=1;
    if(price>quality)two+=1;
  }
  if(one>0&&two>0)cout<<"Happy Alex";
  else cout<<"Poor Alex";
  return 0;
}
