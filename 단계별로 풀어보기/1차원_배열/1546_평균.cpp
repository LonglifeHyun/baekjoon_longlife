#include <iostream>

using namespace std;

int main(void)
{

	int N;
	cin >> N;
	
	int max = 1, sum = 0, tmp;
	for(int i=0;i<N;++i){
		cin >> tmp;
		if( max < tmp )
			max = tmp;
		sum += tmp;
	}
	
	cout << float(sum*100)/float(max*N) << endl;
		
	return 0;
}
