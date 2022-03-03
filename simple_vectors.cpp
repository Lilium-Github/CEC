#include <iostream>
#include <vector>
#include <time.h>
#include <algorithm>
#include <stdlib.h>     /* srand, rand */

using namespace std;

int main() {
	srand(time(NULL));

	vector<int> vec;

	for (int i = 0; i < 20; i++) {
		vec.insert(vec.begin(), rand() % 100);
	}

	cout << "\n\nBASE\n\n";

	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << ", ";
	}

	sort(vec.begin(), vec.end());

	cout << "\n\nSORT\n\n";

	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << ", ";
	}

	random_shuffle(vec.begin(), vec.end());

	cout << "\n\nSHUFFLE\n\n";

	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << ", ";
	}


}
