#include <iostream>

// 168. switch-break
// int main(){
//     for(int i=2;i<10;i++){
//         switch(i){
//             case 3:
//             case 7:
//                 for(int j=1;j<10;j++){
//                     printf("%d * %d = %d\n", i, j, i*j);
//                 }
//                 break;
//             default:
//                 continue;
//         }
//     }
//     return 0;
// }


// 172. 버블정렬
// void sort(int a[]){
//     int n=5;
//     for(int i =0;i<n-1;i++){
//         int min = i;

//         for(int j = i+1;j<n;j++){
//             if(a[j] < a[min]){
//                 min = j;
//             }
//         }

//         if(min != i){
//             int tmp = a[i];
//             a[i] = a[min];
//             a[min] = tmp;
//         }
//     }
// }

// int main(){
//     int a[] = {7,4,5,1,3};
//     sort(a);

//     for(int i=0;i<5;i++){
//         printf("%d ", a[i]);

//     }
//     return 0;
// }

// void sort(int a[]){
//     int n=5;

//     for(int i=1;i<n;i++){
//         int key = a[i];
//         int j = i-1;

//         while(j >=0 && a[j] > key){
//             a[j+1]=a[j];
//             j--;
//         }
//         a[j+1] = key;

//         for(int x=0;x<5;x++){
//             printf("%d ", a[x]);
//         }
//         printf("\n\n");
//     }
// }

// int main(){
//     // int a[] = {7,4,5,1,3};
//     // sort(a);
//     float a = 3.14;
//     printf("%f", a);
//     return 0;
// }


int main(){
  int *arr[3];
  int a = 12, b = 24, c = 36;
  arr[0] = &a;
  arr[1] = &b;
  arr[2] = &c;
 
//   printf("%d\n", *arr[1] + **arr + 1);
    printf("%d\n", arr[0]);
  printf("%d", **arr+1);
}