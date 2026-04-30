class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_set;
        std::unordered_map<char, int> t_set;

        if(s.size() != t.size()) {
            return false;
        }

        for(int i = 0; i < s.size(); i++) {
            s_set[s.at(i)]++;
        }

        for(int i = 0; i < t.size(); i++) {
            t_set[t.at(i)]++;
        }

        for(std::pair<char, int> combo : s_set) {
            if(s_set[combo.first] != t_set[combo.first]) {
                return false;
            }
        }

        return true;
    }
};
