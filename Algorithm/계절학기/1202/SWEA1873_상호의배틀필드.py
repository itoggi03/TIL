import sys
sys.stdin = open("input.txt", "r")

# x, y좌표가 배열의 인덱스를 넘는지 확인해주는 함수
def check(x, y):
    if x >= 0 and y >= 0 and x < H and y < W:
        return True
    else:
        return False


# 시작 지점에서 입력값에 따라 게임 진행하는 함수
def game(x, y, dir):
    cx, cy = x, y
    cd = dir
    for input_s in input_str:
        # 입력값이 S일 경우
        if input_s == 'S':
            nx, ny = cx + dr[cd], cy + dc[cd]
            while check(nx, ny):
                # 벽일 경우 부수고 while문 끝내기
                if game_map[nx][ny] == '*':
                    game_map[nx][ny] = '.'
                    break
                # 강철일 경우 아무 일도 일어나지 않은채로 while문 끝내기
                elif game_map[nx][ny] == '#':
                    break
                nx += dr[cd]
                ny += dc[cd]

        # 입력값이 U, D, L, R일 경우
        else:
            cd = tank_dir2[input_s]
            game_map[cx][cy] = tank[cd] # 일단 전차 방향 바꾸고
            nx, ny = cx + dr[cd], cy + dc[cd]
            # 그 다음 칸이 평지이면 원래 자리 평지로 만들어주고 다음 칸을 해당 방향 화살표로 바꿔줌
            if check(nx, ny) and game_map[nx][ny] == '.':
                game_map[cx][cy] = '.'
                game_map[nx][ny] = tank[cd]
                cx, cy = nx, ny


# 전차 위치 찾아서 game 시작하는 함수
def start():
    for i in range(H):
        for j in range(W):
            if game_map[i][j] in tank:
                game(i, j, tank_dir[game_map[i][j]])
                return


T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    game_map = [list(input()) for _ in range(H)]
    N = int(input())
    input_str = list(input())

    tank = ['^', 'v', '<', '>']
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    tank_dir = {'^': 0, 'v': 1, '<': 2, '>': 3}
    tank_dir2 = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    start()

    # 출력
    print('#{}'.format(tc), end=' ')
    for i in range(H):
        for j in range(W):
            print(game_map[i][j], end='')
        print()
