#include <iostream>
#include <math.h> // round() function from this library.
using namespace std;

int main() {
  double radians;
  cin >> radians;

  double deg = radians * 180 / 3.14;
  cout << round(deg) << endl;

  return 0;
}
