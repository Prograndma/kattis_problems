package main

import (
	"fmt"
	"unicode"
)

var letters string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func charToArbitraryNumbers(char rune) int {

	if unicode.IsUpper(char) {
		return int(char) - 66 + 28
	} else {
		return int(char) - 96
	}

}

func main() {
	for i, char := range letters {
		fmt.Println(letters[i], ":", char, "->", charToArbitraryNumbers(char))

	}
}
