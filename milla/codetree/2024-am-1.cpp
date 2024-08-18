#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define N_length 5
#define R_length 3

using namespace std;


int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int arr[N_length][N_length]={0,};
int K, M;
int ans=0; // 최종 결과값
queue<int> WALLS; // 벽면의 정보는 첫번째부터 꺼내어 쓰므로 자료형 큐를 사용한다

void input(void){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> K >> M;

    for(int i=0;i<N_length;i++){
        for (int j=0;j<N_length;j++){
            cin >> arr[i][j];
        }
    }

    for (int i=0;i<M;i++){
        int tmp;
        cin >> tmp;
        WALLS.push(tmp);
    }

    // 2 20
    // 7 6 7 6 7
    // 6 7 6 7 6
    // 6 7 1 5 4
    // 7 6 3 2 1
    // 5 4 3 2 7
    // 3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3

}

void print_input(){
    cout << "K:" << K << " M:" << M << "\n";
    cout << "===arr 시작==" << '\n';
    for (int i=0;i<N_length;i++){
        for (int j=0;j<N_length;j++){
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << "===WALLS 시작==" << "\n";
    queue<int> tmp(WALLS); // 큐 복사
    while(!tmp.empty()){
        cout << tmp.front() << ' ';
        tmp.pop();
    }
    cout << "===WALLS 끝==" << "\n";
}

void print_rotateArr(int rotate_arr[N_length][N_length]){
    cout << "===rotate arr 시작==" << '\n';
    for (int i=0;i<N_length;i++){
        for (int j=0;j<N_length;j++){
            cout << rotate_arr[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << "===rotate arr 끝==" << "\n";
    cout << "\n";
}
struct Cmp {
	bool operator()(pair<int, int>a, pair<int, int>b) {
		if (a.second != b.second) {
			return a.second > b.second;
		}
		return a.first < b.first;
	}
};
struct info {
	int value, rot, row, col; // 가치(크), 각도(작), 열(작), 행(작)
	priority_queue<pair<int, int>,vector<pair<int,int>>,Cmp> pq;
};

info calValue(int arr[][5], int row, int col, int rot) {
	queue<pair<int, int>> q;
	priority_queue<pair<int, int>, vector<pair<int, int>>, Cmp> pq;

	bool visited[5][5] = { false, };
	int value = 0;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			queue<pair<int, int>> q2;
			if (visited[i][j])continue;
			q.push({ i,j });
			q2.push({ i,j });
			visited[i][j] = true;
			int cnt = 1;
			while (!q.empty()) {
				int cy = q.front().first;
				int cx = q.front().second;
				int cv = arr[cy][cx];
				q.pop();
				for (int k = 0; k < 4; k++) {
					int ny = cy + dy[k];
					int nx = cx + dx[k];
					if (visited[ny][nx])continue;
					if (!isValid(ny, nx))continue;
					int nv = arr[ny][nx];
					if (cv != nv)continue;
					q.push({ ny,nx });
					q2.push({ ny,nx });
					visited[ny][nx] = true;
					cnt++;
				}
			}
			if (cnt >= 3) {
				value += cnt;
				while (!q2.empty()) {
					pq.push(q2.front());
					q2.pop();
				}
			}
		}
	}
	info result = { value, rot, row, col, pq};
	return result;
}


bool isPossibleToHaveTreasure(){ // 가능하면서,, 가장 최대화할 수 있는 좌표로 회전해야함
    // 모든 회전에 대해 우선순위로 정렬
	priority_queue<info, vector<info>, Cmp1> pq;
	info v = {};

    for (int i=0;i<R_length;i++){
        for (int j=0;j<R_length;j++){
            // 원본 배열 복사 (더 효율적인 방법 찾아보기)
            int copy_arr[5][5] = { 0, };
			for (int i = 0; i < 5; i++) {
				for (int j = 0; j < 5; j++) {
					copy_arr[i][j] = arr[i][j];
				}
			}
            int sy = i;
            int sx = j;

            
            for (int k=0;k<3;k++){ //90,180,270 차례로 회전할 예정
                int ccopy_arr[5][5] = {0, };
                for (int i = 0; i < 5; i++) {
                    for (int j = 0; j < 5; j++) {
                        ccopy_arr[i][j] = copy_arr[i][j];
                    }
			    }
                // 실제 회전 (copy_arr 값을 궁극적으로 바꾸는 것임)
                for (int y = 0; y<3; y++) {
                    for (int x = 0; x < 3; x++) {
                        copy_arr[y+sy][x+sx]=ccopy_arr[(2-x)+sy][y+sx];
                    }
			    }
                //print_rotateArr(copy_arr);
                v = calValue(copy_arr, sy, sx, k);
				pq.push(v);
            }
        }
    }
    return true;
}

void solve(){
    
    for(int i=0;i<K;i++){
        // 유물 획득 가능 여부 판단 
        if(isPossibleToHaveTreasure()){
            // 유물 획득 과정 시작
            //findTresure();
            cout << "fin";
            break;
        }
        else{
            cout << ans;
        }
    }
    // return true // 사실상 의미없는 return 값
    
}
int main(void){
    input();
    //print_input();
    solve();

}