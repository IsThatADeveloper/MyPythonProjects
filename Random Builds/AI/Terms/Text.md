# Terms:

## Agent: Entity that perceives its enviornment and acts upon that environment (could be AI or Person trying to find solution)

## State: a config of the agent and its environment 

## Initial state: Where agent starts initially

## Action: Choices that can be made in a state
#### Actions(s) return the set of actions that can be executed in state s (as a function)

## Transition model: Description of what state results from performing any applicable action in any state
#### Results(s,a) returns state resulting from performing action a in state a

## State space: the set of all states reachable from the intial state by any sequence of actions

## Goal test: Way to determine whether a given state is a goal state

## Path cost: Numerical cost associated with a given path

## Optimal solution: A solution that has the lowest path cost among all solutions

(Search Problem)
# Initial state
# Actions
# Transition model 
# Goal test
# Path cost

Node: 
# A data structure that keeps track of: 
## a state
## A parent (node that generated this node)
## An action (action applied to parent to get node)
## A path cost (from inital state to node)