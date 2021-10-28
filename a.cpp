#include<bits/stdc++.h>
using namespace std;
int main(){
	while(true){
		int a, b, c, d, MAX;
		cin >> a >> b >> c >> d;
		switch(a > b){
			case 0:
				switch(a > c){
					case 0:
						switch(a > d){
							case 0:
								cout << a;
								break;
							case 1:
								cout << d;
								break;
						}
					case 1:
						switch(c > d){
							case 0:
								cout << c;
								break;
							case 1:
								cout << d;
								break;
						}
				}
				break;
			case 1:
				switch(b > c){
					case 0:
						switch(b > d){
							case 0:
								cout << b;
								break;
							case 1:
								cout << d;
								break;
						}
					case 1:
						switch(c > d){
							case 0:
								cout << c;
								break;
							case 1:
								cout << d;
								break;
						}
				}
		}
	}
	return 0;
}

