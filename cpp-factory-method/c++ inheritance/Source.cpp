#include<SFML/Graphics.hpp>

#include<iostream>
#include"factory.h"
using namespace std;

int main()
{
    srand(time(NULL));

    //these make star and duck objects
    StarFactory Stargen;
    DuckFactory Duckgen;
    InvaderFactory Lily;

    //SFML boilerplate
    sf::RenderWindow screen(sf::VideoMode(1000, 1000), "demo of virtual functions");

    vector<gameObject*> stuff; //make a vector of POINTERS (lets us do the next couple lines)
    for (int i = 0; i < 30; i++) {
        stuff.push_back(Stargen.create());
        stuff.push_back(Duckgen.create());
        stuff.push_back(Lily.create());
    }

    while (screen.isOpen()) {//game loop##################################################################
        sf::Event event;
        while (screen.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                screen.close();
        }

        //render section---------------------------------------------------------------
        screen.clear();
        for (vector<gameObject*>::iterator i = stuff.begin(); i != stuff.end(); i++)//walk through the vector
        {          
            (*i)->draw(screen); //THIS IS WHY WE MADE A VIRTUAL FUNCTION IN THE PARENT CLASS!
            //(*i)->printInfo(); //for testing purposes
        }      
        screen.display();

    }
    return 0;
}

