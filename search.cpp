#include <iostream>

using namespace std;

int main() {
  int location; //where we are in the list
	int found = 0;  //how many of the target item we've found

	int IDs[] = {234, 567, 321, 234, 789}; // init an array for testing
	location = (sizeof(IDs) / sizeof(int)) - 1; // set location to the last slot in the list

	int searchItem;
	cout << "Enter ID to search:" << endl;
	cin >> searchItem;

	while (location > 0) {
		if(IDs[location] == searchItem) {
			found++;
		}
		location++;
	}

	cout << "ID appears " << found << " times." << endl;
}
