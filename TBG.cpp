#include<iostream>
#include<string>
#include <time.h>   
#include <stdlib.h>
using namespace std;


//inventory; slot 0 is for the pen, slot 1 is for the cake, slot 2 is for the glasses
// slot 3 is for the glyph, slot 4 is for the KNIFE, slot 5 is for the EGG
string inventory[] = {"[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]", "[EMPTY]"};
int room = 1;

void shop(string name);
void monster();
void battle(int monster_health);

int health = 20;

bool monster_exists = true;

string lore = "WE BELIEVE TO HAVE FOUND... AN EXIT.";

int main() {
	// game vars
  string input;
	bool win = false;
  int turns = 1;

  cout << "What is its excellency's's NAME?\n";
  string name;
  getline(cin, name);
  cout << "How excellent. Your VESSEL will soon be prepared. Thank you for your assistance." <<  endl << endl; 

	cout << "You don't know where you are. All you can tell is that there's a bright white LIGHT above you, and that the air hums with MACHINERY." << endl;
  cout<< "You hear a man's VOICE come from speakers above: " << endl;
	cout << "\"Welcome, valued subject, to the Institute For Research On Souls And The Ethereal.\"" << endl << endl;

	do {   // game loop 
		if (health < 1) {
			cout << "you died!" << endl;
			return 0;
		}

		if (win) {
			cout << "hey, you shouldn't be seeing this yet!" << endl;
		}
    if(input.compare("T") == 0) {
      cout << "You're on turn number " << turns << endl << endl;
    }
    turns++;

    if(input.compare("I") == 0) {
      cout << "Current INVENTORY is:\n\n";
      for(int i = 0; i < 8; i++) {
        cout << inventory[i] << endl;
      }
      cout << endl;
    }

		if(input.compare("EAT") == 0 && inventory[1].compare("CAKE") == 0) {
      health = health + 10;
			cout << "Cake. It tastes good, as cake tends to do. +10 HP!\n\n";
			inventory[1] = "[EMPTY]";
    }

    if(input.compare("H") == 0) {
      cout << "Current HEALTH is: " << health << "/20. \n\n";
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
			cout << "You're in a HALLWAY with pearly white walls and a floor, golden carpet below your feet. You can \ngo SOUTH, EAST, or WEST." << endl;
      cout << "A grayed-out picture of a man with a goat's head hangs on the wall. The plaque under it shows his name is \n\"THE EXILED ONE.\"" << endl << endl;

			getline(cin, input);
			if (input == "S")
				room = 1;
			else if (input == "E")
				room = 3;
			else if (input == "W")
				room = 4;
			break;
		case 3:
			cout << "You're in another HALLWAY, or perhaps it's a continuation of the first. On your sides, \nbreaking the monotony of the white walls are golden DOORS, all locked except for one." << endl;
      cout << "Walking in, you notice FILEs strewn about a desk. You may READ them, or move to the EAST or WEST. \n\n" << endl;
			getline(cin, input);
			if (input == "W")
				room = 2;
      else if (input == "E")
				room = 6;
      else if (input.compare("READ FILES") == 0) {
        cout << lore << endl << endl;
      }
			break;
		case 4:
			cout << "You're in a BROOM CLOSET. There's a sinking feeling that you're supposed to see this." << endl;
      cout << "EAST is the way out of the BROOM CLOSET. You hear another VOICE from the NORTH wall." << endl << endl;
			cin >> input;
			if (input == "N") {
				room = 5;
			}
			else if (input == "E") {
				room = 2;
			}
			break;
		case 5:
      shop(name);
			room = 4;
			break;
		case 6:
       if(inventory[4].compare("KNIFE") != 0) {
			  cout << "You're in a BREAK ROOM. The golden carpet under your feet is peppered \nwith coffee stains. On the (noticably off-white) walls, several pieces\n of artwork. Included are portraits of various CEOs (all bald), as well as \nlandscapes of green, grassy hills with a blue sky. There are clouds concentrated on the middle right, \nalong with a blue mountain." << endl;
        cout << "On a nearby counter is a small, butter-covered KNIFE. There are DOORS to the EAST and WEST. What will you do?\n\n";
        getline(cin, input);
        if(input.compare("TAKE KNIFE") == 0) {
          inventory[4] = "KNIFE";
          cout << "\nWithout asking for permission, you gave in to greed and took the KNIFE." << endl;
        }
      }
      else {
        cout << "You're in a BREAK ROOM. The golden carpet under your feet is peppered \nwith coffee stains. On the (noticably off-white) walls, several pieces\n of artwork. Included are portraits of various CEOs (all bald), as well as \nlandscapes of green, grassy hills with a blue sky. There are clouds concentrated on the middle right, \nalong with a blue mountain. \nThe knife is gone." << endl;
        getline(cin, input);
      }

      if (input == "W") 
				room = 3;
			else if (input == "E")
				room = 7;
      
      break;
      
		case 7:
        cout << "You're in a STAIRWELL. The stairs themselves are going downwards, \nbefore stopping in front of a NORTH-facing DOOR. At the top of the stairs is \nanother DOOR, this one facing WEST. A black, rusted sign informs you that you're in STAIRWELL B. \n\n";

				getline(cin, input);

        if (input == "N") 
				  room = 8;
			  else if (input == "W")
				  room = 6;
        break;
		case 8:
      
			if(monster_exists) {
				cout << "Walking through the DOOR, you notice the room you're in is completely white, with not so much as \na speck of dust on the wall. More importantly, however, are the screams coming from a corner of the room\n\n";
				monster();
				if(health < 1) {
					break;
				}
				if(monster_exists == false) {
					cout << "Blue blood on your hands, you kick the creature's remains to a corner of the room." << endl;
					cout << "Now's your chance to get a better view of this room." << endl;
				}
			}
			cout << "You appear to be in some kind of containment room. The walls and floor are all completely white and spotless, save for the monster's body. A man in a lab coat, \npresumably the one who screamed earlier, is standing near a wall. looking you up and down."  << endl;
			cout << "\"Hello there! Ah, um, thank you for saving me. It seems you truly are the superior specimen between the two of you. \"\n";

			if (inventory[2].compare("GLASSES") == 0) {
				inventory[2] = "NO GLASSES";
				cout << "\"Thank you for finding my GLASSES, too! I must say, you make a great HERO. I'm afraid all I have for you is an EGG, though.\"" << endl;
				inventory[5] = "EGG";
			}
			else if (inventory[2].compare("NO GLASSES") == 0) {
				inventory[2] = "NO GLASSES";
				cout << "\"Thank you for finding my GLASSES, too! I must say, you make a great HERO.\"" << endl;
			}
			else {
				cout << "\"Sorry to ask, but would you happen to know where my glasses are?\"";
			}

			getline(cin, input);

			if (input == "S") 
				room = 7;
			else if (input == "W")
				room = 9;
      break;

		case 9:
			cout << "Upon stepping into this room, you can tell that something is different; rather \nthan standard office tile or carpet, the floor is made of polished marble, perfectly \nwhite other than the speckles of gold you can see." << endl;

			cout << "A second staircase stands in front of you, ivory steps adorned by gold. It rises \nNORTH into the clouds, and that's when you realize this room has no roof. \nYou're not sure if any of these rooms have had roofs, actually.\nYou can return the way you came by going EAST." << endl;

			if (input == "N") {
				cout << "\nYou climb, and climb, and climb.\n" << endl;
				room = 10;
			}
			else if (input == "E")
				room = 8;
      break;

		//case 10:

    //case 11:


			
		}


		cout << endl;
	} while (input != "q");
}

