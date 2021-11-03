#include<iostream>
#include<string>
using namespace std;
int main() {
	// game vars
	int room = 1;
  string input;
	bool dead = false;
	bool win = false;

  string inventory[8];
  for (int i = i; i < 8; i++){
    inventory[i] = "[EMPTY]";
  }

	cout << "You don't know where you are. All you can tell is that there's a bright white LIGHT above you, \nand that the air hums with MACHINERY." << endl;
  cout<< "You hear a man's VOICE come from speakers above: " << endl;
	cout << "Welcome, valued subject, to the Institute For Research On Souls And The Ethereal." << endl << endl;

	do {   // game loop
		if (dead) {
			cout << "hey, you shouldn't be seeing this yet!" << endl;
		}

		if (win) {
			cout << "hey, you shouldn't be seeing this yet!" << endl;
		}

    if(input.compare("i") == 0) {
      cout << "Current inventory is:\n\n";
      for(int i = 0; i < 8; i++) {
        cout << inventory[i] << endl;
      }
      cout << endl;
    }

		switch (room) {
		case 1:
      if(inventory[0].compare("PEN") != 0) {
			  cout << "You're in what seems to be a WAITING ROOM. Other than the PEN on the nearby desk, \nthe room is fully barren. There's an open door to your NORTH." << endl;
        cout << endl;
        getline(cin, input);
        if(input.compare("TAKE PEN") == 0) {
          inventory[0] = "PEN";
          cout << "\nWithout asking for permission, you gave in to greed took the PEN." << endl;
        }
      }
      else {
        cout << "You're in what seems to be a WAITING ROOM. Without a PEN on the nearby desk, \nthe room is fully barren. There's an open door to your NORTH." << endl;
        cout << endl;
        getline(cin, input);
      }
			if (input == "N") {
				room = 2;
      }
			break;
		case 2:
			cout << "room two placeholder text" << endl;
			cin >> input;
			if (input == "S")
				room = 11;
			else if (input == "E")
				room = 3;
			else if (input == "W")
				room = 4;
			break;
		case 3:
			cout << "room three placeholder text" << endl;
			cin >> input;
			if (input == "W")
				room = 2;
			break;
		case 4:
			cout << "room four placeholder text" << endl;
			cin >> input;
			if (input == "N")
				room = 5;
			else if (input == "E")
				room = 2;
			break;
		case 5:
			cout << "room five placeholder text" << endl;
			cin >> input;
			if (input == "S")
				room = 4;
			break;
		case 6:

		case 7:

		case 8:

		case 9:

		case 10:

		case 11:
			cout << "Filled with regret, you tried to go BACK. That's not an option. Your choices matter.\nThat is what it means to possess a SOUL." << endl;
			cout << endl;
			room = 2;
		}

		cout << endl;
	} while (input != "q");
}
