#include <iostream> 
#include<bits/stdc++.h> 
using namespace std; 
typedef struct{ 
int profit; 
int weight; 
float ratio; 
}Item; 
 
void data(Item items[],int &n){ 
cout<< "Enter the number of items : "; 
cin>> n; 
cout<<endl; 
 
for(int i=0; i<n; i++){ 
cout<< "Enter the I" <<i+1<< " item's Weight : "; 
cin>> items[i].weight; 
cout<<"Enter the I"<< i+1 <<" item's Profit : "; 
cin>> items[i].profit; 
items[i].ratio = (float)items[i].profit / items[i].weight; 
cout<<endl; 
} 
} 
 
void display(Item items[],int &n){ 
int i; 
cout<< endl<<"Weight : "; 
for(i=0; i<n; i++){ 
cout<< items[i].weight <<"\t"; 
} 
cout<<endl<<"Profit : "; 
for(i=0; i<n; i++){ 
cout<< items[i].profit <<"\t"; 
} 
cout<<endl; 
} 
bool compare(Item i1, Item i2) { 
return (i1.ratio > i2.ratio); 
}
float knapsack(Item items[],int n, int W){ 
float totalWeight = 0; 
float totalProfit = 0; 
sort(items,items+n,compare); 
 
for(int i=0;i<n;i++){ 
if(totalWeight + items[i].weight <= W){ 
totalProfit += items[i].profit; 
totalWeight += items[i].weight; 
} 
else{ 
int wt = W - totalWeight; 
totalProfit += (wt * items[i].ratio); 
totalWeight += wt; 
break; 
} 
} 
cout <<endl<< "Total weight in bag : " << totalWeight<<endl; 
return totalProfit; 
} 
 
int main(){ 
int n,W; 
Item items[100]; 
data(items, n); 
cout <<endl<< "Entered data : "; 
display(items,n); 
cout<< endl<< "Enter the maximum size of KnapSack : "; 
cin>> W; 
float maxProfit = knapsack(items,n,W); 
cout << endl << "Max value for "<< W <<" weight is "<< maxProfit; 
return 0; 
}