#include <iostream>

using namespace std;

int main() {
	int n, d;
	long a, b;
	cin >> n;
	while (n > 0)
	{
		cin >> a >> b;
		d = 0;
		while (a != b) {
			if (a>b) a /= 2;
			else b /= 2;
			d++;
		}
		cout << d << "\n";
		n--;
	}
}