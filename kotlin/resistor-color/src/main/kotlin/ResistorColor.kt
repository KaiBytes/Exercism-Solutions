object ResistorColor {

    val colorCodeList = listOf("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")

    fun colorCode(input: String): Int {
        return colorCodeList.indexOf(input)
    }

    fun colors(): List<String> {
        return colorCodeList
    }

}
