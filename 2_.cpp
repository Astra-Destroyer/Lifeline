#include <bits/stdc++.h> 
#include <chrono> 
 
using namespace std; 
using namespace std::chrono; 
 
void swap(int* a, int* b) { 
int t = *a; 
*a = *b; 
*b = t; 
} 
 
int partition(int a[], int beg, int end) { 
int pivot = a[end]; 
int i = beg - 1; 
 
for (int j = beg; j <= end - 1; j++) { 
if (a[j] < pivot) { 
i++; 
swap(&a[i], &a[j]); 
} 
} 
swap(&a[i + 1], &a[end]); 
return i + 1; 
} 
 
void quickSort(int a[], int beg, int end) { 
if (beg < end) { 
int piv = partition(a, beg, end); 
quickSort(a, beg, piv - 1); 
quickSort(a, piv + 1, end); 
} 
} 
 
void printArr(int a[], int n) { 
for (int i = 0; i < n; i++) { 
cout << a[i] << " "; 
} 
}
int main() { 
int arr[30]; 
int n = sizeof(arr) / sizeof(arr[0]); 
 
cout << "Enter the size of array: "; 
cin >> n; 
 
for (int i = 0; i < n; i++) { 
arr[i] = rand() % 10000; 
} 
 
cout << "\nUnsorted Array: "; 
printArr(arr, n); 
 
auto start = high_resolution_clock::now(); 
quickSort(arr, 0, n - 1); 
auto stop = high_resolution_clock::now(); 
chrono::duration<double, nano> duration = stop - start; 
 
cout << "\nSorted Array: "; 
printArr(arr, n); 
cout << "\nTime taken by QuickSort: " << duration.count() << " nanoseconds" << endl; 
return 0; 
}
