package curso


object BufferOverflow {
    def overflow(word: Array[Char]): Unit ={
        val buffer: Array[Char] = new Array[Char](8)
        var sing: Int = 0
        val password = "contrase".toArray

        if ((word.deep != password.deep) && word.deep != 8){
            println("Contraseña Incorrecta")
        } else {
            println("Contraseña correcta")
            sing = 1
        }

        if (sing.equals(1)){
            println("Bienvenido")
        }

        // la función copyToArray() por defecto copia únicamente
	// los caractéres que pueda almacenar el array destino
	// evitando así el buffer overflow
        word.copyToArray(buffer)

        for (i <- buffer){
            print(i)
        }
        println("")


    }

    def main(args: Array[String]) = {
        print("Contraseña: ")
        val input = scala.io.StdIn.readLine()

        overflow(input.toArray)
    }
}
