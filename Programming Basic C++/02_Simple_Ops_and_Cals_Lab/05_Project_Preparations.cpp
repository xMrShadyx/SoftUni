#include <iostream>
using namespace std;

int main() {
  string archName;
  cin >> archName;
  
  int amountProject;
  cin >> amountProject;

  int hourPerProject = amountProject * 3;

  cout << "The architect " << archName << "will need " << hourPerProject << " hours to complete " << amountProject << " project/s." << endl;
  return 0;
}
