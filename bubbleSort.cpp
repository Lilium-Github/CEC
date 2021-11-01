#include <iostream>
#include <time.h>
using namespace std;

int main() {

    srand(time(NULL));
  
    int arr[100];

    for (int i = 0; i < 10; i++) {
      arr[i] = rand() % 100;
      cout << arr[i] << endl;
    }

    cout << "\n\n\n\n\n";

    bool sorted;

    do {
      sorted = true;
      for (int i = 0; i < 9; i++) {
        if (arr[i] > arr[i+1]) {

          sorted = false;

          int swap = arr[i];
          arr[i] = arr[i+1];
          arr[i+1] = swap;
          
        }
      }

    }
    while(sorted == false);

    for (int i = 0; i < 10; i++) {
      cout << arr[i] << endl;
    }
} 
