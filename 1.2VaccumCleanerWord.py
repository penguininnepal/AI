def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A or B): ").upper()  # Convert to uppercase
    status_input = input(f"Enter status of Room {location_input} (0 for Clean, 1 for Dirty): ")
    status_input_complement = input(f"Enter status of other room (0 for Clean, 1 for Dirty): ")

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print(f"Cost for CLEANING A: {cost}")
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving right to the Location B.")
                cost += 1  # cost for moving right
                print(f"COST for moving RIGHT: {cost}")
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print(f"COST for SUCK: {cost}")
                print("Location B has been Cleaned.")
            else:
                print("No action. Location B is already clean.")
        else:
            print("Location A is already clean.")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B.")
                cost += 1  # cost for moving right
                print(f"COST for moving RIGHT: {cost}")
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print(f"Cost for SUCK: {cost}")
                print("Location B has been Cleaned.")
            else:
                print("No action. Location B is already clean.")
    else:
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print(f"COST for CLEANING B: {cost}")
            print("Location B has been Cleaned.")
            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A.")
                cost += 1  # cost for moving left
                print(f"COST for moving LEFT: {cost}")
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print(f"COST for SUCK: {cost}")
                print("Location A has been Cleaned.")
        else:
            print("Location B is already clean.")
            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A.")
                cost += 1  # cost for moving left
                print(f"COST for moving LEFT: {cost}")
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print(f"COST for SUCK: {cost}")
                print("Location A has been Cleaned.")
            else:
                print("No action. Location A is already clean.")

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()