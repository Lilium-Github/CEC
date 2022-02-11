#include <vector>
#include<iostream>
#include <algorithm>

using namespace std;

float CircleArea(float radius);

int main() {
	cout << "Please Input Radius:" << endl;
	float input;
	cin >> input;

	cout << "Area: " << CircleArea(input);

	cout << "\n\n\n\n\n\n\n\n\n" << endl;

	vector <int> lilyVector;
	int userInput;

	do {
		cout << "Give me a number, or 0 to finish" << endl;

		cin >> userInput;

		lilyVector.push_back(userInput);
	} while (userInput != 0);

	sort(lilyVector.begin(), lilyVector.end());

	bool fiveFound = false;

	for (int i = 0; i < lilyVector.size(); i++) {
		cout << lilyVector[i] << endl;
		if (lilyVector[i] == 5) {
			fiveFound = true;
		}
	}

	if (fiveFound) cout << "This vector contains a 5." << endl;

	for (int i = 0; i < 3; i++) {
		lilyVector.pop_back();
		cout << "popping... \n";
	}

	for (int i = 0; i < lilyVector.size(); i++) {
		cout << lilyVector[i] << endl;
	}

}

float CircleArea(float radius) {
	float area = (radius * radius) * 3.14159;
	return area;
}
