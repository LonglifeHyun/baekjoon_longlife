#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int C, N;
	cin >> C;
	
	
	for(int i=0;i<C;++i){
		cin >> N;
		vector<int> scores(N,0);
		
		int sum = 0;
		float mean;
		for(int j=0;j<N;++j){
			cin >> scores[j];
			sum += scores[j];
		}
		
		mean = float(sum) / float(N);
//		cout << "mean : " << mean << endl;
		sort(scores.rbegin(), scores.rend());
		
//		cout << "[" << i << "] : ";
//		for(int j=0;j<N;++j)
//			cout << scores[j] << ' ';
//		cout << endl;
				
		vector<int>::iterator it = find(scores.begin(),scores.end(),(int)mean);
		while( it == scores.end() ){
			mean--;
			it = find(scores.begin(),scores.end(),(int)mean);
		}
		
		int cnt = it-scores.begin();
//		cout << "it : " << it-scores.begin() << endl;
		
		cout << fixed;
		cout.precision(3);
		cout << (float)cnt / (float)N * 100 << "%" << endl;
	}
	
	return 0;
}
