#include <iostream>
#include <string>

using namespace std;

int cal_score(const string result)
{
	int max_score=0, score=0;
	
	for(int i=0;i<result.size();++i){
		if(result[i]=='O'){
			max_score++;
			score += max_score;
		}
		else
			max_score = 0;
	}		
	
	return score;
}

int main(void)
{
	int n;
	cin >> n;
	
	string tmp;
	int score;
	for(int i=0;i<n;++i){
		cin >> tmp;
		score = cal_score(tmp);
		cout << score << endl; 	
	}
	
	return 0;
}
