#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

void skyrim();

namespace lily {
	void pow(float x, int y) {
		float total = 0;

		for (int i = 1; i <= y; i++) {
			if(total == 0) {
				total = x;
			}
			else {
				total = total * x;
			}
		}

		cout << fixed << setprecision(3) << total;
	}
}

int main() {
	float x = 2.46;
	int y = 4;
	
	lily::pow(x, y);

	//cout << fixed << setprecision(5) << answer;
}

void skyrim() {
	cout << "Hey, you. You're finally awake. \n\nYou were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there. Damn you Stormcloaks. Skyrim was fine until you came along. Empire was nice and lazy. If they hadn't been looking for you, I could've stolen that horse and be halfway to Hammerfell. You there. You and me - we shouldn't be here. It's these Stormcloaks the Empire wants. We're all brothers and sisters in binds now, thief. Shut up back there! And what's wrong with him, huh? Watch your tongue. You're speaking to Ulfric Stormcloak, the true High King. Ulfric? The Jarl of Windhelm? You're the leader of the rebellion. But if they've captured you... Oh gods, where are they taking us? I don't know where we're going, but Sovngarde awaits. No, this can't be happening. This isn't happening. Hey, what village are you from, horse thief? Why do you care? A Nord's last thoughts should be of home. Rorikstead. I'm... I'm from Rorikstead.\n\n...looks like the Thalmor are with him. \n\nGeneral Tullius, sir.The headsman is waiting.Good.Let's get this over with! Shor, Mara, Dibella, Kynareth, Akatosh. Divines, please help me. Look at him. General Tullius the Military Governor. And it looks like the Thalmor are with him. Damn elves. I bet they had something to do with this. \n\nWhy are we stopping ? Why do you think ? End of the line.Let's go. Shouldn't keep the gods waiting for us." << endl;
}
