/*
메모리 2176 KB , 시간 1572 ms 

이건 문제조건이 메모리 8MB, 시간이 3초였음. 
시간이 좀 걸리더라도 메모리를 적게 쓰라는 거였음. 
근데 입력 개수는 10^7개. 
그러니까 입력값을 다 받아놓고 정렬하는 건 불가능. 
10^7 * 4 == 40 MB 이므로. 

그래서 해결은 입력값의 범위만큼 미리 배열 잡아놓고, 
입력될때마다 해당 입력값의 자리를 +1 하면 됨. 카운트 하는거. 
그럼 입력값의 범위는 10^4까지니까 최대 10^4 * 4 == 40 KB 

*/

#include <iostream>
#include <vector>
 
using namespace std;

int main(void)
{			
  	ios::sync_with_stdio(false);
  	cin.tie(NULL);	
  	
	int N;
	cin >> N;	
	
	vector<int> nums(10001,0);

	int tmp;
	for(int i=0; i<N;i++){
		cin >> tmp;
		nums[tmp]++;
	}
	
	for(int i=1;i<nums.size();++i)
		for(int j=0;j<nums[i];++j)
			cout << i << '\n';		
		
	return 0;
}

