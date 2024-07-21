1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
#include <iostream>
using namespace std;
int main(void) {
    int N, K;
    int P[109], Q[109];
    bool Answer = false;
    // enter
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        cin >> P[i];
    }
    for (int i = 1; i <= N; i++) {
        cin >> Q[i];
    }
    for (int x = 1; x <= N; x++) {
        for (int y = 1; y <= N; y++) {
            if (P[x] + Q[y] == K) {
 