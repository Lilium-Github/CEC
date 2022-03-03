#include <SFML/Graphics.hpp>
#include<iostream>
#include <vector>
#include <time.h>
#include <stdlib.h>

using namespace std;


int main()
{
    srand(time(NULL));
    
    sf::RenderWindow window(sf::VideoMode(800, 800), "SFML Base Code");

    sf::CircleShape circle;

    //change each of these to vectors of 20 random numbers
    vector<int> xpos;
    vector<int> ypos;
    vector<int> red;
    vector<int> blue;
    vector<int> green;
    vector<int> radius;

    for (int i = 0; i < 20; i++) {
        xpos.insert(xpos.begin(), rand() % 800);
    }

    for (int i = 0; i < 20; i++) {
        ypos.insert(ypos.begin(), rand() % 800);
    }

    for (int i = 0; i < 20; i++) {
        red.insert(red.begin(), rand() % 255);
    }

    for (int i = 0; i < 20; i++) {
        green.insert(green.begin(), rand() % 255);
    }

    for (int i = 0; i < 20; i++) {
        blue.insert(blue.begin(), rand() % 255);
    }

    for (int i = 0; i < 20; i++) {
        radius.insert(radius.begin(), rand() % 75);
    }

    while (window.isOpen())//GAME LOOP--------------------------------
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

        }

        //modify these arguments so each is a different slot of the vectors above
        for (int i = 0; i < 20; i++) {
            circle.setRadius(radius[i]);
            circle.setFillColor(sf::Color(red[i], green[i], blue[i]));
            circle.setPosition(xpos[i], ypos[i]);
            window.draw(circle);
        }
        window.display();



    }//end game loop-------------------------------------------------

    return 0;
} //end main
