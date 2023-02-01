class Board:
    grid = {"a1": ' ', "a2": ' ', "a3": ' ',
            "b1": ' ', "b2": ' ', "b3": ' ',
            "c1": ' ', "c2": ' ', "c3": ' '}
    grid_choice = ''
    win_conditions = [['a1', 'a2', 'a3'],
                      ['b1', 'b2', 'b3'],
                      ['c1', 'c2', 'c3'],
                      ['a1', 'b2', 'c3'],
                      ['a3', 'b2', 'c1']]

    def update(self, grid_choice, player_counter: str):
        # Update board at end of turn
        if self.grid[grid_choice] == ' ':
            self.grid[grid_choice] = player_counter
            return True
        else:
            return False

    def get(self):
        # Show board to user
        print(self.grid['a1'] + '|' + self.grid['a2'] + '|' + self.grid['a3'])
        print('-+-+-')
        print(self.grid['b1'] + '|' + self.grid['b2'] + '|' + self.grid['b3'])
        print('-+-+-')
        print(self.grid['c1'] + '|' + self.grid['c2'] + '|' + self.grid['c3'])

    def delete(self):
        # Clear board at end of game
        self.grid.clear()

    def check_win(self, player):
        for row in self.win_conditions:
            # print(f"Checking player {player} for win condition {row}")
            if self.grid[row[0]] == player and self.grid[row[1]] == player and self.grid[row[2]] == player:
                return True
        return False

