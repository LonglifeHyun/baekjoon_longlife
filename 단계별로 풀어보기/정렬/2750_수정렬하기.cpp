#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

void print_nums(const vector<int> nums) {
	cout << "nums : ";
	for(int i=0; i<nums.size(); ++i) {
		cout << nums[i] << ' ';
	}
	cout << endl;
}

int main(void)
{
	int N;
	cin >> N;	
	
	vector<int> nums;
	int tmp;
	for(int i=0; i<N;i++){
		cin >> tmp;
		nums.push_back(tmp);
	}
	
	//print_nums(nums);
	
	sort(nums.begin(), nums.end());
	//print_nums(nums);
	
	for(int i=0;i<nums.size();++i)
		cout << nums[i] << endl;
		
	return 0;
}

