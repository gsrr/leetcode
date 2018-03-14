class Solution {
	    public boolean validTicTacToe(String[] board) {
	        char[] map = new char[9];
	        for(int i = 0;i < 3;i++){
	        	for(int j = 0;j < 3;j++){
	        		map[i*3+j] = board[i].charAt(j);
	        	}
	        }
	        int ox = 0;
	        for(int i = 0;i < 9;i++){
	        	if(map[i] != ' ')ox++;
	        }
	        
	        int[] ord = new int[9];
	        for(int i = 0;i < 9;i++)ord[i] = i;
	        outer:
	        do{
	        	for(int j = 0;j < ox;j++){
	        		if(map[ord[j]] != (j%2 == 0 ? 'X' : 'O')){
	        			continue outer;
	        		}
	        	}
	        	char[] t = new char[9];
	        	Arrays.fill(t, ' ');
	        	for(int j = 0;j < ox-1;j++){
	        		t[ord[j]] = map[ord[j]];
	        		if(end(t))continue outer;
	        	}
	        	return true;
	        }while(nextPermutation(ord));
	        return false;
	    }
	    
	    int[][] q = {
	    		{0, 1, 2},
	    		{3, 4, 5},
	    		{6, 7, 8},
	    		{0, 3, 6},
	    		{1, 4, 7},
	    		{2, 5, 8},
	    		{0, 4, 8},
	    		{2, 4, 6}
	    };
	    
	    boolean end(char[] t)
	    {
	    	for(int[] o : q){
	    		if(t[o[0]] != ' ' && t[o[0]] == t[o[1]] && t[o[1]] == t[o[2]])return true;
	    	}
	    	return false;
	    }
	    
	    public boolean nextPermutation(int[] a) {
			int n = a.length;
			int i;
			for (i = n - 2; i >= 0 && a[i] >= a[i + 1]; i--)
				;
			if (i == -1)
				return false;
			int j;
			for (j = i + 1; j < n && a[i] < a[j]; j++)
				;
			int d = a[i];
			a[i] = a[j - 1];
			a[j - 1] = d;
			for (int p = i + 1, q = n - 1; p < q; p++, q--) {
				d = a[p];
				a[p] = a[q];
				a[q] = d;
			}
			return true;
		}
	}
