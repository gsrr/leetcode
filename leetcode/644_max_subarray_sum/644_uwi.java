public class Solution {
	    public double findMaxAverage(int[] nums, int k) {
	    	double low = -12345, high = 12345;
	    	for(int rep = 0;rep < 100;rep++){
	    		double h = (low+high)/2;
	    		if(ok(h, nums, k)){
	    			low = h;
	    		}else{
	    			high = h;
	    		}
	    	}
	    	return low;
	    }
	    
	    boolean ok(double h, int[] nums, int k){
	    	int n = nums.length;
	        double[] cum = new double[n+1];
	        for(int i = 0;i < n;i++){
	        	cum[i+1] = cum[i] + nums[i] - h;
	        }
	        double min = Double.POSITIVE_INFINITY;
	        for(int i = k-1;i < n;i++){
	        	min = Math.min(min, cum[i-(k-1)]);
	        	if(cum[i+1] - min >= 0)return true;
	        }
	        return false;
	    }
	}	
