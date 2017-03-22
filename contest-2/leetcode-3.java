class Solution {
        public:
                bool isRectangleCover(vector<vector<int>>& data) {
                        long long sum = 0;
                        int lx=INT_MAX, ly=INT_MAX, rx=INT_MIN, ry=INT_MIN;

                        map<pair<int, int>, int> mp;
                        mp.clear();

                        for (int i=0; i<data.size(); i++){
                                lx = min(lx, data[i][0]);
                                ly = min(ly, data[i][1]);
                                rx = max(rx, data[i][2]);
                                ry = max(ry, data[i][3]);

                                sum += (long long)(data[i][2]-data[i][0]) * (long long)(data[i][3]-data[i][1]);

                                mp[make_pair(data[i][0], data[i][1])] ++;
                                mp[make_pair(data[i][2], data[i][3])] ++;
                                mp[make_pair(data[i][0], data[i][3])] ++;
                                mp[make_pair(data[i][2], data[i][1])] ++;
                        }

                        if (sum != (long long)(rx-lx) * (long long)(ry-ly)) return false;

                        mp[make_pair(lx, ly)] ++;
                        mp[make_pair(rx, ry)] ++;
                        mp[make_pair(lx, ry)] ++;
                        mp[make_pair(rx, ly)] ++;

                        for (int i=0; i<data.size(); i++){
                                if (mp[make_pair(data[i][0], data[i][1])] == 1) { return false;}
                                if (mp[make_pair(data[i][2], data[i][3])] == 1) { return false;}
                                if (mp[make_pair(data[i][0], data[i][3])] == 1) { return false;}
                                if (mp[make_pair(data[i][2], data[i][1])] == 1) { return false;}
                        }

                        return true;
                }
};
