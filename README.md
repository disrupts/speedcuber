# speedcuber

## A python module that solves 3x3x3 puzzle cubes


Depends on:
  * [numpy](http://www.numpy.org)

It can load and store cubes from JSON text-files but doesn't test them for
correctness, so solve at your own responsibility.

The solver is single threaded for now and has 2 version:
  * a CPU intensive version that uses minimum memory
  * a memory intensive version that keeps partially solved cubes in memory to
    avoid repetion
