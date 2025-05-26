"""
Author: Suveer Dhawan
Project: Robot Vacuum Simulator

This program simulates a robot vacuum navigating and cleaning a 2D environment. 
It processes instructions such as turning, moving, cleaning, and mopping, while 
handling obstructions and environmental terrain (e.g., dirt, water, soap). The 
logic accounts for multiple robots, logs activity to files, and ensures safe 
navigation around boundaries and obstacles.
"""

cleaning_space = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,"d" ,None,None,None,None,None,None,None],
    [None,None,None,None,"s" ,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,"d" ,None,None,"l" ,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,"l" ,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None]
    ]

obstruction_space = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,"c" ,None,None,None,None,None],
    [None,None,"r" ,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,"w" ,None,None,None],
    [None,None,None,None,"r" ,None,None,None,None,None],
    [None,"w" ,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    ]

# We create a list of vacuum directions which has values in a clockwise manner
vacuum_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

def vacuum_action(vacuum, action):
    '''
    Takes a vacuum list and action and updates the vacuum list according to the action. 

        Parameters:
            vacuum- list containing the state of a vacuum (row, column, direction)
            action- instruction for what the vacuum should do 
        
        Returns:
            action_comp- string of the action the vacuum performed 
        Updates the contents of vacuum, cleaning space, and obstruction lists
    '''

    '''
    We will set up if-else conditional statements to account for all actions.
    We will return a string for action completed. 
    '''
    if action == "turn-left":
        action_comp = turn_left(vacuum)

    elif action == "turn-right":
        action_comp = turn_right(vacuum)

    elif action == "clean":
        if cleaning_space[vacuum[0]][vacuum[1]] == "d":
            cleaning_space[vacuum[0]][vacuum[1]] = None
        
        action_comp = "clean"
    
    elif action == "mop":
        if cleaning_space[vacuum[0]][vacuum[1]] == "l":
            cleaning_space[vacuum[0]][vacuum[1]] = None
        
        action_comp = "mop"

    elif action == "forward":
        action_comp = move_vacuum(vacuum)
        
    return action_comp


def perform_cleaning(instructions, vacuums, logs):
    '''
    Takes instruction file (opens it), vacuums list for several vacuums, and the log file path. 
    It has each vacuum execute the specific action strings destined for it one after the other. 
    
        Parameters:
            instructions- File containing action strings on each line
            vacuums- list containing a list of the state of several vacuums (row, column, direction)
            logs - list containing one file path per vacuum
        
        Returns:
            None
        Updates the contents of vacuums, cleaning space, and obstruction lists.
        And writes the completed actions to the logs list and files.
    '''

    with open(instructions, "r") as inst_ref:
        
        #Reading all lines
        vacuum_lists = inst_ref.readlines()

    #Opening all log files 
    log_files = [open(log_file, "w") for log_file in logs]

    # Looping through each line of instructions
    for vacuum in vacuum_lists:
        
        vac_inst = vacuum.strip().split(" ")

        # Unpacking each line
        vac_index, instructions_list = vac_inst
        vac_index = int(vac_index)
        instructions = instructions_list.split(",")

        # Looping through each instruction for instruction set of a vacuum
        for instruction in instructions:
            action = vacuum_action(vacuums[vac_index], instruction)
            
            log_files[vac_index].write(action + "\n")

    #Closing log files 
    for log_file in log_files:
        log_file.close()


def turn_left(vacuum):
    '''
    Takes the vacuum list as input and performs the turning left action to 
    update the direction that the vacuum is facing. 
    '''
    # We use a for loop and subtract 1 from the index to update the direction 
    # in anti-clockwise manner and use modulo for N to NW
    for index, direction in enumerate(vacuum_directions):
        if vacuum[2] == vacuum_directions[index]:
            vacuum[2] = vacuum_directions[(index-1) % len(vacuum_directions)]

            # break statement stops execution of loop after the turn is completed
            break
    
    return "turn-left"


def turn_right(vacuum):
    '''
    Takes the vacuum list as input and performs the turning right action to 
    update the direction that the vacuum is facing. 
    '''
    # We use a for loop and add 1 to the index to update the direction 
    # in clockwise manner and use modulo for NW to N

    for index, direction in enumerate(vacuum_directions):
        if vacuum[2] == direction:
            vacuum[2] = vacuum_directions[(index+1) % len(vacuum_directions)]

            # break statement stops execution of loop after the turn is completed
            break

    return "turn-right"


