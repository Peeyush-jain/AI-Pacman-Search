state = list() ;
state.append((1,4))
state.append((2,3))
state.append((4,5))

print (state)
p = tuple(state)
print (p)
lis = list(p)
print(lis)
x,y = lis[0]
print (x)
lis[0] = (4,5)
print (lis)
print (tuple(lis))

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # create a node which contains parent action state 

    actionList = list() 
    if (problem.isGoalState(problem.getStartState())):
        return None 

    frontier = util.Stack() 
    explore = set()
    search_frontier = set() ;
    node = {} 
    node["parent"] = None 
    node["action"] = None 
    node["state"] =  problem.getStartState() 
    search_frontier.add(node["state"])
    frontier.push(node);
    
    while (frontier.isEmpty() == False):
        node = frontier.pop()
        
        explore.add(node["state"])
        
        
        for child in problem.getSuccessors(node["state"]):
            if (child[0] not in explore):
                child_node = {} 
                child_node["parent"] = node 
                child_node["action"] = child[1]
                child_node["state"] = child[0]
                search_frontier.add(child_node["state"])
                frontier.push(child_node)
        if (problem.isGoalState(node["state"])):
            break         
        

    while (node["parent"] != None):
        actionList.append(node["action"]) 
        node = node["parent"]


    return list(reversed(actionList))     


    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

   corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"
    stateList = list(state)
    if (len(stateList) == 5):
        return 0 
    current_x , current_y = stateList[0]
    visitedCorners = stateList[1:]
    maximum = 0 ;
    for corner in problem.corners :
        if (corner not in visitedCorners):
            goal_x , goal_y = corner    
            maximum = max(maximum,abs(current_x- goal_x) + abs(current_y - goal_y))


while (len(visitedCorners) == 4):
        minimum = float("Inf");
        visit = corners[0]

        for corner in problem.corners :
            if (corner not in visitedCorners):
                goal_x , goal_y = corner    
                dist = abs(current_x- goal_x) + abs(current_y - goal_y)
                if (dist < minimum):
                    minimum = dist
                    x , y = corner 
                    visit = corner


        visitedCorners.append(visit)
        total = total + minimum 
        current_x = x 
        current_y = y 

