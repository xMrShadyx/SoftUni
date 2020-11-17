#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int length;
  int width;
  int height;
  float percent;
  cin >> length >> width >> height >> percent;

  int size = length * width * height;
  float total = size * 0.001;
  float percentage = percent * 0.01;

  float lastTotal = total * (1 - percentage);

  cout << lastTotal;

  return 0;
}