def forward(location):
    '''
    Takes a location list as input and executes the forward action to update the 
    object's position

        Parameters:
            location: list containing the state of an object (row, column, direction)
        Returns:
            new_row, new_col: new position of object on the grid 
            None if movememnt would take object out of bounds
    '''
    
    '''
    We use if-else conditional statements to update the object's location 
    based on all possible directions it is facing
    '''
    # Initializing new position of vaucum
    new_row = location[0]
    new_col = location[1]

    if location[2] == "N":
        # decreasing row position by 1 when moving forward
        new_row -= 1

    elif location[2] == "NE":
        # decreasing row by 1 and increasing column by 1
        new_row -= 1
        new_col += 1

    elif location[2] == "E":            
        # increasing column position by 1
        new_col += 1

    elif location[2] == "SE":
        # increasing row and column positions by 1
        new_row += 1 
        new_col += 1
            
    elif location[2] == "S":            
        # increasing row position by 1
        new_row += 1

    elif location[2] == "SW":
        #increasing row by 1 and decreasing column by 1
        new_row += 1
        new_col -= 1

    elif location[2] == "W":
        # decreasing column position by 1
        new_col -= 1

    elif location[2] == "NW":
        # decreasing row and column positions by 1
        new_row -= 1
        new_col -= 1 

    # Ensuring new movememnt is within bounds and updating location
    if 0 <= new_row < len(cleaning_space) and 0 <= new_col < len(cleaning_space[0]):
        return new_row, new_col
    else:
        return None


def move_vacuum(vacuum):
    '''
    Takes the vacuum list as input and ascertains the final position when the instruction is
    forward movememnt. 

        Parameters:
            vacuum: list containing the state of a vacuum (row, column, direction)
        Returns:
            turn-right/turn-left string: if there are obstacles or vacuum would go out of bounds upon movememnt
            forward string: if vacuum is able to succesfully complete forward movement 
    '''
    # Storing intial and new positions of vacuum location after forward function
    initial_row = vacuum[0]
    initial_col = vacuum[1]

    new_position = forward(vacuum)

    # Performing turn right action if forward movement would take the vacuum out of bounds 
    if new_position is None:
        turn_right(vacuum)
        return "turn-right"

    new_row, new_col = new_position

    potential_move = [new_row, new_col, vacuum[2]]

    # Checking obstructions when moving two locations
    action = obstruction_check(potential_move, vacuum)
    
    if action is not None:
        vacuum[0], vacuum[1] = initial_row, initial_col
        return action
    
    '''Movement checks for location attributes'''
    # if vacuum is over dirty space and moves forward
    if cleaning_space[initial_row][initial_col] == "d":
            
        # it smears dirt onto new location if it is clean
        if cleaning_space[new_row][new_col] == None:
            cleaning_space[new_row][new_col] = "d"
            
        # or sets mud in its new location if it has water
        elif cleaning_space[new_row][new_col] == "l":
            cleaning_space[new_row][new_col] = "m"

        # or the new location becomes clean if it had soap
        elif cleaning_space[new_row][new_col] == "s":
            cleaning_space[new_row][new_col] = None
        
    # if vacuum is over water and moves forward
    if cleaning_space[initial_row][initial_col] == "l":
        
        # Checking slipped position when moving two locations
        slip_position = forward(potential_move)

        # Checking out of bounds
        if slip_position is None:
            turn_right(vacuum)
            return "turn-right"
        
        slip_row, slip_col = slip_position
        slipped_move = [slip_row, slip_col, vacuum[2]]
        
        # Checking obstructions when moving two locations
        action = obstruction_check(slipped_move, vacuum)

        if action is not None:
            vacuum[0], vacuum[1] = initial_row, initial_col
            return action

        # if skipped location is clean, water is set
        if cleaning_space[new_row][new_col] == None:
            cleaning_space[new_row][new_col] = "l"

        # if skipped location is dirty, mud is set
        elif cleaning_space[new_row][new_col] == "d":
            cleaning_space[new_row][new_col] = "m"

        # if skipped location has water, water remains
        elif cleaning_space[new_row][new_col] == "l":
            cleaning_space[new_row][new_col] = "l"

        # if skipped location has soap, it becomes clean
        elif cleaning_space[new_row][new_col] == "s":
            cleaning_space[new_row][new_col] = None

        # Vacuum's new location
        new_row, new_col = slip_row, slip_col

    # if vacuum is over soap and moves forward
    if cleaning_space[initial_row][initial_col] == "s":
        
        # Checking slipped position when moving two locations
        slip_position = forward(potential_move)

        # Checking out of bounds
        if slip_position is None:
            turn_right(vacuum)
            return "turn-right"
        
        slip_row, slip_col = slip_position
        slipped_move = [slip_row, slip_col, vacuum[2]]
        
        # Checking obstructions when moving two locations
        action = obstruction_check(slipped_move, vacuum)

        if action is not None:
            vacuum[0], vacuum[1] = initial_row, initial_col
            return action

        # Setting skipped location as clean
        cleaning_space[new_row][new_col] = None

        # Vacuum's new location
        new_row, new_col = slip_row, slip_col
    
    # if vacuum if over mud and moves forward, it smears mud onto new location
    if cleaning_space[initial_row][initial_col] == "m":
        cleaning_space[new_row][new_col] = "m"

    '''Updating vacuum position after all obstruction checks'''
    vacuum[0], vacuum[1] = new_row, new_col

    # Returning forward if the vacuum moved forward
    # And updating the location of robot vacuum in the grid        
    obstruction_space[initial_row][initial_col] = None
    obstruction_space[vacuum[0]][vacuum[1]] = "r"
    return "forward"
    

