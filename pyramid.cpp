#include <bits/stdc++.h>


using namespace std;

const int maxn = 350 + 15;

inline void Read( int & x ){
    x = 0;
    char ch;
    for( ch = getchar() ; ch < '0' || ch > '9' ; ch = getchar() );
    for( ; ch <= '9' && ch >= '0' ; ch = getchar() ) x = x * 10 + ch - '0';
}

int n , m , K , a[maxn][maxn] , sum[maxn][maxn] , mxrow[maxn][maxn][maxn] , mxcol[maxn][maxn][maxn];

int Query( int x1 , int y1 , int x2 , int y2 ){
    if( x1 > x2 || (x1 == x2 && y1 > y2 ) ) return 0;
    return sum[x2][y2] - sum[x2][y1 - 1] - sum[x1 - 1][y2] + sum[x1 - 1][y1 - 1];
}



int main( int argc , char * argv[] ){
    int cnt = 0;
    int T;
    Read( T );
    while( T -- ){
        Read( n ) , Read( m ) , Read( K );
        int ans = 0;
        for(int i = 1 ; i <= n ; ++ i)
            for(int j = 1 ; j <= m ; ++ j){
                Read( a[i][j] );
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] + a[i][j] - sum[i - 1][j - 1];
            }
        for(int i = 1 ; i <= n ; ++ i)
            for(int j = 1 ; j <= m ; ++ j){
                mxrow[i][j][j] = a[i][j];
                for(int k = j + 1 ; k <= m ; ++ k) mxrow[i][j][k] = max( mxrow[i][j][k - 1] , a[i][k] );
            }
        for(int i = 1 ; i <= m ; ++ i)
            for(int j = 1 ; j <= n ; ++ j){
                mxcol[i][j][j] = a[j][i];
                for(int k = j + 1 ; k <= n ; ++ k) mxcol[i][j][k] = max( mxcol[i][j][k - 1] , a[k][i] );
            }
        for(int i = 1 ; i <= n ; ++ i)
            for(int j = 1 ; j <= m ; ++ j){
                for(int s = max( ans + 1 , max( 1 , a[i][j] ) ) ; i + s - 1 <= n && i - s + 1 >= 1 && j + s - 1 <= m && j - s + 1 >= 1 ; ++ s){
                    int used = 0;
                    for(int k = s , v = 1 ; k >= 1 && used <= K ; -- k , ++ v){
                        int x1 = i - k + 1;
                        int y1 = j - k + 1;
                        int x2 = i + k - 1;
                        int y2 = j + k - 1;
                        int sum = 0;
                        if( mxrow[x1][y1][y2] > v || mxrow[x2][y1][y2] > v || mxcol[y1][x1][x2] > v || mxcol[y2][x1][x2] > v ){
                            used = -1;
                            break;
                        }
                        sum += Query( x1 , y1 , x1 , y2 );
                        sum += Query( x1 + 1 , y1 , x2 , y1 );
                        sum += Query( x1 + 1 , y2 , x2 , y2 );
                        sum += Query( x2 , y1 + 1 , x2 , y2 - 1 );
                        if( k > 1 )
                            used += ( 2 * k - 2 ) * 4 * v - sum;
                        else
                            used += v - sum;
                    }
                    if( used != -1 && used <= K ) ans = s;
                }
            }
        printf( "%d\n" , ans );
    }
    return 0;
}
