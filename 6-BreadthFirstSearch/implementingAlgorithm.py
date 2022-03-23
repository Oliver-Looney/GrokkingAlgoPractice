from collections import deque
from implementingGraph import graph

def isMangoSeller(name):
    return name[-1] == 'm'

def isAlice(name):
    return name == 'alice'

def breadthFirstSearch(searchGraph, start, targetFunc, successMessage = "target found"):
    searchQueue = deque() # create a new queue
    searchQueue += searchGraph[start] # adds all my neighbors to the queue
    searched = [] # This array is to keep track of which neighbors were searched
    # while searchQueue is not empty
    while searchQueue:
        person = searchQueue.popleft() # gets the first person from the queue
        if not person in searched: # Only search if the person has not been searched
            if targetFunc(person): # checks if the person matches target func
                print(person + " " + successMessage) # YES
                return True
            else: 
                searchQueue += graph[person] # NO - add all their neighbors to the queue
                searched.append(person)
    return False # no target was found

breadthFirstSearch(graph,"you", isMangoSeller, "is mango seller")
breadthFirstSearch(graph, "you", isMangoSeller)
breadthFirstSearch(graph, "you", isAlice)