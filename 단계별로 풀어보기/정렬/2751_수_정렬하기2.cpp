/*
(1) endl�� ������� ���� �ð� �ʰ� 

(2) endl -> '\n' ���� �� 716ms

(3) �߰����� �ӵ� ������  280ms

	ios::sync_with_stdio(false);	
		c�� ����� �Լ� ��Ʈ�� ����ȭ ����. 
		printf �� cout �� ��� ���� ���� ����Ǵ��� �� �� ���⿡ ȥ�� �Ұ�. 
	
	cin.tie(NULL);
		�⺻������ cin�� cout�� stream  ���۸� ����(tie)�ϰ� �ִ�. 
		��, �Է� �Ǵ� ��� ��û�� �ް� �Ǹ� ������ stream ���۸� Ȯ���ϰ� flush�ϴ� ������ ��ġ�� �ȴ�. 
		�̶�, ���� ��ɾ�� ���� ������ �����ϸ�, 
		����� stream ���۸� ��� Ȯ���ϴ� ������ ��ġ�� �ʱ� ������ �ӵ��� ������ �� �ִ�.  

*/

#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

int main(void)
{
  	ios::sync_with_stdio(false);		// �̰� �ΰ� �������ָ� ����� �ӵ��� ��������. 
  	cin.tie(NULL);						// ��, �̶� scanf, printf �� C�� ����� ����� ����ϸ� �ȵȴ�. 
  	
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
		cout << nums[i] << '\n';		// endl ��� ���๮�ڸ� ����ϸ� ��� �ӵ��� ��������.  
										// �̰� �𸣰� ���� �����ϴ� ������ �ߴ�. 
		
	return 0;
}
