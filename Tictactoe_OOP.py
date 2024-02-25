class tictactoe:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1  # Start with player1
        self.dic = {'r1c1' :'+',
                    'r1c2' :'+',
                    'r1c3' :'+',
                    'r2c1' :'+',
                    'r2c2' :'+',
                    'r2c3' :'+',
                    'r3c1' :'+',
                    'r3c2' :'+',
                    'r3c3' :'+'}

    def greet(self):
        print('Let\'s play!!!')
        print('Player 1 is', self.player1)
        print('Player 2 is', self.player2)

    def board(self):
        print(self.dic['r1c1'] + "|" + self.dic['r1c2'] + "|" + self.dic['r1c3'])
        print('-'*5)
        print(self.dic['r2c1'] + "|" + self.dic['r2c2'] + "|" + self.dic['r2c3'])
        print('-'*5)
        print(self.dic['r3c1'] + "|" + self.dic['r3c2'] + "|" + self.dic['r3c3'])

    def play(self):
        self.greet()
        while not self.check_winner() and '+' in self.dic.values():
            self.board()
            print(f"Player {self.current_player}, choose your move (e.g., r1c1 for row 1, column 1): ")
            move = input().lower()
            if move in self.dic and self.dic[move] == '+':
                self.dic[move] = self.current_player
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            else:
                print("Invalid move! Try again.")
        self.board()
        if self.check_winner():
            print(f"Congratulations! Player {self.check_winner()} wins!")
        else:
            print("It's a draw!")

    def check_winner(self):
        rows = [[self.dic[f'r{i}c{j}'] for j in range(1, 4)] for i in range(1, 4)]
        cols = [[self.dic[f'r{j}c{i}'] for j in range(1, 4)] for i in range(1, 4)]
        diags = [[self.dic[f'r{i}c{i}'] for i in range(1, 4)], [self.dic[f'r{i}c{4-i}'] for i in range(1, 4)]]

        all_lines = rows + cols + diags

        for line in all_lines:
            if len(set(line)) == 1 and '+' not in line:
                return line[0]

        return None

# Example usage:
x = tictactoe('X','O')
x.play()
