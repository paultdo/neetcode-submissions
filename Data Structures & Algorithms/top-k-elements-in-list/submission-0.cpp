class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> num_count;
        vector<vector<int>> buckets(nums.size() + 1);
        unordered_set<int> added_nums;
        vector<int> result;
        for(int i : nums) {
            num_count[i]++;
        }

        for(auto duo : num_count) {
            buckets[duo.second].push_back(duo.first);
        }

        for(int i = buckets.size() - 1; i >= 0; i--) {
            if(k == 0) {
                break;
            }
            for(int j = buckets[i].size() - 1; j >= 0; j--) {
                if(!added_nums.contains(buckets[i][j])) {
                    added_nums.insert(buckets[i][j]);
                    k--;
                    if(k == 0) {
                        break;
                    }
                }
            }
        }

        for(int i : added_nums) {
            result.push_back(i);
        }

        return result;
    }
};
