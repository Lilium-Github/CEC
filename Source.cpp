#include<iostream>
using namespace std;
int main() {
	// game vars
	int room = 1;
	char input;
	bool dead = false;
	bool win = false;

	cout << "You don't know where you are. All you know is there's a bright white light above you, \nand that the air hums with machinery." << endl;
	cout << "Welcome, valued subject, to the Institute For Research On Souls And The Ethereal." << endl << endl;

	do {   // game loop
		if (dead) {
			cout << "hey, you shouldn't be seeing this yet!" << endl;
		}

		if (win) {
			cout << "hey, you shouldn't be seeing this yet!" << endl;
		}

		switch (room) {
		case 1:
			cout << "room one placeholder text" << endl;
			cin >> input;
			if (input == 'N')
				room = 2;
			else
				cout << "not an option" << endl;
			break;
		case 2:
			cout << "room two placeholder text" << endl;
			cin >> input;
			if (input == 'S')
				room = 11;
			else if (input == 'E')
				room = 3;
			else if (input == 'W')
				room = 4;
			else
				cout << "not an option" << endl;
			break;
		case 3:
			cout << "room three placeholder text" << endl;
			cin >> input;
			if (input == 'W')
				room = 2;
			else
				cout << "not an option" << endl;
			break;
		case 4:
			cout << "room four placeholder text" << endl;
			cin >> input;
			if (input == 'N')
				room = 5;
			else if (input == 'E')
				room = 2;
			else
				cout << "not an option" << endl;
			break;
		case 5:
			cout << "room five placeholder text" << endl;
			cin >> input;
			if (input == 'S')
				room = 4;
			else
				cout << "not an option" << endl;
			break;
		case 6:

		case 7:

		case 8:

		case 9:

		case 10:

		case 11:
			cout << "secret room placeholder text" << endl;
			cout << endl;
			room = 2;
		}

		cout << endl;
	} while (input != 'q');
}