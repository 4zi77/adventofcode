
if __name__ == '__main__':

    with open("input.txt", "r") as f:
        max_id = 0
        ids = []
        for L in f:
            row_val = 0
            col_val = 0
            row = L[:7]
            col = L[7:-1]
            for idx_c, c in enumerate(col):
                if c == 'R':
                    col_val += 2**(2-idx_c)
            for idx_r, r in enumerate(row):
                if r == 'B':
                    row_val += 2**(6-idx_r)
            if 8*row_val+col_val > max_id:
                max_id = 8*row_val+col_val
            ids.append(8*row_val+col_val)
        for i in range(max_id):
            if (i not in ids) and (i-1 in ids) and (i+1 in ids):
                print(i)
