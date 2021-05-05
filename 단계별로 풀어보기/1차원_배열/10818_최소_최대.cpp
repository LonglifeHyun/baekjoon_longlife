#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int N;
	cin >> N;
	
	vector<int> nums(N);
	
	int tmp;
	for(int i=0;i<nums.size();++i){
		cin >> tmp;
		nums[i] = tmp;
	}
	
	sort(nums.begin(), nums.end());
	
	cout << nums[0] << " " << nums[nums.size()-1] << endl;
	
	
	return 0;
}
