#include <iostream>
#include <windows.h>
#include <vector>
#include <cmath>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

void quadForm(float a, float b, float c);

int main()
{
    srand(time(NULL));
    
    cout << "Welcome to the Program to Prove That Lily Knows CPP Concepts, or PPLKCPPC.\n" << endl;

    float input;

    cout << "How much money do you have? ";
    cin >> input;

    if (input > 24.57) {
        float change = input - 24.57;
        cout << "\nHere's your eggs. Your change is " << change << endl;
    }
    else if (input == 24.57) {
        cout << "\nHere's your eggs." << endl;
    }
    else {
        cout << "\nNo eggs for you." << endl;
    }

    bool troo = true;

    do {
        cout << "Press 'd' for dog, 'c' for cat, 'b' for birb, 'e' for eduardo, 'q' to go onto the next segment. \n";
        char input;
        cin >> input;

        switch (input) {
        case 'd':
            cout << "woof!" << endl;
            break;
        case 'c':
            cout << "meow." << endl;
            break;
        case 'b':
            cout << "The working class must seize the means of production." << endl;
            break;
        case 'e':
            cout << "eduardo!" << endl;
            break;
        case 'q' :
            troo = false;
            break;
        }

    } while (troo);

    int toPrint = 0;
    int loops = 0;
    vector<int> nums;

    while (toPrint != 75) {
        toPrint = rand() % 50 + 51;

        cout << toPrint << endl;
        nums.push_back(toPrint);

        loops++;
    }

    Beep(420, 500);

    float sum = 0;

    for (int i = 0; i < loops; i++) {
        sum += nums[i];
    }

    float avg = sum / loops;

    cout << "AVG: " << avg << endl;

    quadForm(1, 5, 6);
}

void quadForm(float a, float b, float c) {
    float root1 = ((b * -1.0) + sqrt(b*b-(4.0 * a * c))) / (2.0 * a);
    float root2 = ((b * -1.0) - sqrt(b*b-(4.0 * a * c))) / (2.0 * a);

    cout << root1 << "\n" << root2 << endl;
}
