

object Hamming {

    fun compute(leftStrand: String, rightStrand: String): Int {
        if (leftStrand.length == rightStrand.length){
             return leftStrand.zip(rightStrand) { leftStrand, rightStrand -> leftStrand != rightStrand }.filter { it == true }.count()
        } else {
            return throw IllegalArgumentException("left and right strands must be of equal length")
        }
    }
}
