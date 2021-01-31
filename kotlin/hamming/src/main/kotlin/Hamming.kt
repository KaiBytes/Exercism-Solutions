import java.security.InvalidParameterException

//Object keyword

object Hamming {

    fun compute(leftStrand: String, rightStrand: String): Int {

        var i : Int = 0
        var count : Int = 0

        if (leftStrand.length != rightStrand.length) {
            return throw InvalidParameterException("left and right strands must be of equal length")
        } else {
            while (i < leftStrand.length){
                if (leftStrand[i] != rightStrand[i]){
                    count++
                }
                i++
            }
        }

        return count
    }
}
