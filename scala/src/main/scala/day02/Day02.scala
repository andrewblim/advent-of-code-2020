package day02

import scala.io.Source
import scala.util.matching.Regex

case class PolicyValidation(p1: Int, p2: Int, letter: Char, password: String) {

  def validate() = {
    val occurrences = password.filter(_ == letter).length
    p1 <= occurrences && occurrences <= p2
  }

  def validate2() = {
    val x1 = p1 <= password.length && password(p1-1) == letter
    val x2 = p2 <= password.length && password(p2-1) == letter
    x1 != x2
  }
}

object Day02 {

  def readPolicyAndPassword(input: String): PolicyValidation = {
    val info = raw"(\d+)-(\d+) (\w)\: (\w+)".r
    input match {
      case info(lower, upper, letter, password) =>
        new PolicyValidation(lower.toInt, upper.toInt, letter(0), password)
    }
  }

  def main(args: Array[String]): Unit = {
    val input: Vector[PolicyValidation] =
      Source.fromFile(args(0)).getLines.toVector.map(readPolicyAndPassword(_))
    println("Part 1:")
    println(input.filter(_.validate).length)
    println("Part 2:")
    println(input.filter(_.validate2).length)
  }
}
