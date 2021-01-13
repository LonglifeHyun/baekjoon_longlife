/*
(1) endl을 사용했을 때는 시간 초과 

(2) endl -> '\n' 변경 시 716ms

(3) 추가적인 속도 개선시  280ms

	ios::sync_with_stdio(false);	
		c의 입출력 함수 스트림 동기화 해제. 
		printf 와 cout 중 어느 것이 먼저 실행되는지 알 수 없기에 혼용 불가. 
	
	cin.tie(NULL);
		기본적으로 cin과 cout은 stream  버퍼를 공유(tie)하고 있다. 
		즉, 입력 또는 출력 요청을 받게 되면 각각의 stream 버퍼를 확인하고 flush하는 과정을 거치게 된다. 
		이때, 위의 명령어로 둘의 공유를 해제하면, 
		입출력 stream 버퍼를 모두 확인하는 과정을 거치지 않기 때문에 속도가 빨라질 수 있다.  

*/

#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

int main(void)
{
  	ios::sync_with_stdio(false);		// 이거 두개 적용해주면 입출력 속도가 빨라진다. 
  	cin.tie(NULL);						// 단, 이때 scanf, printf 등 C의 입출력 방식을 사용하면 안된다. 
  	
	int N;
	cin >> N;	
	
	vector<int> nums;
	int tmp;
	for(int i=0; i<N;i++){
		cin >> tmp;
		nums.push_back(tmp);
	}
	
	sort(nums.begin(), nums.end());
	
	for(int i=0;i<nums.size();++i)
		cout << nums[i] << '\n';		// endl 대신 개행문자를 사용하면 출력 속도가 빨라진다.  
										// 이걸 모르고 정렬 구현하는 헛짓을 했다. 
		
	return 0;
}
