//Object keyword
//what is the exact difference between imperative and functional programming??
//idk what the arrow does?

object Hamming {

    fun compute(leftStrand: String, rightStrand: String): Int {
        if (leftStrand.length == rightStrand.length){
            var count = 0;
            leftStrand.zip(rightStrand) { leftStrand, rightStrand -> if (leftStrand != rightStrand) count++ }
            return count
        } else {
            return throw IllegalArgumentException("left and right strands must be of equal length")
        }
    }
}
