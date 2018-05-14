#include <cstdio>
#include <map>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

bool ans( map<int, vector<int> > graph)
{
	map<int, int> in_deg;
	for (map<int, vector<int> >::iterator it = graph.begin(); it != graph.end(); it++)
	{
		int u = it->first;
		if (in_deg.count(u) == 0)
			in_deg[u] = 0;
		vector<int> &vs = graph[u];
		for (int i = 0; i < vs.size(); i++)
		{
			int v = vs[i];
			if(in_deg.count(v) == 0)
				in_deg[v] = 0;
			in_deg[v]++;
		}
		
	}
	int root = 0;
	int cnt = 0;
	map<int, int>::iterator it;
	it = in_deg.begin();
	for(it; it != in_deg.end(); it++)
	{
		if(in_deg[it->first] == 0)
		{
			root = it->first;
			cnt++;
		}
	}
	if(cnt > 1)
	{
		return false;
	}

	cnt = 0;
	it = in_deg.begin();
	for(it; it != in_deg.end(); it++)
	{
		if(in_deg[it->first] > 1)
		{
			cnt++;
		}
	}
	if(cnt > 0)
	{
		return false;
	}

	queue<int> q;
	map<int, bool> vis;
	q.push(root);
	while (!q.empty()) {
		int u = q.front();
		q.pop();
		if(vis[u] == true)
		{
			return false;
		}
		vis[u] = true;
		vector<int> &vs = graph[u];
		for (int i = 0; i < vs.size(); i++) {
			int v = vs[i];
			q.push(v);
		}
	}
	for (map<int, bool>::iterator it = vis.begin(); it != vis.end(); it++)
		if (!it->second) 
			return false;
		
	it = in_deg.begin();
	for(it; it != in_deg.end(); it++)
	{
		if (!vis[it->first]) 
			return false;
	}
	
	return true;
}


int main() {
	int u, v, t = 0;
	scanf("%d %d", &u, &v);
	while (u >= 0) {
		t++;
		map<int, vector<int> > graph;
		while (u > 0) {
			//if (deg.count(u) == 0) deg[u] = 0;
			//if (deg.count(v) == 0) deg[v] = 0;
			graph[u].push_back(v);
			scanf("%d %d", &u, &v);
		}
		bool ok = ans(graph);
		/*
		bool ok = true;
		int root = 0;
		for (map<int, int>::iterator it = deg.begin(); it != deg.end(); it++)
			if (it->second > 1) {
				ok = false;
				break;
			}
			else if (it->second == 0) {
				if (root > 0) {
					ok = false;
					break;
				}
				else root = it->first;
			}
		if (ok) {
		}
		*/
		if (ok) 
			printf("Case %d is a tree.\n", t);
		else 
			printf("Case %d is not a tree.\n", t);
		scanf("%d %d", &u, &v);
	}
}
