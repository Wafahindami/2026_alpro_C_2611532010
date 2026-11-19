# papan presensi
# attendance board: 3 mahasiswa x 4 meetings, 0 = absent
board = []
for i in range(3):
    board.append([0] * 4)
board[0][1] = 1
board[2][3] = 1
for row in board:
    print(row)