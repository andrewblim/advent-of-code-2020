package day01

import scala.io.Source

object Day01 {

  def findSumCombination(vals: Vector[Int], target: Int, n: Int): Option[Vector[Int]] = {
    vals.combinations(n).find(_.sum == target)
  }

  def main(args: Array[String]): Unit = {
    val input: Vector[Int] = Source.fromFile(args(0)).getLines.toVector.map(_.toInt)
    println("Part 1:")
    val pair = findSumCombination(input, 2020, 2)
    println(pair)
    println(pair.get.product)
    println("Part 2:")
    val triplet = findSumCombination(input, 2020, 3)
    println(triplet)
    println(triplet.get.product)
  }
}
