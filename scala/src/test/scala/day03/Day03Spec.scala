package day03

import org.scalatest._
import flatspec._
import matchers._

class Day03Spec extends AnyFlatSpec with should.Matchers {
  import day03.Day03._

  "The Day03 object" should "count sledded trees" in {
    val treeMapData = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
    """.strip
    val treeMap = readMap(treeMapData)
    sledTrees(treeMap, (0, 0), (1, 1)) shouldEqual 2
    sledTrees(treeMap, (0, 0), (3, 1)) shouldEqual 7
    sledTrees(treeMap, (0, 0), (5, 1)) shouldEqual 3
    sledTrees(treeMap, (0, 0), (7, 1)) shouldEqual 4
    sledTrees(treeMap, (0, 0), (1, 2)) shouldEqual 2
  }
}
