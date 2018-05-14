#include <cstdio>  
#include <cstring>  
const int maxn = 110;  
int cas, v, e, M;  
bool g[maxn][maxn];  
int color[maxn], rec[maxn];  
int gcnt = 0;
  
void dfs(int p, int black) {  
    if (p > v) {
	gcnt += 1;
	printf("%d\n", gcnt);
        if (M < black) {  
            M = black;  
            for (int i = 1; i <= v; i++)  
                rec[i] = color[i];  
        }  
        return;  
    }  
    //judge if can color  
    for (int i = 1; i <= v; i++)  
        if (g[p][i] && color[i]) {  
            dfs(p + 1, black);      //can't color black, color white and return  
            return;  
        }  
    color[p] = 1;  
    dfs(p + 1, black + 1);      //can color black  
    color[p] = 0;  
    dfs(p + 1, black);          //can color white  
}  
  
int main() {  
    scanf("%d", &cas);  
    while (cas--) {  
        M = 0;  
        scanf("%d%d", &v, &e);  
        memset(g, 0, sizeof(g));  
        for (int i = 0; i < e; i++) {  
            int a, b;  
            scanf("%d%d", &a, &b);  
            g[a][b] = g[b][a] = 1;  
        }  
        dfs(1, 0);  
        printf("%d\n", M);  
        int cnt = 0;  
        for (int i = 1; i <= v; i++)  
            if (rec[i]) {  
                if (++cnt != M)  
                    printf("%d ", i);  
                else  
                    printf("%d\n", i);  
            }  
    }  
    return 0;  
}  
