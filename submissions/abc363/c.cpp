1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
    using namespace std;
// 全ての順列を生成する関数
set<string> all_permutations(string str) {
  set<string> perm_set;
  sort(str.begin(), str.end());
  do {
    perm_set.insert(str);
  } while (next_permutation(str.begin(), str.end()));
  return perm_set;
}
// 回文チェック関数
bool is_palindrome(const string &s) {
