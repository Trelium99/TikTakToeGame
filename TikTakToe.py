class TikTakToe:

    def __init__(self):
        self.answers = {"a1": " ", "a2": " ", "a3": " ",
                        "b1": " ", "b2": " ", "b3": " ",
                        "c1": " ", "c2": " ", "c3": " "}
        self.move_count = 0
        self.win_list_row = ["a", "b", "c"]
        self.win_list_col = ["1", "2", "3"]
        self.flag = True

    def make_board(self):
        board = (f" | 1 | 2 | 3 \n"
                 f" | ---------\n"
                 f"A| {self.answers["a1"]} | {self.answers["a2"]} | {self.answers["a3"]}\n"
                 f" | ---------\n"
                 f"B| {self.answers["b1"]} | {self.answers["b2"]} | {self.answers["b3"]}\n"  
                 f" | ---------\n"
                 f"C| {self.answers["c1"]} | {self.answers["c2"]} | {self.answers["c3"]}")
        print(board)

    def check_win(self, winner):
        self.move_count += 1
        for item in self.win_list_row:
            if self.answers[f"{item}1"] == self.answers[f"{item}2"] and self.answers[f"{item}1"] == self.answers[f"{item}3"] and self.answers[f"{item}1"] != " ":
                print(f"Game Over! {winner} is Winner!")
                self.flag = False

        for item in self.win_list_col:
            if self.answers[f"a{item}"] == self.answers[f"b{item}"] and self.answers[f"a{item}"] == self.answers[f"c{item}"] and self.answers[f"a{item}"] != " ":
                print(f"Game Over! {winner} is Winner!")
                self.flag = False

        if self.answers["a1"] == self.answers["b2"] and self.answers["a1"] == self.answers["c3"] and self.answers["a1"] != " ":
            print(f"Game Over! {winner} is Winner!")
            self.flag = False

        if self.answers["a3"] == self.answers["b2"] and self.answers["a3"] == self.answers["c1"] and self.answers["a3"] != " ":
            print(f"Game Over! {winner} is Winner!")
            self.flag = False

        if self.move_count == 9 and self.flag:
            print("Game over! No more moves available.")
            self.flag = False

        return self.flag

    def update_board(self, player):
        if player == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"

        mark = str(input("Where do you want to place a mark? (e.g:a1):\n").lower())
        if self.answers[mark] == " ":
            self.answers[mark] = player
            self.make_board()
            return self.check_win(winner)
        else:
            print("Invalid Selection. Try again.")
            self.update_board(player)

