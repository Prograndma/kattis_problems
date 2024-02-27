package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"unicode"
)

var BASE64 = 29.
var MOD64 = 1_000_000_007.

func charsToArbitraryNumbers64(inStr string) []int64 {
	var returnArray []int64
	for _, char := range inStr {
		if unicode.IsLetter(char) {
			if unicode.IsUpper(char) {
				returnArray = append(returnArray, int64(char)-66+28)
			} else {
				returnArray = append(returnArray, int64(char)-96)
			}
		} else {
			returnArray = append(returnArray, int64(char)+53)
		}
	}
	return returnArray
}

func hashy64(inStr string) int64 {
	s := charsToArbitraryNumbers64(inStr)
	var curHash int64 = 0
	for i := 0; i < len(inStr); i++ {
		curHash = (curHash*int64(BASE64) + s[i]) % int64(MOD64)
	}
	return curHash
}

func whereHashPresent64(inStr string, hashLen int, searchHash int64) []int64 {
	tmp := math.Pow(BASE64, float64(hashLen-1))
	tmp = math.Mod(tmp, MOD64)
	maxPow := int64(tmp)
	var s = charsToArbitraryNumbers64(inStr)
	var where []int64
	var curHash int64 = 0
	for i := 0; i < hashLen; i++ {
		curHash = (curHash*int64(BASE64) + s[i]) % int64(MOD64)
	}
	// since we don't know how big where will be this might be better, we do have an upper limit though.
	// Which is faster? allocating bigger memory? Or dealing with slices?
	if searchHash == curHash {
		where = append(where, 0)
	}

	for i := hashLen; i < len(s); i++ {
		curHash -= s[i-hashLen] * maxPow
		curHash *= int64(BASE64)
		curHash += s[i]
		curHash %= int64(MOD64)
		if curHash == searchHash {
			where = append(where, int64(i-hashLen+1))
		}
	}
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	var lineHash int64
	scanner := bufio.NewScanner(os.Stdin)
	for {
		scanner.Scan()
		// Holds the string that scanned
		input := scanner.Text()
		if len(input) == 0 {
			break
		}
		if isPattern {
			//fmt.Println(input)
			isPattern = false
			lineHash = hashy64(input)
			lineLen = len(input)
		} else {
			isPattern = true
			locations := whereHashPresent64(input, lineLen, lineHash)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
		}

	}
}
