package day01

import org.scalatest._
import flatspec._
import matchers._

class Day01Spec extends AnyFlatSpec with should.Matchers {
  import day01.Day01._

  "The Day01 object" should "find combinations" in {
    val vals = Vector(1721, 979, 366, 299, 675, 1456)
    findSumCombination(vals, 2020, 2) shouldEqual Some(Vector(1721, 299))
    findSumCombination(vals, 2020, 3) shouldEqual Some(Vector(979, 366, 675))
  }
}
