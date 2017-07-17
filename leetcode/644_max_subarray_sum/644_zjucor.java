/*
 * 只要10-5 精度就好
 */
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
    	int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
    	for(int i : nums) {
    		min = Math.min(min, i);
    		max = Math.max(max, i);
    	}
    	
    	double lo = min, hi = max;
    	while(hi-lo > 1e-6) {
    		double mid = (lo+hi)/2.0;
    		if(ok(nums, k ,mid))
    			lo = mid;
    		else
    			hi = mid;
    	}
    	
    	return lo;
    }

	private boolean ok(int[] nums, int k, double mid) {
		// 数组每个数减去mid，转换为：连续子数组累加大于0
		double[] t = new double[nums.length];
		for(int i=0; i<nums.length; i++)
			t[i] = nums[i] - mid;
		
		double sum = 0;
		for(int i=0; i<k; i++)	sum += t[i];
		if(sum >= 0)	return true;
		
		double min = 0, sum2 = 0;
		for(int i=k; i<t.length; i++) {
			sum2 += t[i-k];
			sum += t[i];
			min = Math.min(min, sum2);
			
			if(sum - min >= 0)	return true;	
		}
		
		return false;
	}
}
