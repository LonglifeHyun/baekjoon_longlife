#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	vector< pair<int,int> > nums(9);
	
	pair<int,int> tmp;
	for(int i=0;i<nums.size();++i){
		cin >> tmp.first;
		tmp.second = i+1;
		nums[i] = tmp;
	}
	
	sort(nums.begin(), nums.end());
	
	cout << nums[nums.size()-1].first << endl 
		 << nums[nums.size()-1].second << endl;
	
	return 0;
}
