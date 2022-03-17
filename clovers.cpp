#include <SFML/Graphics.hpp>

sf::RenderWindow window(sf::VideoMode(800, 800), "Shamrocks");
sf::CircleShape circle;
sf::RectangleShape rect;



class Clover
{
	public:

	int xpos;
	int ypos;

	void draw()
	{
		circle.setRadius(30);
		circle.setFillColor((sf::Color(0, 100, 0)));
		circle.setPosition(xpos, ypos);
		window.draw(circle);

		circle.setRadius(30);
		circle.setFillColor((sf::Color(0, 100, 0)));
		circle.setPosition(xpos + 50, ypos);
		window.draw(circle);

		circle.setRadius(30);
		circle.setFillColor((sf::Color(0, 100, 0)));
		circle.setPosition(xpos + 25, ypos - 50);
		window.draw(circle);

		rect.setPosition(xpos + 45, ypos);
		rect.setFillColor(sf::Color(0, 100, 0));
		rect.setSize(sf::Vector2f(20, 80));
		window.draw(rect);
	}
};

int main()
{

	while (window.isOpen())//GAME LOOP--------------------------------
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();

		}

		Clover clovers[7];

		for (int i = 0; i < 7; i++) {
			clovers[i].xpos = (i+1) * 100;
			clovers[i].ypos = (i+1) * 100;
		}

		//render section-------------------------------
		window.clear();

		for (int i = 0; i < 7; i++) {
			clovers[i].draw();
		}

		window.display();

	}//end game loop-------------------------------------------------



	return 0;
} //end main
