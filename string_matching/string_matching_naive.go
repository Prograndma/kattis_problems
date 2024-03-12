package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func whereStringPresentGood(input, search string, searchLen int) []int {
	var where []int
	for i := 0; i <= len(input)-searchLen; i++ {
		if input[i:i+searchLen] == search {
			where = append(where, i)
		}
	}
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	info, infoErr := os.Stdin.Stat()
	if infoErr != nil {
		panic(infoErr)
	}
	var maxSize int
	scanner := bufio.NewScanner(os.Stdin)
	maxSize = int(info.Size())
	buffer := make([]byte, 0, maxSize)
	scanner.Buffer(buffer, maxSize)
	var search string
	for {
		scanner.Scan()
		input := scanner.Text()
		input = strings.TrimSpace(input)
		if len(input) == 0 {
			break
		}
		if isPattern {
			isPattern = false
			search = input
			lineLen = len(input)
		} else {
			isPattern = true
			locations := whereStringPresentGood(input, search, lineLen)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
		}

	}
}
