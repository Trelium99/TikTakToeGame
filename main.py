import TikTakToe

game = TikTakToe.TikTakToe()
game.make_board()
flag = True
while flag:
    for i in range(2):
        if i == 0:
            player = "X"
        else:
            player = "O"
        flag = game.update_board(player)
        if not flag:
            exit()




