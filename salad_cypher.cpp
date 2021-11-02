#include <iostream>

using namespace std;

int main() {
  cout << "please input plaintext to be encoded (no spaces please!):\n";
  string plaintext;
  cin >> plaintext;
  int len  = plaintext.size();

  cout << "\nplease input the amount you'd like to shift your plaintext:\n";
  int key;
  cin >> key;

  cout << "\nyour encoded text is: \n\n";
  for(int i = 0; i < len; i++) {
    plaintext[i] = toupper(plaintext[i]);
    if(plaintext[i] >= 65 && plaintext[i] <= 90) {
      plaintext[i] += (key % 26);
      while (plaintext[i] > 90) {
        plaintext[i] -= 26;
      }
    }
    cout << static_cast<char>(plaintext[i]);
  }
  
  cout << "\n";
} 
