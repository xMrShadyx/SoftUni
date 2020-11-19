#include <iostream>
using namespace std;

int main() {
  int amountTables;
  double lenghtNonSquareTables;
  double lenghtSquareTables;
  cin >> amountTables >> lenghtNonSquareTables >> lenghtSquareTables;

  double totalVolume = amountTables * (lenghtNonSquareTables + 2 * 0.30) * (lenghtSquareTables + 2 * 0.30);
  double totalSquare = amountTables * (lenghtNonSquareTables / 2) * (lenghtNonSquareTables / 2);
  double priceInUSD = (totalVolume * 7) + (totalSquare * 9);
  double priceInBGN = priceInUSD * 1.85;

  cout.setf(ios::fixed);
  cout.precision(2);

  cout << priceInUSD << "USD" << endl;
  cout << priceInBGN << "BGN" << endl;
  return 0;
}
