package main

import (
	"fmt"
	"unicode"
)

var letters string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \t\n"

func charToArbitraryNumbers(char rune) int {
	if unicode.IsLetter(char) {
		if unicode.IsUpper(char) {
			return int(char) - 66 + 28
		} else {
			return int(char) - 96
		}
	} else {
		return int(char) + 53
	}

}

func main() {
	for i, char := range letters {
		fmt.Println(letters[i], ":", char, "->", charToArbitraryNumbers(char))

	}
}