void shop(string name) {
    cout << "You come across what appears to be a SHOP. A statue of THE EXILED ONE greets you. \nHis goat head does not move with his VOICE." << endl;
    cout << "\"Hello, " << name << " and welcome to my shop. Normally, she'd never enter this place... \nBut with your arrival, her situation has become far from normal.\"" << endl;

    string input;

    cout << "\"Let's see... I have a few things for you. A slice of CAKE, a pair of (broken) GLASSES. \nI could also inscribe a cursed GLYPH for you, but I'd need a PEN to sign the CONTRACT with...\"" << endl;
    cout << "\"Make your choice, excellency. That, or simply QUIT our little transaction.\"" << endl << endl;

    do {
      getline(cin, input);

      if(input.compare("CAKE") == 0) {
        cout << "\"Well met. Go, take some CAKE.\"" << endl << endl;

        inventory[1] = "CAKE";
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

          health = health - 10;
        }
        else {
          cout << "Nice try, excellency. No PEN means no CONTRACT, which means no GLYPH. Only the ambitious succeed." << endl << endl;
        }
      }

    } while (input.compare("QUIT") != 0);
    room = 4;
}

void monster() {
	int coin = rand() % 10 + 1;
	cout << "A monster appears before you." << endl;

	battle(15 + coin);
}

void battle(int num) {
	cout << "Battle Begin!" << endl;

	string input;

	int player_attack = 0;
	int monster_attack = 0;

	int monster_health = num;
	
	while (monster_health > 0 && health > 0) {
		input = "placeholder";

		cout << "The monster has " << monster_health << " remaining!" << endl;
		cout << "You have " << health << " remaining!" << endl;
		cout << "Input 'A' to attack, or 'D' to defend!\n\n";
		getline(cin, input);

		if(input.compare("A") == 0) {
			if(inventory[4].compare("KNIFE") == 0) {
				player_attack = rand() % 5 + 3;
				cout << "You slash at the monster, dealing " << player_attack << " damage." << endl;
			}
			else {
				player_attack = rand() % 3 + 1;
				cout << "You punch at the monster, dealing " << player_attack << " damage." << endl;
			}
			monster_attack = rand() % 4 + 2;
			cout << "The creature lunges for you, dealing " << monster_attack << " damage." << endl;
		}
		else if(input.compare("D") == 0) {
			player_attack = 0;
			cout << "You put your arms up in an attempt to block the monster." << endl;
			monster_attack = rand() % 3;
			cout << "The creature lunges for you, dealing a measly " << monster_attack << " damage." << endl;
		}

		health -= monster_attack;
		monster_health -= player_attack;

		if(health < 1) {
			cout << "YOU DIED!\n\n\n\n\n\n\n";
		}
		else if(monster_health < 1) {
			cout << "Congrats, you defeated the monster!";
			monster_exists = false;
		}
		else {
			cout << "Your body naturally heals itself for 1 health." << endl;
			health = health + 1;
		}

	} 
}
