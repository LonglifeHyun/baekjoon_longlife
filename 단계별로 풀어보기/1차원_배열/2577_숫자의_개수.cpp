#include <iostream>
#include <vector>
#include <string>
#include <typeinfo>

using namespace std;

int main(void)
{
	int a, b, c;
	cin >> a >> b >> c;
	
	string mul_abc = to_string(a*b*c);

	vector<int> digits(10,0);	
	string tmp;
	
	for(int i=0;i<mul_abc.size();++i){
		tmp = mul_abc[i];
		digits[stoi(tmp)]++;
	}
	
	for(int i=0;i<digits.size();++i)
		cout << digits[i] << endl;
	
	return 0;
}
