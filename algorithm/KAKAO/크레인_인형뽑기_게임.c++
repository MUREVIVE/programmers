#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int temp = 0;
    stack<int> s;
    
    for(int i=0; i<moves.size(); i++) { // 크레인 move 횟수 동안
        for(int j=0; j<board.size(); j++) { // board column 0 ~ 4
            if(board[j][moves[i] - 1] == 0) // 해당 칸이 비어있다면
                continue;
            
            else { // 해당 칸이 비어있지 않다면 
                // s.push(board[j][move[i] - 1]);
                temp = board[j][moves[i] - 1]; // 임시 변수에 해당 인형 정보를 저장.
                board[j][moves[i] - 1] = 0;
                
                // 같은 인형이 붙어있는 경우는 어떻게? 
                if(!s.empty() && s.top() == temp) {
                    // 착각한게 있음. s.pop() 두번을 해야 한다고 생각했었는데, 
                    // 2번째 인형의 경우 s 바구니에 담기 전이다!
                    s.pop(); 
                    answer += 2;
                    
                }
                
                else 
                    s.push(temp);    
                
                break;
            }
            
            
            
                
        }
    }
    
    return answer;
}
