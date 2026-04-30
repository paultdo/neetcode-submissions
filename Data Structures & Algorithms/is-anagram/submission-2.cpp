class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_hashmap;
        unordered_map<char, int> t_hashmap;
        for(int i = 0; i < s.size(); i++) {
            if(!s_hashmap.contains(s.at(i))) {
                s_hashmap.insert({s.at(i), 1});
            } else {
                s_hashmap.at(s.at(i))++;
            }
        }

        for(int i = 0; i < t.size(); i++) {
            if(!t_hashmap.contains(t.at(i))) {
                t_hashmap.insert({t.at(i), 1});
            } else {
                t_hashmap.at(t.at(i))++;
            }
        }

        for(auto pair : s_hashmap) {
            if(!t_hashmap.contains(pair.first)) {
                return false;
            }

            if(s_hashmap.at(pair.first) != t_hashmap.at(pair.first)) {
                return false;
            }
        }

        return true;


    }
};
