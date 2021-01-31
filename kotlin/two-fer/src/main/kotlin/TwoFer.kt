//what does internal refer to?
    //Setting a declaration as internal means that it’ll be available in the same module only.
    //By module in Kotlin, we mean a group of files that are compiled together.

//What I learned
//Default values for parameters

internal fun twofer(name: String = "you") = "One for $name, one for me."
