#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	int N;
	string str;
	
	cin >> N >> str;
	
	int sum = 0;
	for(int i=0;i<N;++i)
		sum += str[i] - '0';
	cout << sum << endl;
	
	return 0;
}
