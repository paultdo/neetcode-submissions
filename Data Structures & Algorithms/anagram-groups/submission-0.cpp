class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<int, vector<int>> hash;
        vector<vector<string>> result;
        unordered_set<int> uniques;
        int i = 0;
        for(string word: strs) {
            vector<int> count(26); // a-z

            for(char c : word) {
                count[c - 'a']++;
            }

            hash[i] = count;
            i++;
        }

        for(auto p : hash) {
            vector<string> sub_array;
            if(!uniques.contains(p.first)) {
                sub_array.push_back(strs[p.first]);
                uniques.insert(p.first);
            }

            for(auto d : hash) {
                if(p.first != d.first) {
                    if(d.second == p.second && !uniques.contains(d.first)) {
                        sub_array.push_back(strs[d.first]);
                        uniques.insert(d.first);
                    }
                }
            }
            if(sub_array.size()) {
               result.push_back(sub_array); 
            }
            
        }

        return result;

    }
};
