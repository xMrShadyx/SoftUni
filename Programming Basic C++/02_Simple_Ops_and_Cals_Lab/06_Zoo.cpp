#include <iostream>
using namespace std;

int main() {
  float dogFood = 2.5;
  float otherFood = 4;

  float amountDogs;
  float otherAnimals;

  cin >> amountDogs;
  cin >> otherAnimals;

  float result = (amountDogs * dogFood) + (otherAnimals * otherFood);

  cout << result << " lv." << endl;

  return 0;
}
