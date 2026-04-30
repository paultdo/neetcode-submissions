class Solution {
public:
    bool isValid(string s) {
        vector<char> stck;
        if(s.size() == 1 || s.size() == 0) {
            return false;
        }
        for(char bracket: s) {
            if(bracket == '(' || bracket == '{' || bracket == '[') {
                stck.push_back(bracket);
            }

            if(stck.size()) {
                if(bracket == ')' && stck.back() == '(') {
                    stck.pop_back();
                } else if(bracket == ')') {
                    return false;
                }

                if(bracket == '}' && stck.back() == '{') {
                    stck.pop_back();
                } else if(bracket == '}') {
                    return false;
                }

                if(bracket == ']' && stck.back() == '[') {
                    stck.pop_back();
                } else if(bracket == ']') {
                    return false;
                }
            } else {
                return false;
            }

        }

        if(stck.size()) {
            return false;
        }

        return true;
    }
};
