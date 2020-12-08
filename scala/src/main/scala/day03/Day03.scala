package day03

import scala.io.Source

object Day03 {

  def readMap(input: String): Vector[Vector[Boolean]] = {
    input.split("\n").toVector.map(_.toVector.map(_ == '#'))
  }

  def sledTrees(treeMap: Vector[Vector[Boolean]], start: (Int, Int), step: (Int, Int)): Int = {
    val rows = treeMap.length
    val cols = treeMap(0).length
    val xs = Iterator.from(start._1, step._1)
    val ys = Iterator.from(start._2, step._2)
    val stops =
      (xs zip ys takeWhile({ case (x, y) => x >= 0 && y >= 0 && y < rows })).toList
    stops.map({ case (x, y) => if (treeMap(y)(x % cols)) 1 else 0 }).sum
  }

  def main(args: Array[String]): Unit = {
    val input: String = Source.fromFile(args(0)).mkString
    val treeMap = readMap(input)
    println("Part 1:")
    println(sledTrees(treeMap, (0, 0), (3, 1)))
    println("Part 2:")
    val slopes = List((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    val treeHits = slopes.map(sledTrees(treeMap, (0, 0), _))
    println(treeHits)
    println(treeHits.map(_.toLong).product)
  }
}
