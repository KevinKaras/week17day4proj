from tree import Node

class KnightPathFinder:
    def __init__(self, coordinates):
        self._coordinates = coordinates
        self._root = Node(coordinates)
        self._considered_positions = { coordinates }

    def find_path(self, destination):
        path = []
        paths_to_do = 
        #no negative numbers
        

    def get_valid_moves(self, coordinates):
        possible_moves = [
            (-2, -1), 
            (-2, 1), 
            (-1, -2), 
            (-1, 2), 
            (1, -2), 
            (1, 2), 
            (2, -1), 
            (2, 1)
        ]
        valid_moves = []
        current_x, current_y = coordinates
        for possible_x, possible_y in possible_moves:
            new_position = (current_x + possible_x, current_y + possible_y)
            if new_position[0] in range(0, 8) and new_position[1] in range(0, 8):
                valid_moves.append(new_position)
        return valid_moves 



    def new_move_positions(self, )


         




           ( 3 , 3 )



    x  y                x  y
8 ( 1, 4 )          7 ( 1, 2 )    |     ( x - 2, y + 1 )         ( x - 2, y - 1 )
3 ( 5, 4 )          4 ( 5, 2 )    |     ( x + 2, y + 1 )         ( x + 2, y - 1 )
1 ( 2, 5 )          6 ( 2, 1 )    |     ( x - 1, y + 2 )         ( x - 1, y - 2 )
2 ( 4, 5 )          5 ( 4, 1 )    |     ( x + 1, y + 2 )         ( x + 1, y - 2 )

#  #if x, y  are negative, prompt move is not allowed
#         if ( x < 0 , y < 0  ||  (x > 7 || y > 7) ):
#             print("move points to outside of board")

#         #if the numbers aren't negative, check if it's a valid move 
#         if ((coord[0] - dest[0] > -3 / 3) && (coord[1] - dest[1] > -2 / 2))  # check X                # positive side 
        
#         if ()                  # negative side  check Y


#         #if any paths in paths to do = destination.