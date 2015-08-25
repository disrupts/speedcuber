# External dependancy
import numpy as np

# From Python Standard Library
from random import SystemRandom as sysrand
from copy   import deepcopy
from json   import loads as jsonloads
from json   import dump  as jsondump

class Cube:
    """ A simple 3x3x3 Cube solver

    This class stores a cube in memory with each side as a matrix of str.
    Each element in this "list of lists" represents a colour.
    Each side is written as if looking towars that face of the cube.

    Those sides are:   front, back, up, down, left and right.
    Those colours are: 'B' for Blue
                       'W' for White
                       'Y' for Yellow
                       'R' for Red
                       'O' for Orange
                       'G' for Green

    To move the cube, use the self.motion method.
    Those motions are: 'F' for Front clockwise
                       'f' for Front counter-clockwise
                       'B' for Back clockwise
                       'b' for Back countrer-clockwise
                       'U' for Up clockwise
                       'u' for Up countrer-clockwise
                       'D' for Down clockwise
                       'd' for Down countrer-clockwise
                       'L' for Left clockwise
                       'l' for Left countrer-clockwise
                       'R' for Right clockwise
                       'r' for Right countrer-clockwise
    As a general rule, clockwise motions are capitalised.

    Some methods are duplicated, such as self.motion() and self.shuffle()
    The capitalised version (eg: self.MOTION()) overwrites the object
    itself while non-capitalised methods don't modify the object and
    instead return a modified copy.

    It currently lacks a way to check the cube (especially if it is
    loaded from a json textfile) has a possible solution.

    """

    def __init__(self):
        """ Initialse a solved cube and define the rotation array """

        self.front = np.array([['B', 'B', 'B'],
                               ['B', 'B', 'B'],
                               ['B', 'B', 'B']])
        self.up    = np.array([['W', 'W', 'W'],
                               ['W', 'W', 'W'],
                               ['W', 'W', 'W']])
        self.down  = np.array([['Y', 'Y', 'Y'],
                               ['Y', 'Y', 'Y'],
                               ['Y', 'Y', 'Y']])
        self.left  = np.array([['R', 'R', 'R'],
                               ['R', 'R', 'R'],
                               ['R', 'R', 'R']])
        self.right = np.array([['O', 'O', 'O'],
                               ['O', 'O', 'O'],
                               ['O', 'O', 'O']])
        self.back  = np.array([['G', 'G', 'G'],
                                ['G', 'G', 'G'],
                                ['G', 'G', 'G']])
        self.rotation_types = \
              ['F', 'f', 'R', 'r', 'L', 'l', 'U', 'u', 'D', 'd', 'B', 'b']


    def str(self):
        """ Write the cube into a pretty string """

        # Shape of the string
        # print("    xxx        ")
        # print("    xxx        ")
        # print("    xxx        ")
        # print("               ")
        # print("xxx xxx xxx xxx")
        # print("xxx xxx xxx xxx")
        # print("xxx xxx xxx xxx")
        # print("               ")
        # print("    xxx        ")
        # print("    xxx        ")
        # print("    xxx        ")

        cube_str = ""

        cube_str += "    "+self.up[0][0]+self.up[0][1]+self.up[0][2]+"        "+"\n"
        cube_str += "    "+self.up[1][0]+self.up[1][1]+self.up[1][2]+"        "+"\n"
        cube_str += "    "+self.up[2][0]+self.up[2][1]+self.up[2][2]+"        "+"\n"

        cube_str += "               "+"\n"

        cube_str +=  self.left[0][0]+ self.left[0][1]+ self.left[0][2]+" "
        cube_str += self.front[0][0]+self.front[0][1]+self.front[0][2]+" "
        cube_str += self.right[0][0]+self.right[0][1]+self.right[0][2]+" "
        cube_str +=  self.back[0][0]+ self.back[0][1]+ self.back[0][2]+"\n"

        cube_str +=  self.left[1][0]+ self.left[1][1]+ self.left[1][2]+" "
        cube_str += self.front[1][0]+self.front[1][1]+self.front[1][2]+" "
        cube_str += self.right[1][0]+self.right[1][1]+self.right[1][2]+" "
        cube_str +=  self.back[1][0]+ self.back[1][1]+ self.back[1][2]+"\n"

        cube_str +=  self.left[2][0]+ self.left[2][1]+ self.left[2][2]+" "
        cube_str += self.front[2][0]+self.front[2][1]+self.front[2][2]+" "
        cube_str += self.right[2][0]+self.right[2][1]+self.right[2][2]+" "
        cube_str +=  self.back[2][0]+ self.back[2][1]+ self.back[2][2]+"\n"

        cube_str += "               "+"\n"

        cube_str += "    "+self.down[0][0]+self.down[0][1]+self.down[0][2]+"        \n"
        cube_str += "    "+self.down[1][0]+self.down[1][1]+self.down[1][2]+"        \n"
        cube_str += "    "+self.down[2][0]+self.down[2][1]+self.down[2][2]+"        "

        return cube_str

    def is_solved(self):
        """ Returns True if the cube is solved

        It doesn't care about the which center piece is on which side.
        All we'll be considered solved.

        """

        solved = False
        solved_array = []
        solved_array.append(self.is_side_solved(self.front))
        solved_array.append(self.is_side_solved(self.back))
        solved_array.append(self.is_side_solved(self.left))
        solved_array.append(self.is_side_solved(self.right))
        solved_array.append(self.is_side_solved(self.up))
        solved_array.append(self.is_side_solved(self.down))
        if solved_array.count(True) == 6:
            solved = True
        return solved

    def is_side_solved(self, side):
        """ Check if a single side of the Cube is solved """

        solved = True
        core = side[1][1]
        for i in range(3):
            for j in range(3):
                if not core == side[i][j]:
                    solved = False
                    break
            if solved == False:
                break
        return solved

    def motion(self, motion_str):
        """ Non-destructive version of MOTION

        It won't modify the cube but return a copy of it with that move
        applied to it.

        """

        cube_copy = deepcopy(self)
        return copy.MOTION(motion_str)

    def MOTION(self, motion_str):
        """ Apply one move to the Cube

        This motion will modify the cube itself.
        All those motions are: 'F' for Front clockwise
                               'f' for Front counter-clockwise
                               'B' for Back clockwise
                               'b' for Back countrer-clockwise
                               'U' for Up clockwise
                               'u' for Up countrer-clockwise
                               'D' for Down clockwise
                               'd' for Down countrer-clockwise
                               'L' for Left clockwise
                               'l' for Left countrer-clockwise
                               'R' for Right clockwise
                               'r' for Right countrer-clockwise

        """

        # Front clockwise
        if motion_str == 'F':
            # sides movement
            buffer_array    = deepcopy(self.left[:,2])
            self.left[:,2]  = self.down[0]
            self.down[0]    = np_reversed(self.right[:,0])
            self.right[:,0] = self.up[2]
            self.up[2]     = np_reversed(buffer_array)
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.front)

        # Front counter-clockwise
        elif motion_str == 'f':
            # sides movement
            buffer_array    = deepcopy(self.left[:,2])
            self.left[:,2]  = np_reversed(self.up[2])
            self.up[2]     = self.right[:,0]
            self.right[:,0] = np_reversed(self.down[0])
            self.down[0]    = buffer_array
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.front)

        # Back clockwise
        elif motion_str == 'B':
            # sides movement
            buffer_array    = deepcopy(self.up[0])
            self.up[0]     = self.right[:,2]
            self.right[:,2] = np_reversed(self.down[2])
            self.down[2]    = self.left[:,0]
            self.left[:,0]  = np_reversed(buffer_array)
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.back)
        # Back counter-clockwise
        elif motion_str == 'b':
            # sides movement
            buffer_array    = deepcopy(self.up[0])
            self.up[0]     = np_reversed(self.left[:,0])
            self.left[:,0]  = self.down[2]
            self.down[2]    = np_reversed(self.right[:,2])
            self.right[:,2] = buffer_array
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.back)

        # Right clockwise
        elif motion_str == 'R':
            # sides movement
            buffer_column   = deepcopy(self.front[:,2])
            self.front[:,2] = self.down[:,2]
            self.down[:,2]  = np_reversed(self.back[:,0])
            self.back[:,0]  = np_reversed(self.up[:,2])
            self.up[:,2]    = buffer_column
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.right)
        # Right counter-clockwise
        elif motion_str == 'r':
            # sides movement
            buffer_column   = deepcopy(self.front[:,2])
            self.front[:,2] = self.up[:,2]
            self.up[:,2]    = np_reversed(self.back[:,0])
            self.back[:,0]  = np_reversed(self.down[:,2])
            self.down[:,2]  = buffer_column
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.right)

        # Left clockwise
        elif motion_str == 'L':
            # sides movement
            buffer_column   = deepcopy(self.front[:,0])
            self.front[:,0] = self.up[:,0]
            self.up[:,0]    = np_reversed(self.back[:,2])
            self.back[:,2]  = np_reversed(self.down[:,0])
            self.down[:,0]  = buffer_column
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.left)
        # Left counter-clockwise
        elif motion_str == 'l':
            # sides movement
            buffer_column    = deepcopy(self.front[:,0])
            self.front[:,0]  = self.down[:,0]
            self.down[:,0] = np_reversed(self.back[:,2])
            self.back[:,2]   = np_reversed(self.up[:,0])
            self.up[:,0]    = buffer_column
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.left)

        # Up clockwise
        elif motion_str == 'U':
            # sides movement
            buffer_row    = deepcopy(self.front[0])
            self.front[0] = self.right[0]
            self.right[0] = self.back[0]
            self.back[0]  = self.left[0]
            self.left[0]  = buffer_row
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.up)
        # Up counter-clockwise
        elif motion_str == 'u':
            # sides movement
            buffer_row    = deepcopy(self.front[0])
            self.front[0] = self.left[0]
            self.left[0]  = self.back[0]
            self.back[0]  = self.right[0]
            self.right[0] = buffer_row
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.up)

        # Down clockwise
        elif motion_str == 'D':
            # sides movement
            buffer_row    = deepcopy(self.front[2])
            self.front[2] = self.left[2]
            self.left[2]  = self.back[2]
            self.back[2]  = self.right[2]
            self.right[2] = buffer_row
            # face rotation
            self.__FACE_ROTATE_CLOCK(self.down)
        # Down counter-clockwise
        elif motion_str == 'd':
            # sides movement
            buffer_row    = deepcopy(self.front[2])
            self.front[2] = self.right[2]
            self.right[2] = self.back[2]
            self.back[2]  = self.left[2]
            self.left[2]  = buffer_row
            # face rotation
            self.__FACE_ROTATE_COUNTER(self.down)

        else:
            raise(ValueError)

        return self

    def __FACE_ROTATE_CLOCK(self, matrix):
        buffer_int   = matrix[0][0]
        matrix[0][0] = matrix[2][0]
        matrix[2][0] = matrix[2][2]
        matrix[2][2] = matrix[0][2]
        matrix[0][2] = buffer_int

        buffer_int   = matrix[0][1]
        matrix[0][1] = matrix[1][0]
        matrix[1][0] = matrix[2][1]
        matrix[2][1] = matrix[1][2]
        matrix[1][2] = buffer_int

        return matrix

    def __FACE_ROTATE_COUNTER(self, matrix):
        buffer_int = matrix[0][0]
        matrix[0][0] = matrix[0][2]
        matrix[0][2] = matrix[2][2]
        matrix[2][2] = matrix[2][0]
        matrix[2][0] = buffer_int

        buffer_int   = matrix[0][1]
        matrix[0][1] = matrix[1][2]
        matrix[1][2] = matrix[2][1]
        matrix[2][1] = matrix[1][0]
        matrix[1][0] = buffer_int

        return matrix

    def shuffle_moves(self, n):
        """ Outputs a list of n random moves """

        shuffles = []
        for i in range(n):
            shuffles.append(self.rotation_types[sysrand().randrange(0,11)])
        return shuffles

    def SHUFFLE(self, n):
        """ Applies n random moves to the Cube

        It will modify the Cube and return the list of applied moves.

        """

        shuffles = self.shuffle_moves(n)
        for move in shuffles:
            self = self.MOTION(move)
        return shuffles

    def shuffle(self, n):
        """ Non-destructive version of SHUFFLE

        It won't modify the cube but return a shuffled copy of it.
        It returns the modified cube and the list of moves.

        """

        cube_copy = deepcopy(self)
        return cube_copy.SHUFFLE(n), shuffles

    def solve_cpu_singlethread(self):
        """ Solves the Cube and outputs the move list

        It tries all posible motions of increasing movement until the
        Cube is solved.

        It doesn't check if it is a valid cube (that it hasn't beed
        twisted and has no solution with legal motions - without moving
        stickers arround or removing and turning cubies.

        ----------------------------------------------------------------

        This version doesn't keep track of the moves already done to
        the cube while checking moves that are one motion longer
        (eg: it won't store the state of applying 'FlT' to try 'FlTb' or
        any other move that start with 'FlT').
        It is therefore CPU intensive but uses very little memory.

        It could be optimised CPU-wise by separating the execution of
        each different list of motions and checking if the resulting
        cube is solved on independent threads.

        """

        attempts = 1                                   # DEBUG
        moves = self.rotation_types[0]
        while True:
            # check those moves solve the cube
            cube_copy = deepcopy(self)
            for move in moves:
                cube_copy = cube_copy.MOTION(move)
            if cube_copy.is_solved() == True:
                break
            attempts += 1                               #DEBUG

            # Update the moves
            moves, __increased = key_gen(self.rotation_types, moves)
        return moves, attempts

    def solve_mem_singlethread(self):
        """ Solves the Cube and outputs the move list

        It tries all posible motions of increasing movement until the
        Cube is solved.

        It doesn't check if it is a valid cube (that it hasn't beed
        twisted and has no solution with legal motions - without moving
        stickers arround or removing and turning cubies.

        ----------------------------------------------------------------

        This version keeps a dictionary with all the previous moves and
        the state of the cube after those moves.

        It is set to clean-up a bit (could be optimisied much further)
        the dictionary by keeping only the cubes that correspond to the
        list of moves that are of the last 2 length (eg: when the move
        to check moves from 'bb' to 'FFF', all the single-move cube are
        deleted.

        This method could benefit from multithreading in the same way
        as solve_cpu_singlethread(). Check it's documentation for
        further information.

        """

        attempts       = 1                               # DEBUG
        modified_cubes = dict()
        moves          = self.rotation_types[0]
        increased      = False
        while True:
            # check those moves solve the cube,
            # but first get from the dictionary all the moves already done
            truncated_moves = moves[:-1]
            try:
                # The first pass of single moves is done!
                # Only the last motion needs to be applied
                cube_copy = deepcopy(modified_cubes[truncated_moves])
                cube_copy = cube_copy.MOTION(moves[-1])
            except(KeyError):
                # This is a move from the first pass
                cube_copy = deepcopy(self)
                for move in moves:
                    cube_copy = cube_copy.MOTION(move)
                pass

            if cube_copy.is_solved() == True:
                break
            attempts += 1                               #DEBUG

            # adds the new copy to the dictionary
            modified_cubes[moves] = deepcopy(cube_copy)

            # clean up the dictionary
            # not optimised, just deletes all the cubes that are 2 moves
            # shorter than current length (not useful)
            if increased == True:
                length_to_delete = len(moves) - 2
                if length_to_delete >= 1:
                    moves_to_delete = ''
                    for i in range(length_to_delete):
                        moves_to_delete += self.rotation_types[0]
                    while True:
                        del modified_cubes[moves_to_delete]
                        moves_to_delete, break_condition = key_gen(self.rotation_types, moves_to_delete)
                        if break_condition == True:
                            break

            # Update the moves
            moves, increased = key_gen(self.rotation_types, moves)

        return moves, attempts

    def load(self, filename):
        """ Loads a json file into a Cube object

        It reads a text file formated in the same maner self.dump() stores
        the Cube.
        It is a JSON file containing a dictionary with an element for each
        side of the Cube.

        The json modules loads normal python arrays which are then converted
        to numpy arrays.

        """

        file_handle = open(filename, 'r')
        dictionary = jsonloads(file_handle.read())
        file_handle.close()
        self.front = np.array(dictionary["front"])
        self.back  = np.array(dictionary["back"])
        self.left  = np.array(dictionary["left"])
        self.right = np.array(dictionary["right"])
        self.up    = np.array(dictionary["up"])
        self.down  = np.array(dictionary["down"])

    def dump(self, filename):
        """ Stores a Cube object in a json text file

        A dictionary with every side of the cube is written to a text
        file formated in JSON.

        The json module doesn't have support for numpy arrays so those are
        converted to normal python arrays first.

        """


        dictionary = dict()
        dictionary["front"] = [list(elem) for elem in self.front]
        dictionary["back"]  = [list(elem) for elem in self.back]
        dictionary["left"]  = [list(elem) for elem in self.left]
        dictionary["right"] = [list(elem) for elem in self.right]
        dictionary["up"]    = [list(elem) for elem in self.up]
        dictionary["down"]  = [list(elem) for elem in self.down]
        file_handle = open(filename, 'r+')
        jsondump(dictionary, file_handle)
        file_handle.close()


def np_reversed(array):
    """ neversed() for numpy arrays """

    return np.array(list(reversed(array)))

def key_gen(alphabet, key):
    """ Word generator

    Given an alphabet and a word, outputs the next possible word.
    You can see the alphabet as a number base and key_gen() as adding 1
    to a given number.

    """

    first_letter     = alphabet[0]
    last_letter      = alphabet[-1]
    new_key          = ""
    increased_length = False
    if len(key) == key.count(last_letter):
        increased_length = True
        for i in range(len(key)+1):
            new_key += first_letter
    else:
        for letter in list(reversed(key)):
            if letter != last_letter:
                position = len(key) - list(reversed(key)).index(letter) - 1
                new_key = key[:position] + alphabet[alphabet.index(letter)+1]
                for i in range(len(key)-position-1):
                    new_key += first_letter
                break
    return new_key, increased_length

