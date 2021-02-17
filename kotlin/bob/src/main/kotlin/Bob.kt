object Bob {
    fun hey(input: String): String {
//        val noNumInput = input.filter { it.isLetter() }
        var capitalFlag : Boolean = false
        var lowerCaseFlag : Boolean = false
        var questionFlag : Boolean = false

        for (char in input){
            if (char.isUpperCase()) capitalFlag = true
            if (char.isLowerCase()) lowerCaseFlag  = true
        }

        if (input.contains("?")) questionFlag = true

        if (capitalFlag == true && lowerCaseFlag == false){
            if (lowerCaseFlag == true) return "Whatever."
            if (questionFlag == true) return "Calm down, I know what I'm doing!"
            return "Whoa, chill out!"
        }

        if (lowerCaseFlag == true && capitalFlag == true){
            if (questionFlag == true) return "Sure."
            return "Whatever."
        } else return "Fine. Be that way!"



    }
}
