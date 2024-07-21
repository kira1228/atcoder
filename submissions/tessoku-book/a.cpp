1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#include <iostream>
    using namespace std;
int main() {
  int N;
  int A[109];
  bool Answer = false;
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> A[i];
  }
  for (int i = 1; i <= N; i++) {
    for (int j = i + 1; j <= N; j++) {
      for (int k = j + 1; k <= N; k++) {
        if (A[i] + A[j] + A[k] == 1000) {
          Answer = true;
        }
