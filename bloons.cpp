//"bloons" style game, part 1
//coded by Dr. Mo, Feb 2022
//dynamicsofanasteroid.com
#include <SFML/Graphics.hpp>
#include <vector>
#include<iostream>
using namespace std;

//discussion questions for students:
//1) How would you *avoid* diagonals in the path? How do you purposely create them?
//2) Why the "-1" in this line: if(currPath < pathPoints.size()-1)? Why is it needed?
//3) What's the difference between a struct and a class? Could we have used a class instead of a struct?

int ticker = 0;

//create a struct: structs are like classes, but no functions (just variables)
struct point {
    int x;
    int y;
};

class bloon {
private: 
    int xpos;
    int ypos;
    int currPath;
public:
    bloon(int x, int y);
    void move(vector<point>myPath);
    void draw(sf::RenderWindow& window);
};

bloon::bloon(int x, int y) {
    xpos = x;
    ypos = y;
    currPath = 0;
}

void bloon::move(vector<point>myPath) {
    //pathing algorithm*******************************************************************
        //this works by moving the x and y coord of our baloon towards the (x,y) of the next point in the path
        //the path is stored as a series of points in a vector called "pathPoints"

    ticker++; //slow dem bloons down
    if (ticker % 50 == 0) { //make 30 bigger to slow down baloon more

        //first check if you're at the turning point, move to next point if you are
        if ((xpos == myPath[currPath].x) && (ypos == myPath[currPath].y))
            if (currPath < myPath.size() - 1) //don't walk off end of vector!
                currPath++; //iterate to next point

        //if not there yet, move our x towards x position of next junction
        if (xpos < myPath[currPath].x)
            xpos += 1;
        if (xpos > myPath[currPath].x)
            xpos -= 1;
        //and move our y towards y position of next junction
        if (ypos < myPath[currPath].y)
            ypos += 1;
        if (ypos > myPath[currPath].y)
            ypos -= 1;
    }//end pathing algorithm**************************************************************
}

void bloon::draw(sf::RenderWindow& window) {
    sf::CircleShape bloon(50);
    bloon.setFillColor(sf::Color(250, 0, 0));
    bloon.setPosition(xpos, ypos);
    window.draw(bloon);
}


int main()
{
    //set up path points using the struct we made
    struct point p1;
    p1.x = 100;
    p1.y = 400;
    struct point p2;
    p2.x = 100;
    p2.y = 300;
    struct point p3;
    p3.x = 300;
    p3.y = 300;
    struct point p4;
    p4.x = 300;
    p4.y = 500;
    struct point p5;
    p5.x = 700;
    p5.y = 500;
    struct point p6;
    p6.x = 700;
    p6.y = 300;
    struct point p7;
    p7.x = 800;
    p7.y = 300;


    //set up vector to hold path points, push path points into it
    vector <point> pathPoints;
    pathPoints.push_back(p1);
    pathPoints.push_back(p2);
    pathPoints.push_back(p3);
    pathPoints.push_back(p4);
    pathPoints.push_back(p5);
    pathPoints.push_back(p6);
    pathPoints.push_back(p7);

    // create game window
    sf::RenderWindow window(sf::VideoMode(800, 800), "bloons");

    
    
    sf::RectangleShape grass;
    grass.setSize(sf::Vector2f(100, 100));
    grass.setFillColor(sf::Color(50, 250, 50));
    int currPath = 0; //begin heading towards the first point in the pathing vector

    int map[8][8] = {
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,1,1,1,0,0,0,1,
        1,1,0,1,0,0,0,1,
        0,0,0,1,1,1,1,1,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
    };

    bloon bloon1(-100, 400);
    bloon bloon2(-200, 400);
    bloon bloon3(-300, 400);
    bloon bloon4(-400, 400);
    bloon bloon5(-500, 400);

    vector <bloon> bloons;
    bloons.push_back(bloon1);
    bloons.push_back(bloon2);
    bloons.push_back(bloon3);
    bloons.push_back(bloon4);
    bloons.push_back(bloon5);

    // GAME LOOP----------------------------------------------------------------------------------------
    while (window.isOpen())
    {
        // check all the window's events that were triggered since the last iteration of the loop
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }



        for (int i = 0; i < 5; i++) {
            bloons[i].move(pathPoints);
        }


        //move da bloon

        // Render section----------------------------------------------------------------
        window.clear(sf::Color(100,100,100));

        for (int rows = 0; rows < 8; rows++) {
            for (int cols = 0; cols < 8; cols++) {
                if (map[rows][cols] == 1) {
                    grass.setPosition(cols * 100, rows * 100);
                    window.draw(grass);
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            bloons[i].draw(window);
        }

        window.display();
    }

    return 0;//buh bye
}
