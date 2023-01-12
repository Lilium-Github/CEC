#include <iostream>
#include <vector>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

int main()
{
    srand(time(NULL));
    
    cout << "Welcome to Lily's dice rolling tool. \nPlease input the size of the die you'd like to roll: ";

    int vecLen;
    cin >> vecLen;

    vector<int> rolls;

    bool loop = true;

    float rollNum;

    while (loop) {
        cout << "\n\n\n";
        
        rolls.clear();

        cout << "How many times would you like to roll? \nType 0 to quit." << endl;
        cin >> rollNum;

        for (int i = 0; i < rollNum; i++) {
            rolls.push_back(rand() % vecLen + 1);
        }

        float sum = 0;
        int highest = 0;
        
        for (int i = 0; i < rollNum; i++) {
            sum += rolls[i];

            if (rolls[i] > highest) {
                highest = rolls[i];
            }
        }

        float avg = sum / rollNum;

        cout << "Your rolls were: ";
        for (auto i = rolls.begin(); i != rolls.end(); ++i)
            cout << *i << " ";
        cout << "\n";

        cout << "Your highest roll was " << highest << endl;

        cout << "Your average roll was " << avg << endl;

        if (rollNum == 0) {
            loop = false
        }
    }
}
