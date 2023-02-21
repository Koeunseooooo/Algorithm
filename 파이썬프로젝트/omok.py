OMOK_NUM = 5
BLACK_DOL = 1
WHITE_DOL = 0
BOARD_WIDTH = 10
BOARD_HEIGHT = 10


def boundary(x, y):  # 경계선을 확인하는 함수(지금 당장은 안쓰임)
    if x < BOARD_HEIGHT and x >= 0 and y < BOARD_WIDTH and y >= 0:
        return True
    return False


class PlayBoard:
    def __init__(self):
        self.board = [['.' for i in range(10)]for j in range(10)]

    def printBoard(self):
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                print(self.board[i][j], end='')
            print()
        print()

    def setBoard(self, new_i, new_j, bturn):
        if bturn == BLACK_DOL:
            self.board[new_i][new_j] = BLACK_DOL
        else:
            self.board[new_i][new_j] = WHITE_DOL

    def checkHorizontalOmok(self, new_i, new_j, bturn):
        count = 0
        for j in range(new_j, -1, -1):
            if j < 0:
                break
            if self.board[new_i][j] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        for j in range(new_j+1, new_j + 1 + OMOK_NUM - count):
            if j > BOARD_WIDTH - 1:
                break
            if self.board[new_i][j] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        return False

    def checkVerticalOmok(self, new_i, new_j, bturn):
        count = 0
        for i in range(new_i, -1, -1):
            if i < 0:
                break
            if self.board[i][new_j] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        for i in range(new_i + 1, new_i + 1 + OMOK_NUM - count):
            if i > BOARD_HEIGHT-1:
                break
            if self.board[i][new_j] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        return False

    def checkFirstDiagOmok(self, new_i, new_j, bturn):
        count = 0
        for d in range(0, OMOK_NUM):
            if new_i - d < 0 or new_j + d > BOARD_WIDTH:
                break
            if self.board[new_i - d][new_j + d] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        for d in range(1, OMOK_NUM):
            if new_i + d > BOARD_HEIGHT - 1 or new_j - d < 0:
                break
            if self.board[new_i + d][new_j - d] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        return False

    def checkSecondDiagOmok(self, new_i, new_j, bturn):
        count = 0
        for d in range(0, OMOK_NUM):
            if new_i - d < 0 or new_j - d < 0:
                break
            if self.board[new_i - d][new_j - d] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        for d in range(1, OMOK_NUM):
            if new_i + d > BOARD_HEIGHT - 1 or new_j + d > BOARD_HEIGHT - 1:
                break
            if self.board[new_i + d][new_j + d] == (BLACK_DOL if bturn else WHITE_DOL):
                count += 1
                if count == OMOK_NUM:
                    return True
            else:
                break
        return False

    def checkOmok(self, new_i, new_j, bturn):
        if self.checkHorizontalOmok(new_i, new_j, bturn):
            return True
        elif self.checkVerticalOmok(new_i, new_j, bturn):
            return True
        if self.checkFirstDiagOmok(new_i, new_j, bturn):
            return True
        elif self.checkSecondDiagOmok(new_i, new_j, bturn):
            return True
        else:
            return False


playboard = PlayBoard()

while True:
    x, y, t = map(int, input(
        "x, y좌표 그리고 본인 순서(1,0)를 입력하세요. 1은 흑돌, 0은 백돌입니다").split())
    playboard.setBoard(x, y, t)
    playboard.printBoard()
    if playboard.checkOmok(x, y, t):
        print("끝!")
    # 잘 되는지 확인만 하면 댐
