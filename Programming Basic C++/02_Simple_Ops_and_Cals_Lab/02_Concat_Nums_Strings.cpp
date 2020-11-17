#include <iostream>
using namespace std;

int main() {
  string firstName;
  string lastName;
  string town;
  int age;
  
  cout << "What is your firstName: " << endl;
  cin >> firstName;
  cout << "What is your lastName: " << endl;
  cin >> lastName;
  cout << "What is your age: " << endl;
  cin >> age;
  cout << "Where you from: " << endl;
  cin >> town;

  cout << "You are " << firstName << " " << lastName << ", a " << age << "-years old person from " << town << endl;
  return 0;
}
