#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int find_idx(const vector<int>& nums,const int target, int mid){	
//	cout <<"here0"<< endl;
	int idx = 0;
	
	
	if(nums[mid-1] < target && target < nums[mid]){		// case 1: found
//		cout <<"here1"<< endl;
		idx = mid;
//		cout << "idx : " << idx << endl;
		return	idx;
	}
	else if ( nums[mid] < target && target < nums[mid+1]) {
//		cout <<"here1-2"<< endl;
		idx = mid+1;
//		cout << "idx : " << idx << endl;
		return	idx;
	}
	else if (nums[mid] < target) {						// case 2 : search right
//		cout <<"here2"<< endl;
		if (nums.size()-1 - mid > 1){
			mid += (nums.size()-1 - mid)/2 + 1;
			idx = find_idx(nums, target, mid);
		}
		else if(nums.size()-1 - mid == 1){
			if (nums[nums.size()-1] < target) 
				idx = nums.size();
			else
				idx = mid + 1;
		}
//		cout << "idx : " << idx << endl;
		return idx;
	}
	else if (target < nums[mid-1]) {					// case 3 : search left
//		cout <<"here3"<< endl;
		if (mid > 1) {
			mid = mid/2;
			idx = find_idx(nums, target, mid);
		}
		else if(mid == 1) {
			if (target < nums[0])
				idx = 0;
			else
				idx = mid;	
		}
//		cout << "idx : " << idx << endl;
		return idx;
	}
	
	return idx;
	
}

void print_nums(const vector<int>& nums) {
	cout << "nums : ";
	for(int i=0;i<nums.size();++i){
		cout << nums[i] << ' ';
	}
	cout << endl;
}

int main(void)
{
	int N,tmp,mid,idx;
	cin >> N;	
	vector<int> nums;
	
	cin >> tmp;
	nums.push_back(tmp);
//	print_nums(nums);
	
	if (N>1) {
		cin >> tmp;
		if(tmp < nums[0]){
			nums.insert(nums.begin(),tmp);
		}
		else{
			nums.push_back(tmp);
		}
//		print_nums(nums);
		
		for(int i=2;i<N;++i){
//			cout << "i : " << i << endl;
			cin >> tmp;
			mid = nums.size()/2;
//			cout << "mid : " << mid << endl;
			idx = find_idx(nums, tmp, mid);
	
			nums.insert(nums.begin()+idx,tmp);
//			print_nums(nums);
		}
	}

	for(int i=0;i<nums.size();++i)
		cout << nums[i] << endl;
	
	return 0;
}

/*
시간제한 : 2초, 메모리 제한 256MB
2750 문제와 똑같이 풀면 시간 초과 발생 

해결 : 입력 값 받으면서 동시에 정렬. (이진 탐색 이용) 
-> 결과 : 시간 초과 

*/
