# Functional Elevators

## The Problem

Given a building with numbered floors, an Elevator that can move between floors (starting on a given floor), and a list of Passengers, who each have a Starting Floor and a Destination Floor, how many "moves" (transitions between floors) does the elevator need to make to deliver them all as efficiently as possible?

We can start with some Assumptions:

• The building has numbered floors, starting at 1, at least as many as the maximum destination of the passengers. (If the highest floor a passenger wants to visit is 6, assume the building has 6 floors.)

• There is a single elevator, that moves from floor to floor. Each movement up or down is one "move".

• _(Let's not worry about the time it takes to open and close doors, or load or unload passengers. And let's assume the elevator can carry all the passengers at once. For now.)_

## The Conceptual Approach:

First, we should discuss the problem: How should we find the shortest path? Let's try doing it on paper (or at least, as a diagram) first.

* What assumptions can we make about possible paths for the elevator to take?

* How many possible paths do we need to consider? What constitutes a valid path?

* What code do we need to write? Try to identify small, functional units of code with "one job"...

## Technical Approach:

Let's try to use the Functional Core, Imperative Shell pattern:

• Most of our code should be in simple functions or units that do one thing well, that does not call other functions!

 • (ideally, they should have as few arguments as possible, not use shared state, and not mutate data...)

• We should have one "high level" function, an "imperative shell" that manages state, and calls our functional units in the right order, with the right arguments. _(It should not do anything else! Any other functionality or business logic should go in new functional units.)_

 • (we can use Typing or Integration Tests to help insure that it works)

Let's also try to practice Test Driven Development:

• Before writing any functional units of code, write a Test first, starting with as small of a "piece" as possible:

 • This Test should initially fail, because the behavior hasn't been implemented (Red)

 • We should write the bare minimum amount of code to make the test pass (Green)

 • Once the Test has Failed, and Passed, consider refactoring the code (Blue)

• Ideally, we should only be writing functional code to make Tests pass.

 • We shouldn't be implementing any behavior that does not have Tests!

## Inputs:

The top level, "imperative shell" should accept two arguments:

* The floor that the Elevator starts on (integer)

* A list of Passengers, each including a Starting Floor (integer) and a Destination Floor (integer)

_(API Updated on 2023-08-14)_
It should return ~the total number of "moves" (movements of the Elevator between floors) required to get all the Passengers to their Destinations as efficiently as possible. (It should probably also return, or at least, print out,~ the intended path of the elevator as it moves between floors, to help us verify that it's working as intended. (We can count this to get the "total moves"!)

## Additional Challenges

We intentionally kept our Elevator Scenario simple to start with. If we get it working, and have more time (and want more challenges), consider adding support for more features. (Ideally, TDD these new features, starting with Tests that fail because they aren't supported yet!)

# 2023-07-10 Session

_(Dave, Tara, Lewis, Fernando)_

## How should we calculate an efficient path for the Elevator?

Given a list of Passengers (each with a starting Floor, and destination floor)

And a Starting Floor (for the elevator)

Calculate the paths, count the moves, determine which path(s) are most efficient

* Given two Passengers, A and B:

 * Consider the moves for getting & delivering them in different orders?

  * (rules for skipping passengers?)

 * Index-based Approach:
    first, calculate step from origin to destination for each passenger
    each floor is an index number
    when we have the distance + index compared to the next passenger  

Deciding a direction - dividing the group of passengers between the ones going up or the ones going down.
Given a list of passengers categorize them into up or down
Function to decide which group to start with.

At some point: How will the data be inputed into the formula?
First define the interface,
then try to make a simple implementation
then ask wether changing the representation of our passenger would make things easier.

Consider a safety check. Are there any passengers that never got picked up and never got let off.

Assume it's as many people as we want.

Let's start by describing the high level interface:

Variables Input
passengers
origin
destination 

Mid Calc Variables

max_destination min_destination
direction
group_up
group_down

## What Code Do We Need to Write?

# 2023-08-14 Session

_(Tara, Dave, Edward, Sam)_

We reviewed the problem, and our work so far...

* Finished implementing `get_highest_floor`/`get_lowest_floor` functions

* Implemented a "Brute Force" solution to compare better solutions against

* _(Refactored tests to use pytest.mark.parametrize!)_

* Recognized the need for a "validation" function:

    * To determine if a solution is valid
   
    * And actually delivers all passengers to destinations...

* Changed our main interface: Solutions now return a verbose list of floor "moves"

    * The length of this list is equivalent to the old "total_moves" return

    * _(And we can now determine if it is valid!)_

* Refactored reference "shell" to use the new interface, passing tests for new return value

* Added `move_elevator`` function that generates a list of moves between any two floors

* Reimplemented `brute_force` using `move_elevator` - less code, and better logging, too!

