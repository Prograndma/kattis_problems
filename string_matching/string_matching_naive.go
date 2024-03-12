package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func whereStringPresentGood(input, search string, searchLen int) []int {
	var wherePos = 0
	where := make([]int, len(input))
	for i := 0; i <= len(input)-searchLen; i++ {
		if input[i:i+searchLen] == search {
			where[wherePos] = i
			wherePos++
		}
	}
	return where[:wherePos]
}

func whereStringPresent(input, search string, searchLen int) []int {
	//fmt.Println("Input", input)
	//fmt.Println("search", search)
	//fmt.Println("searchLen", searchLen)
	var searchPos = 0
	var wherePos = 0
	var found = 0
	where := make([]int, int(math.Ceil(float64(len(input))/float64(searchLen))))
	for i := range input {
		if input[i] == search[searchPos] {
			if searchPos < searchLen-1 {
				searchPos++
			} else {
				where[wherePos] = i - searchLen + 1
				wherePos++
				found++
				searchPos = 0
			}
		} else {
			searchPos = 0
		}
	}
	return where[:found]
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
		// Holds the string that scanned
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
