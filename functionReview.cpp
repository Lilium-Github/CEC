#include <iostream>
#include <cmath>
using namespace std;

int add(int x, int y);
int pythagoras(int a, int b);

int main() {
    int num1, num2;
    cout << "please enter a and b:" << endl;

    cin >> num1;
    cin >> num2;
    cout << num1 << " + " << num2 << " = " << add(num1, num2) << endl;

    cout << "c = " << pythagoras(num1, num2) << endl;
}

int add(int x, int y) {
    return x + y;
}

int pythagoras(int a, int b) {
    return sqrt((a * a) + (b * b));
}
