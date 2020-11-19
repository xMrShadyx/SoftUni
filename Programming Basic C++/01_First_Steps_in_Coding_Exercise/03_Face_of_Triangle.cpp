#include <iostream>
#include <cmath>
using namespace std;

int main() {
  double x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;

  double length = abs(x1 - x2);
  double width = abs(y1 - y2);

  double side1 = length * width;
  double side2 = 2 * (length + width);

  cout.setf(ios::fixed);
  cout.precision(2);

  cout << side1 << endl;
  cout << side2 << endl;
  return 0;
}
