#include"GameObject.h"
#include<SFML/Graphics.hpp>

void star::draw(sf::RenderWindow& window) { //passes a POINTER to the gamescreen
    sf::CircleShape triangle1(30, 3);
    triangle1.setFillColor(sf::Color(0, 200, 255));
    triangle1.setPosition(xpos, ypos);
    window.draw(triangle1);//draw to gamescreen

    sf::CircleShape triangle2(30, 3);
    triangle2.setFillColor(sf::Color(200, 200, 255));
    triangle2.setPosition(xpos + 40, ypos - 15);
    triangle2.rotate(60); //twist to make star shape
    window.draw(triangle2);
}

void duck::draw(sf::RenderWindow& window) {
    //can you complete this? make a duck draw to the screen!
    sf::Texture duckTexture;
    duckTexture.loadFromFile("duck.png");
 
    sf::Sprite duck(duckTexture);
    duck.setPosition(xpos, ypos);

    window.draw(duck);
    cout << "drawing ducks!" << endl;
}

void invader::draw(sf::RenderWindow& window) {
    sf::Texture texture;
    texture.loadFromFile("invader.png");

    sf::Sprite invader(texture);
    invader.setPosition(xpos, ypos);

    window.draw(invader);
}