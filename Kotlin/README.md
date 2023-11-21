## Kotlin

**Termux Users only**

**Note: Update repo before installing.**

```bash
apt update -y && apt upgrade -y
```

1. Install by:

```bash
apt install kotlin
```

2. create an app `myapp.kt` with extension `.kt`

```bash
// myapp.kt

fun main() {
    println("Hello, Kotlin")
}
```

3. run

```bash
kotlinc myapp.kt -include-runtime -d myapp.jar \
java -jar myapp.jar
```

`kotlinc` : is an kotlin command. if just type `kotlinc` then an interactive kotlin shell appear.
`myapp.kt` : is script name, that we passing kotlin script.
`-include-runtime` : 
`-d myapp.jar` : 
`java -jar myapp.jar` : this run kotlin program
