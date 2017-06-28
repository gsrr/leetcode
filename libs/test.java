class Solution {
	    public int kInversePairs(int n, int k) {
	    	long[] dp = new long[k+n];
	    	int mod = 1000000007;
	    	dp[0] = 1;
	    	for(int i = 1;i <= n;i++){
	    		for(int j = dp.length-1-i;j >= 0;j--){
	    			dp[j+i] -= dp[j];
	    			//if(dp[j+i] < 0)dp[j+i] += mod;
	    		}
	    	}
		for(int j = 0;j < dp.length;j++){
			System.out.printf("%d,",dp[j])	;
			
		}

	    	for(int i = 1;i <= n;i++){
	    		for(int j = 0;j < dp.length-1;j++){
	    			dp[j+1] += dp[j];
	    			//dp[j+1] %= mod;
	    		}
	    	}
		System.out.printf("\n")	;
		for(int j = 0;j < dp.length;j++){
			System.out.printf("%d,",dp[j])	;
			
		}
		System.out.printf("\n")	;
	    	return (int)dp[k];
	    }
	}

public class test{
	
	public static void main(String[] args)
	{
		Solution s = new Solution();
		System.out.printf("%d\n",s.kInversePairs(3,1))	;
	}
}
