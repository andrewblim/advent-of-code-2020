package day02

import org.scalatest._
import flatspec._
import matchers._

class Day02Spec extends AnyFlatSpec with should.Matchers {
  import day02.Day02._

  "PolicyValidation" should "validate under criterion 1" in {
    PolicyValidation(1, 3, 'a', "abcde").validate shouldBe true
    PolicyValidation(1, 3, 'b', "cdefg").validate shouldBe false
    PolicyValidation(2, 9, 'c', "ccccccccc").validate shouldBe true
  }

  "PolicyValidation" should "validate under criterion 2" in {
    PolicyValidation(1, 3, 'a', "abcde").validate2 shouldBe true
    PolicyValidation(1, 3, 'b', "cdefg").validate2 shouldBe false
    PolicyValidation(2, 9, 'c', "ccccccccc").validate2 shouldBe false
  }

  "The Day02 object" should "read policies" in {
    readPolicyAndPassword("1-3 a: abcde") shouldEqual PolicyValidation(1, 3, 'a', "abcde")
    readPolicyAndPassword("1-3 b: cdefg") shouldEqual PolicyValidation(1, 3, 'b', "cdefg")
    readPolicyAndPassword("2-9 c: ccccccccc") shouldEqual PolicyValidation(2, 9, 'c', "ccccccccc")
  }
}
