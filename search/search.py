# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import pacman

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

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
        if (problem.isGoalState(node["state"])):
            break 
        
        for child in problem.getSuccessors(node["state"]):
            if (child[0] not in explore or child[0] not in search_frontier):
                child_node = {} 
                child_node["parent"] = node 
                child_node["action"] = child[1]
                child_node["state"] = child[0]
                search_frontier.add(child_node["state"])
                frontier.push(child_node)
               
        

    while (node["parent"] != None):
        actionList.append(node["action"]) 
        node = node["parent"]


    return list(reversed(actionList))     


    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actionList = list() 
    if (problem.isGoalState(problem.getStartState())):
        return None 

    frontier = util.Queue() 
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
        if (problem.isGoalState(node["state"])):
            break 
       
        for child in problem.getSuccessors(node["state"]):
            if (child[0] not in explore and child[0] not in search_frontier):
                child_node = {} 
                child_node["parent"] = node 
                child_node["action"] = child[1]
                child_node["state"] = child[0]
                search_frontier.add(child_node["state"])
                frontier.push(child_node)
    
    while (node["parent"] != None):
        actionList.append(node["action"]) 
        node = node["parent"]


    return list(reversed(actionList))     


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    actionList = list() 
    if (problem.isGoalState(problem.getStartState())):
        return None 

    frontier = util.PriorityQueue() ;
    explore = set();
    search_frontier = dict() ;
    node = {} ;
    node["parent"] = None 
    node["action"] = None 
    node["state"] =  problem.getStartState() 
    node["cost"] = 0 

    search_frontier[node["state"]] = node["cost"] ;
    
    frontier.push(node,node["cost"]);
    
    while (frontier.isEmpty() == False):
        node = frontier.pop()
        
        if (problem.isGoalState(node["state"])):
            break 
        explore.add(node["state"])
        
        for child in problem.getSuccessors(node["state"]):
            if (child[0] not in explore):
                child_cost = child[2] + node["cost"]     
                if (child[0] not in search_frontier):
                    child_node = {} 
                    child_node["parent"] = node 
                    child_node["action"] = child[1]
                    child_node["state"] = child[0]
                    child_node["cost"] = child_cost 
                    frontier.push(child_node,child_node["cost"])
                    search_frontier[child_node["state"]] = child_node["cost"] 
                else :
                    if (search_frontier[child[0]] > child_cost):
                        child_node = {} 
                        child_node["parent"] = node 
                        child_node["action"] = child[1]
                        child_node["state"] = child[0]
                        child_node["cost"] = child_cost
                        frontier.update(child_node,child_node["cost"])
                        search_frontier[child_node["state"]]  = child_node["cost"]         
            
    while (node["action"] != None):
        actionList.append(node["action"]) 
        node = node["parent"]

    

    return list(reversed(actionList))     

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    actionList = list() 
    if (problem.isGoalState(problem.getStartState())):
        return None 

    frontier = util.PriorityQueue() ;
    explore = set();
    search_frontier = dict() ;
    node = {} ;
    node["parent"] = None 
    node["action"] = None 
    node["state"] =  problem.getStartState() 
    node["g"] = 0 
    node["h"] = heuristic(problem.getStartState(),problem)
    search_frontier[node["state"]] = node["g"] 
    
    frontier.push(node, node["g"] + node["h"]);
    
    while (frontier.isEmpty() == False):
        node = frontier.pop()
        
        if (problem.isGoalState(node["state"])):
            break 
        explore.add(node["state"])
        
        for child in problem.getSuccessors(node["state"]):
            if (child[0] not in explore):
                child_g = child[2] + node["g"]
                child_h = heuristic(child[0],problem)    
                if (child[0] not in search_frontier):
                    child_node = {} 
                    child_node["parent"] = node 
                    child_node["action"] = child[1]
                    child_node["state"] = child[0]
                    child_node["g"] = child_g
                    child_node["h"] = child_h
                    frontier.push(child_node,child_node["g"] + child_node["h"])
                    search_frontier[child_node["state"]] = child_node["g"] 
                else :
                    if (search_frontier[child[0]] > child_g):
                        child_node = {} 
                        child_node["parent"] = node 
                        child_node["action"] = child[1]
                        child_node["state"] = child[0]
                        child_node["g"] = child_g
                        child_node["h"] = child_h
                        frontier.update(child_node,child_node["g"] + child_node["h"])
                        search_frontier[child_node["state"]]  = child_node["g"]         
            
    while (node["action"] != None):
        actionList.append(node["action"]) 
        node = node["parent"]

    

    return list(reversed(actionList))     

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
