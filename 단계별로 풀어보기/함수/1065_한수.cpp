#include <iostream>
#include <string>

using namespace std;

int find_han_num(int n)
{
	int cnt=0;
	for(int i=111;i<=n;++i){
		string tmp = to_string(i);
		int fst_dif = int(tmp[0])-int(tmp[1]);
		int snd_dif = int(tmp[1])-int(tmp[2]);
		if(fst_dif == snd_dif)
			cnt++;
	}
	return cnt;
}

int main(void)
{
	int N, han_num;
	cin >> N;
	
	if(N < 100)
		han_num = N;
	else if(100<= N && N < 111)
		han_num = 99;
	else
		han_num = 99 + find_han_num(N);

	cout << han_num << endl;
	return 0;
}
