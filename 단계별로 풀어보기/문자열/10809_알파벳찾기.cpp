#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

int main(void)
{
	string S;
	cin >> S;
	
	for(int i='a';i<='z';++i){
//		cout << "type : " << typeid(S.find(char(i))).name() << endl;  // unsigned int -> overflow
		cout << int(S.find(char(i))) << ' ';
	}
	cout << endl;
	
	return 0;
}