def obstruction_check(location, vacuum):
    '''
    Takes a location list as input and performs an obstruction check using obstruction_space 
    to ensure the path is clear for the movememnt of the vacuum. 

        Parameters:
            location - list containing the state of an object (row, column, direction)
        Returns:
            action string - turn-right or turn-left if there is an obstacle
            None - if path is clear 
    '''
    new_row = location[0]
    new_col = location[1]
    direction = location[2]

    # if new location would overlap with cat, vacuum turns right instead and 
    # the cat moves forward if the space is clear of obstructions
    if obstruction_space[new_row][new_col] == "c":
        cat = [new_row, new_col, direction]
        
        # Calling function to find new location for the cat
        cat_forward = forward(cat)

        # moving the cat if space is clear of obstructions
        if cat_forward is not None:
            if obstruction_space[cat_forward[0]][cat_forward[1]] == None:
                obstruction_space[new_row][new_col] = None
                obstruction_space[cat_forward[0]][cat_forward[1]] = "c"

        turn_right(vacuum)
        action = "turn-right"
        return action
    
    # if new location would overlap with wall, vacuum turns right instead
    if obstruction_space[new_row][new_col] == "w":
        turn_right(vacuum)
        action = "turn-right"
        return action

    # if new location would overlap with robot, vacuum turns left instead
    if obstruction_space[new_row][new_col] == "r":
        turn_left(vacuum)
        action = "turn-left"
        return action

    return None


# WARNING!!! *DO NOT* REMOVE THIS LINE
# THIS ENSURES THAT THE CODE BELLOW ONLY RUNS WHEN YOU HIT THE GREEN `Run` BUTTON, AND NOT THE BLUE `Test` BUTTON
if __name__ == "__main__":
    test_commands = "test_commands.txt"
    test_logs = ["test_log1.txt","test_log2.txt"]
    vacuums = [
            [2,2,"N"],
            [4,4,"NE"],
        ]

    print("INITIAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if obstruction_space[row_index][col_index] is not None:
                print(obstruction_space[row_index][col_index],end='')
            elif cell is None:
                print(".",end='')
            else:
                print(cell,end='')
        print()

    print("CLEANING")
    perform_cleaning(test_commands,vacuums,test_logs)

    print("FINAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if obstruction_space[row_index][col_index] is not None:
                print(obstruction_space[row_index][col_index],end='')
            elif cell is None:
                print(".",end='')
            else:
                print(cell,end='')
        print()

    print("ACTIONS")
    for log_file in test_logs:
        with open(log_file,"r") as log:
            print(f"FROM: {log_file}")
            print(log.read())