#include <iostream>
#include <string>
#include <vector>
#include <map>

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;


class UnionFind
{   
public:
    vi pset;
    UnionFind(int n){
        for(int i = 0; i < n; i++) pset.push_back(i);
    }
    
    int find_set(int i){
        if(pset[i] == i) return i;

        pset[i] = find_set(pset[i]);
        
        return pset[i];
    }

    void union_set(int i, int j){
        pset[find_set(i)] = find_set(j);
    }

    bool is_same_set(int i, int j){
        if(find_set(i) == find_set(j)) return true;
        return false;
    }
};

int main(){

    int t, n, n_people, people;
    cin >> t;
    
    while(t--){
        map<string, int> map_input;
        vector<pair<string, string > > relation;
        cin >> n;
        n_people = 0;
        for(int i = 0; i < n; i++){
            string s1, s2;
            cin >> s1 >> s2;
            pair<string, string> p(s1, s2);
            relation.push_back(p);
            if(map_input.count(s1) == 0){
                n_people++;
                map_input[s1] = n_people;
            }

            if(map_input.count(s2) == 0){
                n_people++;
                map_input[s2] = n_people;
            }
        }

        UnionFind uf(n_people);
        for(int i = 0; i < relation.size(); i++){
            pair<string, string> p(relation[i]);
            int s1 = map_input[p.first], s2 = map_input[p.second];
            s1--;
            s2--;
            uf.union_set(s1, s2);
            people = 0;
            for(int j = 0; j < uf.pset.size(); j++){
                if(uf.is_same_set(s1, uf.pset[j])) people++;
            }

            cout << people << endl;
        }
    }

    return 0;
}