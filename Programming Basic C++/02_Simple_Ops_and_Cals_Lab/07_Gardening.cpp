#include <iostream>
#include <iomanip>
using namespace std;

int main() {

  float greenNeeding;
  cin >> greenNeeding;

  float resultFullPrice = greenNeeding * 7.61;
  float someDiscount = resultFullPrice * 0.18;
  float lastPrice = resultFullPrice - someDiscount;

  cout << fixed << setprecision(2) << "The final price is: " << lastPrice << " lv. The discount is: " << someDiscount << " lv." << endl;

  return 0;
}
