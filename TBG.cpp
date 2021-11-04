#include<iostream>
#include<string>
using namespace std;


//inventory; slot 0 is for the pen, slot 1 is for the knife, slot 2 is for the glasses
// slot 3 is for the glyph
string inventory[] = {"[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]"};
int room = 1;

void shop(string name);



int main() {
	// game vars
  string input;
	bool dead = false;
	bool win = false;

  cout << "What is its excellency's's NAME?\n";
  string name;
  getline(cin, name);
  cout << "How excellent. Your VESSEL will soon be prepared. Thank you for your assistance." <<  endl << endl; 

	cout << "You don't know where you are. All you can tell is that there's a bright white LIGHT above you, and that the air hums with MACHINERY." << endl;
  cout<< "You hear a man's VOICE come from speakers above: " << endl;
	cout << "\"Welcome, valued subject, to the Institute For Research On Souls And The Ethereal.\"" << endl << endl;

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
			  cout << "You're in what seems to be a WAITING ROOM. Other than the PEN on the nearby desk, \nthe room is fully barren. There's an open door to your NORTH." << endl << endl;
        cout << endl;
        getline(cin, input);
        if(input.compare("TAKE PEN") == 0) {
          inventory[0] = "PEN";
          cout << "\nWithout asking for permission, you gave in to greed and took the PEN." << endl;
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
			cout << "A hallway with pearly white walls and a floor, golden carpet below your feet. You can \ngo SOUTH, EAST, or WEST." << endl;
      cout << "A grayed-out picture of a man with a goat's head hangs on the wall. The plaque under it shows his name is \n\"THE EXILED ONE.\"" << endl << endl;

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
			cout << "You're in a BROOM CLOSET. There's a sinking feeling that you're supposed to see this." << endl;
      cout << "EAST is the way out of the BROOM CLOSET. You hear another VOICE from the NORTH wall." << endl << endl;
			cin >> input;
			if (input == "N")
				room = 5;
			else if (input == "E")
				room = 2;
			break;
		case 5:
      shop(name);
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

void shop(string name) {
    cout << "You come across what appears to be a SHOP. A statue of THE EXILED ONE greets you. \nHis goat head does not move with his VOICE." << endl;
    cout << "\"Hello, " << name << " and welcome to my shop. Normally, she'd never enter this place... \nBut with your arrival, her situation has become far from normal.\"" << endl;

    string input;

    cout << "\"Let's see... I have a few things for you. A KNIFE, a pair of (broken) GLASSES. \nI could also inscribe a cursed GLYPH for you, but I'd need a PEN to sign the CONTRACT with...\"" << endl;
    cout << "\"Make your choice, excellency. That, or simply QUIT our little transaction.\"" << endl << endl;

    do {
      getline(cin, input);

      if(input.compare("KNIFE") == 0) {
        cout << "\"Well net. Go, take your KNIFE.\"" << endl << endl;

        inventory[1] = "KNIFE";
      }
      else if(input.compare("GLASSES") == 0) {
        cout << "\"I wouldn't expect your excellency to be interested in this garbage. \nShe isn't nearsighted, after all. Nevertheless, take your GLASSES.\"" << endl << endl;

        inventory[2] = "GLASSES";
      }
      else if(input.compare("GLYPH") == 0) {
        if(inventory[0].compare("PEN") == 0) {
          cout << "\"Very well then. \nBy the might of *&*&*&*&*&*&*&*&*&, please POINT a GLYPH of GLOBALITY onto \nits excellency.\"" << endl << "\"It is done, I'll be taking your pen, too.\"" << endl << endl;

          inventory[0] = "[EMPTY]";
          inventory[3] = "POINTED GLYPH of GLOBALITY";
        }
        else {
          cout << "Nice try, excellency. No PEN, no GLYPH. Only the ambitious succeed." << endl << endl;
        }
      }

    } while (input.compare("QUIT") != 0);
    room = 4;
  }
