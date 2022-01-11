#include <SFML/Graphics.hpp>
#include<iostream>
using namespace std;

int main()
{
    sf::RenderWindow window(sf::VideoMode(500, 500), "Hello World!");

    sf::Font font;
    if (!font.loadFromFile("Windsong.ttf")) cout << "font didn't load" << endl;

    sf::Text text;
    text.setString("Hello world");
    text.setCharacterSize(24); // in pixels, not points!
    text.setFillColor(sf::Color::Red);
    text.setStyle(sf::Text::Bold | sf::Text::Underlined);
    text.setFont(font);


    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(text);
        window.display();
    }

    return 0;
}
