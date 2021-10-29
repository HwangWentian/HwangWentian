#include<bits/stdc++.h>
using namespace std;

int main(){
	while(true){
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		switch(a > b){
			case 1:
				switch(a > c){
					case 1:
						switch(a > d){
							case 1:
								cout << a;
								break;
							case 0:
								cout << d;
								break;
						}
						break;
					case 0:
						switch(c > d){
							case 1:
								cout << c;
								break;
							case 0:
								cout << d;
								break;
						}
						break;
				}
				break;
			case 0:
				switch(b > c){
                    case 1:
                        switch (b > d) {
                            case 1:
                                cout << b;
                                break;
                            case 0:
                                cout << d;
                                break;
                        }
						break;
					case 0:
						switch(c > d){
							case 1:
								cout << c;
								break;
							case 0:
								cout << d;
								break;
						}
						break;
				}
		}
		cout << endl; 
	}
	return 0;
}


