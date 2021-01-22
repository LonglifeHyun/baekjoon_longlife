/* 

vector���� remove �� erase ����

���Ӹ޸� �����̳�(vector, deque, string)�� ���
v.erase( remove(v.begin(), v.end(), 1234), v.end() );

list ���, �� �� �۾��� �ϳ��� ������
l.remove(1234);
�� ���� �ȴ�.

���� �����̳�(set, map, multi-)�� ���
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
