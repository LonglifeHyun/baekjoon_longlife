/*
�޸� 2176 KB , �ð� 1572 ms 

�̰� ���������� �޸� 8MB, �ð��� 3�ʿ���. 
�ð��� �� �ɸ����� �޸𸮸� ���� ����� �ſ���. 
�ٵ� �Է� ������ 10^7��. 
�׷��ϱ� �Է°��� �� �޾Ƴ��� �����ϴ� �� �Ұ���. 
10^7 * 4 == 40 MB �̹Ƿ�. 

�׷��� �ذ��� �Է°��� ������ŭ �̸� �迭 ��Ƴ���, 
�Էµɶ����� �ش� �Է°��� �ڸ��� +1 �ϸ� ��. ī��Ʈ �ϴ°�. 
�׷� �Է°��� ������ 10^4�����ϱ� �ִ� 10^4 * 4 == 40 KB 

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

