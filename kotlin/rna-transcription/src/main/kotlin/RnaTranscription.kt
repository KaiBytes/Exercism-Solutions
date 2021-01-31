//Learned in this exercise
//Defining body for single expression functions with "="
//Initializing empty array using CharArray(size)
//Using when, a flow control expression

fun transcribeToRna(dna: String): String {
    val transDna = CharArray(dna.length)

    for (i in 0 until dna.length){
        transDna[i] = transDnaComponent(dna[i])
        println(transDna[i])
    }

    return transDna.joinToString("")
}

fun transDnaComponent(dnaComp : Char) : Char =
        when (dnaComp){
            'G' -> 'C'
            'C' -> 'G'
            'T' -> 'A'
            'A' -> 'U'
            else -> throw IllegalArgumentException("Unknown DNA : $dnaComp")
        }