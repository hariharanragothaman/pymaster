#include <bits/stdc++.h>
using namespace std;

/*
    SET vs UNORDERED_SET:
    - set<int>: O(log n) insert/search, Red-Black Tree, NO hash collisions
    - unordered_set<int>: O(1) avg, O(n) worst, Hash Table, vulnerable to adversarial input
    - CSES has anti-hash test cases → DEFAULT TO set<> for uniqueness
    - Use unordered_set ONLY if: (1) time is critical AND (2) you add custom hash

    MAP vs UNORDERED_MAP:
    - map<int,int>: O(log n), Red-Black Tree, guaranteed performance
    - unordered_map<int,int>: O(1) avg, O(n) worst, can be attacked
    - CSES default: use map<>

    WHEN RED-BLACK TREE (set/map) BEATS HASH TABLE:
    - Adversarial/crafted inputs (CSES test #15 on Distinct Numbers)
    - Need sorted order as bonus
    - Need guaranteed O(log n) performance
    - Small datasets where O(log n) ≈ O(1) anyway
*/

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    set<int> S;
    int x;
    for (int i = 0; i < n; i++) {
        cin >> x;
        S.insert(x);
    }
    cout << S.size() << '\n';
    return 0;
}
