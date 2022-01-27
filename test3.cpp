#include <iostream>
using namespace std;

void counter(int);

int main() {
	cout << "\nPART 1 ####################################################" << endl;

	int month;

	cout << "What month is it? (in numbers, please)" << endl;
	cin >> month;

	switch (month) {
	case 1:
		cout << "That month has 31 days." << endl;
		break;
	case 2:
		cout << "That month has 28/29 days." << endl;
		break;
	case 3:
		cout << "That month has 31 days." << endl;
		break;
	case 4:
		cout << "That month has 30 days." << endl;
		break;
	case 5:
		cout << "That month has 31 days." << endl;
		break;
	case 6:
		cout << "That month has 30 days." << endl;
		break;
	case 7:
		cout << "That month has 31 days." << endl;
		break;
	case 8:
		cout << "That month has 31 days." << endl;
		break;
	case 9:
		cout << "That month has 30 days." << endl;
		break;
	case 10:
		cout << "That month has 31 days." << endl;
		break;
	case 11:
		cout << "That month has 30 days." << endl;
		break;
	case 12:
		cout << "That month has 31 days." << endl;
		break;
	}

	cout << "\nPART 2 ####################################################" << endl;
	int room = 1;
	char input;
	bool quit = false;

	do {
		cout << endl;
		switch (room) {
		case 1:
			cout << "You are in room 1. Exits are North, East, or West." << endl;
			cin >> input;

			if (input == 'n')
				room = 2;
			else if (input == 'e')
				room = 4;
			else if (input == 'w')
				room = 3;
			else cout << "I didn't quite get that.\n";

			break;
		case 2:
			cout << "You are in room 2. Exits are South." << endl;
			cin >> input;

			if (input == 's')
				room = 1;
			else cout << "I didn't quite get that.\n";

			break;
		case 3:
			cout << "You are in room 3. Exits are East." << endl;
			cin >> input;

			if (input == 'e')
				room = 1;
			else cout << "I didn't quite get that.\n";

			break;
		case 4:
			cout << "You are in room 4. Exits are South or West." << endl;
			cin >> input;

			if (input == 's')
				room = 5;
			else if (input == 'w')
				room = 1;
			else cout << "I didn't quite get that.\n";

			break;
		case 5:
			cout << "You are in room 5. Exits are North. Type q to move on to the third section of Lily's exam." << endl;
			cin >> input;

			if (input == 'n')
				room = 4;
			else if (input == 'q')
				quit = true;
			else cout << "I didn't quite get that.\n";

			break;
		}


	} while (quit == false);

	cout << "\nPART 3 ####################################################" << endl;

	int userIn;

	do {
		cout << "Enter a number, 0 to quit: ";
		cin >> userIn;
		cout << endl;
		counter(userIn);
		cout << endl;
	} while (userIn != 0);
}

void counter(int n) {
	if (n > 0) {
		cout << n << " ";
		counter(n - 1);
	}

	if (n != 0) 
		cout << n << " ";
}
