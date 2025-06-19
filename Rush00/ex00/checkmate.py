# ฟังก์ชันนี้ใช้หาตำแหน่งของหมากทุกตัวบนกระดาน
def find_positions(board):
    P, B, R, Q, K = [], [], [], [], []
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'P':
                P.append([i, j])
            elif piece == 'B':
                B.append([i, j])
            elif piece == 'R':
                R.append([i, j])
            elif piece == 'Q':
                Q.append([i, j])
            elif piece == 'K':
                K = [i, j]
    return K, P, B, R, Q


# ฟังก์ชันนี้เช็คว่า (r, c) อยู่ในขอบเขตของกระดานหรือไม่
def is_in_bounds(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board)


# ฟังก์ชันหลัก ใช้ตรวจสอบว่า King ถูกรุกหรือไม่
def is_in_check(*rows):
    try:
        # แปลง input เป็นกระดาน 2 มิติ เช่น ("..K", "...") → [['.', '.', 'K'], ['.', '.', '.']]
        board = [list(row) for row in rows]

        # หาตำแหน่งของ King, Pawn, Bishop, Rook, Queen
        king, pawns, bishops, rooks, queens = find_positions(board)

        if not king:
            print("Fail")
            return

        # ตรวจสอบว่ามี Pawn รุก King หรือไม่ (โจมตีเฉียงขึ้น)
        for r, c in pawns:
            for dr, dc in [(-1, -1), (-1, 1)]:
                if [r + dr, c + dc] == king:
                    print("Success")
                    return

        # ตรวจสอบ Bishop และ Queen (แนวทแยง)
        for r, c in bishops + queens:
            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                i, j = r + dr, c + dc
                while is_in_bounds(board, i, j):
                    if [i, j] == king:
                        print("Success")
                        return
                    if board[i][j] != '.':
                        break  # เจอหมากอื่นบังทาง
                    i += dr
                    j += dc

        # ตรวจสอบ Rook และ Queen (แนวตรง)
        for r, c in rooks + queens:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = r + dr, c + dc
                while is_in_bounds(board, i, j):
                    if [i, j] == king:
                        print("Success")
                        return
                    if board[i][j] != '.':
                        break
                    i += dr
                    j += dc

        # ไม่มีตัวไหนรุกได้
        print("Fail")

    except:
        pass  # เพื่อป้องกันการ crash จาก input ผิดรูปแบบ