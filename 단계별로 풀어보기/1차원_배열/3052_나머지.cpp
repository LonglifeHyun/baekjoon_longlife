/* 

vector에서 remove 와 erase 차이

연속메모리 컨테이너(vector, deque, string)의 경우
v.erase( remove(v.begin(), v.end(), 1234), v.end() );

list 경우, 이 두 작업이 하나로 합쳐진
l.remove(1234);
를 쓰면 된다.

연관 컨테이너(set, map, multi-)의 경우
c.erase(1234);
 
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	vector<int> remains(42,0);
	
	int tmp;
	
	for(int i=0;i<10;++i){
		cin >> tmp;
		remains[tmp%42]++;
	}
	
	remains.erase( remove(remains.begin(), remains.end(), 0), remains.end() );
	
	cout << remains.size() << endl;
	
	return 0;
}
