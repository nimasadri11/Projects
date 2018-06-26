 

def start():
    def space():
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Let's play again!")
    from itertools import combinations
    import random
    print ("Use the below guide to play TicTacToe with me!")
    print ("1 2 3")
    print ("4 5 6")
    print ("7 8 9")
    print (" ")
    print ("Get ready!")
    board = []

    for y in range(3):
        board.append(["*"] * 3)

    def print_board(board):
        for row in board:
            print (" ".join(row))
    print_board(board)
    list = [0, 8, 1, 6, 3, 5, 7, 4, 9, 2]
    sl_A = []
    sl_C = [] 
    sum_comp = []
    select_comp = 0
    vl_A = 0
    vl_comp = 0
    r_r = [9,0,0,0,1,1,1,2,2,2]
    c_c = [8,0,1,2,0,1,2,0,1,2]
    corners = [8, 6, 4, 2]
    middles = [1,3,7,9]
    history = []
    sum_tot = 0
    tms = 0
    tms_2 = 0
    m = 0
    sl_x = [8, 1, 6, 3, 5, 7, 4, 9, 2]

    vl_to_num = {8:1, 1:2, 6:3, 3:4, 5:5, 7:6, 4:7, 9:8, 2:9}
    selected_comp = 0

    def lister(nu):
        listing = vl_to_num[nu]
    """win = {[6, 8]:1, [5,9]:1, [4,8]:3, [5,7]:3, [1,5]: 9, [2,4]:9, [2,6]:7, [3,5]:7, [1,9]:5, [3,7]:5, [2,8]:5, [4,6]:5, \
             [1,6]: 8, [2,5] : 8, [3,4]:8, [2,9]:4, [5,6]:4, [3,8]:4, [4,9]:2, [5,8]:2, [6,7]:2, [1,8]:6, [4,5]:6, [2,7]:6}"""

    while sum_tot < 45:
        not_lose = False
        winn = False 
        select_A = int(input("Player 1 turn: "))
        while (select_A in history) or (select_A not in range(10)) or (select_A == 0):
            if select_A in history:
                print ("This position has already been taken.")
                select_A = int(input("Player 1 turn: "))
            elif (select_A not in range(10)) or (select_A == 0):
                print ("Please enter a number between 1 to 9.")
                select_A = int(input("Player 1 turn: "))
        history.append(select_A)
        vl_A = list[select_A]
        sl_A.append(vl_A)
        sl_x.remove(vl_A)
        the_row = r_r[select_A]
        the_col = c_c[select_A]
        board[the_row][the_col] = ("X")

        sum_tot += vl_A
        for r in combinations(sl_A, 3):
            if r[0] + r[1] + r[2] == 15:
                print ("You won!")
                space()
                start()
        if sum_tot == 45:
            print ("Tied!")
            space()
            start()


        for i in combinations(sl_C, 2):
            for s in combinations(sl_x, 1):
                if i[0] + i[1] + s[0] == 15:
                    select_comp = s[0]
                    winn = True 

        if winn == False and ((selected_comp in history) or (selected_comp == 0)):
            for n in combinations(sl_A, 2):
                for z in combinations(sl_x, 1):
                    if n[0] + n[1] + z[0] == 15:
                        select_comp = z[0]
                        not_lose = True
        
             
        if not_lose == False and winn == False and ((selected_comp in history) or (selected_comp == 0)):
            if 5 not in history:
                select_comp = 5 
            else:
                select_comp = random.choice(corners)
                while (corners != [])  and (vl_to_num[select_comp] in history):
                    corners.remove(select_comp)
                    select_comp = random.choice(corners)
                while (corners == []) and (middles != []) and (select_comp in history):
                    select_comp = random.choice(middles)
                    if vl_to_num[select_comp] in history:
                        middles.remove(select_comp)
        sl_C.append(select_comp)
        sum_comp.append(select_comp)
        selected_comp = vl_to_num[select_comp]
        history.append(selected_comp)
        if select_comp in sl_x: 
            sl_x.remove(select_comp)
        the_row = r_r[selected_comp]
        the_col = c_c[selected_comp]
        board[the_row][the_col] = "O"
        print_board(board)
        sum_tot += select_comp

        for j in combinations(sl_C, 3):
            if j[0] + j[1] + j[2] == 15:
                 print ("You Lost!")
                 space()
                 start()
        if sum_tot >= 45:
            print ("Tied!")
            space()
            start()

start()
        


