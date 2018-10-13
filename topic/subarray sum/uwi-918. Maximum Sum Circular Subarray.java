class Solution {
	public int maxSubarraySumCircular(int[] A) {
		int n = A.length;
		long[] cum = new long[2*n+1];
		for(int i = 0;i < 2*n;i++){
			cum[i+1] = cum[i] + A[i%n];
		}
		PriorityQueue<long[]> pq = new PriorityQueue<>(
				100000, 
				(x, y) -> Long.compare(x[0], y[0]));
		long max = Long.MIN_VALUE;
		for(int i = 0;i < 2*n;i++){
			if(i-n >= 0){
				while(!pq.isEmpty() && pq.peek()[1] < i-n){
					pq.poll();
				}
				max = Math.max(max, cum[i] - pq.peek()[0]);
			}
			pq.add(new long[]{cum[i], i});
		}
		return (int)max;
	}
}	
