#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
bool palindrome(int num);
int main() {
	int input;
	do {
		cout << "Number:" << endl;
		cin >> input;
		if (palindrome(input)) {
			cout << "This is a palindrome!" << endl;
		}
		else {
			cout << "Not a palindrome." << endl;
		}
	} while (input != 0);
}
bool palindrome(int num) {
	string list = to_string(num);
	string backwards = list;
	reverse(backwards.begin(), backwards.end());
	if (backwards.compare(list) == 0) {
		return true;
	}
	else return false;
}
