class Game:
    turn_counter = 0
    active_player = None
    running = True
    board = None

    # Take in board object and assign to game object EG: self.board.update. Gives full access to methods on board object
    def __init__(self, board):
        self.board = board

    # Get player based on turn counter
    def get_player(self):
        print(self.turn_counter)
        if self.turn_counter % 2 == 0:
            return 'X'

        else:
            return 'O'

    # Game logic
    def run_game(self):
        while self.running:

            if self.turn_counter == 0:
                self.board.get()

            active_player = self.get_player()
            print(f"Active player is: {active_player}")
            turn_active = True
            while turn_active:
                grid_position = input("Enter the grid position you would like to put your counter in: ")
                success = self.board.update(grid_position, active_player)
                if success:
                    turn_active = False
                else:
                    print("Place taken, please choose again")

            self.board.get()
            self.board.check_win(active_player)
            self.turn_counter += 1

