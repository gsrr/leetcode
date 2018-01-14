class Solution {
public:
    vector<int> partitionLabels(string S) {
        int len=S.size();
	vector<int> res;
	int maxm=0,last=-1;
	for(int i=0;i<len;i++)
	{
		if(i>maxm)
		{
			res.push_back(maxm-last);
			last=i-1;
			maxm=i;
		}
		for(int j=i+1;j<len;j++)
		{
			if(S[j]==S[i])maxm=max(maxm,j);
		}
	}
	res.push_back(len-1-last);
	return res;
    }
};
