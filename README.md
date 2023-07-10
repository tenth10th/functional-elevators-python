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

* A list of Passengers, each including a Starting Floor (integer) and a Destination fFloor (integer)

It should return the total number of "moves" (movements of the Elevator between floors) required to get all the Passengers to their Destinations as efficiently as possible. (It should probably also return, or at least, print out, the intended path of the elevator as it moves between floors, to help us verify that it's working as intended.)

## Additional Challenges

We intentionally kept our Elevator Scenario simple to start with. If we get it working, and have more time (and want more challenges), consider adding support for more features. (Ideally, TDD these new features, starting with Tests that fail because they aren't supported yet!)

