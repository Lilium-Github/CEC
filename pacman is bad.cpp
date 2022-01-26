//SFML C++ PACMAN pt 2
//created by Dr. Mo 11/21
//dynamicsofanasteroid.com

#include<iostream>
#include "SFML/Graphics.hpp"
using namespace std;

enum DIRECTIONS { LEFT, RIGHT, UP, DOWN }; //left is 0, right is 1, up is 2, down is 3

int main() {
    //game set up (you'll need these lines in every game)
    sf::RenderWindow screen(sf::VideoMode(1200, 800), "pacman"); //set up screen
    sf::Event event; //set up event queue
    sf::Clock clock; //set up the clock (needed for game timing)
    const float FPS = 60.0f; //FPS
    screen.setFramerateLimit(FPS); //set FPS

    //load in images
    sf::Texture brick;
    brick.loadFromFile("brick.png");
    sf::Sprite block;
    block.setTexture(brick);

    sf::Texture v_wall;
    v_wall.loadFromFile("wall-v.png");
    sf::Sprite vWall;
    vWall.setTexture(v_wall);

    sf::Texture h_wall;
    h_wall.loadFromFile("wall-h.png");
    sf::Sprite hWall;
    hWall.setTexture(h_wall);

    int map[20][30] = {
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
        1,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2,0,1,
        1,0,2,0,2,0,3,3,3,3,3,0,2,0,0,0,0,2,0,3,3,3,3,3,0,2,0,2,0,1,
        1,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2,0,1,
        1,0,2,0,2,0,3,3,3,3,3,3,1,3,0,0,3,1,3,3,3,3,3,3,0,2,0,2,0,1,
        1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1,
        1,0,2,0,1,3,3,3,3,3,3,3,3,3,0,0,3,3,3,3,3,3,3,3,3,1,0,2,0,1,
        1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,
        1,0,1,3,3,3,3,3,1,0,2,0,1,1,1,1,1,1,0,2,0,1,3,3,3,3,3,1,0,1,
        1,0,0,0,0,0,0,0,2,0,2,0,1,1,1,1,1,1,0,2,0,2,0,0,0,0,0,0,0,1,
        1,0,1,3,3,3,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,3,3,3,1,0,1,
        1,0,2,0,0,0,2,0,2,0,1,1,1,1,0,0,1,1,1,1,0,2,0,2,0,0,0,2,0,1,
        1,0,2,0,2,0,2,0,2,0,1,1,1,1,0,0,1,1,1,1,0,2,0,2,0,2,0,2,0,1,
        1,0,2,0,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,2,0,2,0,1,
        1,0,2,0,2,0,2,0,2,0,3,3,3,3,3,3,3,3,3,3,0,2,0,2,0,2,0,2,0,1,
        1,0,2,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,2,0,1,
        1,0,2,0,1,3,3,3,1,3,3,3,0,3,3,3,3,0,3,3,3,1,3,3,3,1,0,2,0,1,
        1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    };

    //player setup
    int xpos = 40;
    int ypos = 40;
    int vx = 0;
    int vy = 0;
    int radius = 20;
    sf::CircleShape player(radius);
    player.setFillColor(sf::Color(250, 250, 0)); //using RGB value for color here (hex also works)
    player.setPosition(xpos, ypos); //top left "corner" of circle (not center!)
    bool keys[] = { false, false, false, false };


    //################### HOLD ONTO YOUR BUTTS, ITS THE GAME LOOP###############################################################
    while (screen.isOpen()) {//keep window open until user shuts it down

        while (screen.pollEvent(event)) { //look for events-----------------------

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                screen.close();
            //KEYBOARD INPUT 
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
                keys[LEFT] = true;
            }
            else keys[LEFT] = false;

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
                keys[RIGHT] = true;
            }
            else keys[RIGHT] = false;


            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
                keys[UP] = true;
            }
            else keys[UP] = false;

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
                keys[DOWN] = true;
            }
            else keys[DOWN] = false;


        }//end event loop---------------------------------------------------------------

         //move Mr. Pac
        if (keys[LEFT] == true) {
            vx = -5;
            vy = 0;
        }

        else if (keys[RIGHT] == true) {
            vx = 5;
            vy = 0;
        }

        else if (keys[UP] == true) {
            vy = -5;
            vx = 0;
        }
        else if (keys[DOWN] == true) {
            vy = 5;
            vx = 0;
        }

        player.setPosition(xpos, ypos);

        //right collision
        if (vx > 0 &&
            //top right
            ((map[(ypos+2) / 40]
                [(xpos + (radius * 2)+2) / 40] > 0) ||
                //bottom right
                (map[(ypos + (radius * 2)-2) / 40]
                    [(xpos + (radius * 2)+2) / 40] > 0)))
        {
            vx = 0;
        }

        if (vx < 0 &&
            //top left
            ((map[(ypos+2) / 40]
                [(xpos + 2) / 40] > 0) ||
                //bottom left
                (map[(ypos + (radius * 2)-2) / 40]
                    [(xpos + 2) / 40] > 0)))
        {
            vx = 0;
        }

        if (vy < 0 &&
            //top right
            ((map[(ypos+2) / 40]
                [(xpos + (radius * 2)+2) / 40] > 0) ||
                //top left
                (map[(ypos+2) / 40]
                    [(xpos+2) / 40] > 0)))
        {
            vy = 0;
            cout << "bump!\n";
        }


        if (vy > 0 &&
            //bottom right
            ((map[(ypos + (radius * 2)-2) / 40]
                [(xpos + (radius * 2)+2) / 40] > 0) ||
                //bottom left
                (map[(ypos + (radius * 2)-2) / 40]
                    [(xpos+2) / 40] > 0)))
        {
            vy = 0;
        }

        xpos += vx;
        ypos += vy;

        //render section-----------------------------------------
        screen.clear(); //wipes screen, without this things smear

        //draw map
        for (int rows = 0; rows < 20; rows++) {
            for (int cols = 0; cols < 30; cols++) {
                if (map[rows][cols] == 1) {
                    block.setPosition(cols * 40, rows * 40);
                    screen.draw(block);
                }
                if (map[rows][cols] == 2) {
                    vWall.setPosition(cols * 40, rows * 40);
                    screen.draw(vWall);
                }
                if (map[rows][cols] == 3) {
                    hWall.setPosition(cols * 40, rows * 40);
                    screen.draw(hWall);
                }
            }
        }
        screen.draw(player); //draw player
        screen.display(); //flips memory drawings onto screen

    }//######################## end game loop ###################################################################################

    cout << "goodbye!" << endl;
} //end of main
