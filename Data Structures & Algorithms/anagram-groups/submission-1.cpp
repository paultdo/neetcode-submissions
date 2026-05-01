class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> results;
        for(string word : strs) {
            vector<int> count(26);
            for(char c : word) {
                count[c - 'a']++;
            }
            results[count].push_back(word);
        }

        vector<vector<string>> return_value;

        for(auto i : results) {
            return_value.push_back(i.second);
        }

        return return_value;
    }
};
