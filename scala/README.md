# advent-of-code-2020 / scala

Scala-based solutions for [Advent of Code, 2020](https://adventofcode.com/2020).

I've just used sbt to build, test, and run everything. To run the code for a day, from sbt, run `runMain dayDD.DayDD "path/to/dayDD/input"`. To run the tests for a day, run `testOnly dayDD.DayDDSpec`.

Under `src/main/scala`, there are directories `dayDD` representing packages for each day. Under each daily directory, there should be at least a file `DayDD.scala` with a `main` method. I expect for most days that'll be all, but in case some problems demand multiple files and classes, they may also be in separate files under the `dayDD` directory.
