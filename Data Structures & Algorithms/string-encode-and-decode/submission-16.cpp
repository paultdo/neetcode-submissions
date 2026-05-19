class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for(string s : strs) {
            encoded_string += to_string(s.size());
            encoded_string += '#';
            encoded_string += s;
        }

        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> decoded_strs;
        string new_str = "";
        int i = 0;
        while(i < s.size()) {
            int len = 0;
            while(s[i] != '#') {
                len *= 10;
                len += static_cast<int>(s[i] - '0');
                i++;
            }
            i = i + 1;

            new_str = s.substr(i, len);
            decoded_strs.push_back(new_str);
            i = i + len;
        }

        return decoded_strs;
    }
};
