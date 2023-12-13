# Pallankuzhi (Mancala) :


def move(start):
    if start != 14:
        cur_val = beads[start]
        beads[start] = 0
        start += 1
        for i in range(cur_val):
            if start <= 14:
                beads[start] += 1
            else:
                start = 1
                beads[start] += 1
            start += 1
            print(beads)
        if start > 14:
            start = 1
            cur_val = beads[start]
            next_val = beads[start + 1]
            if next_val != 0:
                move(start + 1)
            else:
                if start >= 12:
                    win = beads[start + 2]
                    beads[start + 2] = 0
                elif start == 13:
                    win = beads[1]
                    beads[1] = 0
                elif start == 14:
                    win = beads[2]
                    beads[2] = 0
        elif start == 14:
            cur_val = beads[start]
            next_val = beads[1]
            if next_val != 0:
                move(1)
            else:
                win = beads[2]
                beads[2] = 0
        else:
            cur_val = beads[start]
            next_val = beads[start + 1]
            if next_val != 0:
                move(start)
        # if start > 14:
        #     start = 1
        #     next_val = beads[start + 1]
        # elif start == 14:
        #     next_val = beads[1]
        # else:
        #     next_val = beads[start + 1]
        # if next_val == 0:
        #     win = beads[start+2]
        # else:
        #     move(start)
    else:
        cur_val = beads[start]
        start = 0
        next_val = beads[1]


beads = {1:5, 2:5, 3:5, 4:5, 5:5, 6:5, 7:5, 8:5, 9:5, 10:5, 11:5, 12:5, 13:5, 14:5}

n = int(input("Enter the key : "))
move(n)