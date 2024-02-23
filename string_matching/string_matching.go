package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"unicode"
)

var BASE = 29.
var MOD = 1_000_000_007.

func charsToArbitraryNumbers(inStr string) []int {
	var returnArray []int
	// So I have an idea, don't use this awful slice. You know the length of the array, you have
	// the indices. Use them. Slices are awful. append uses slices! So like yeah. Update this and
	// see what type of performance boost you can get when you're done.
	for _, char := range inStr {
		if unicode.IsUpper(char) {
			returnArray = append(returnArray, int(char)-96)
		} else {
			returnArray = append(returnArray, int(char)-66+26)
		}
	}
	return returnArray
}

func hashy(inStr string) int {
	s := charsToArbitraryNumbers(inStr)
	var curHash = 0
	for i := range len(inStr) {
		curHash = (curHash*int(BASE) + s[i]) % int(MOD)
	}
	return curHash
}

func whereHashPresent(inStr string, hashLen int, searchHash int) []int {
	maxPow := math.Pow(BASE, float64(hashLen))
	maxPow = math.Mod(maxPow, MOD)
	var s = charsToArbitraryNumbers(inStr)
	var where []int
	var curHash int
	//fmt.Println(inStr)
	//fmt.Println(hashLen)
	//fmt.Println(s)
	for i := range hashLen {
		curHash = (curHash*int(BASE) + s[i]) % int(MOD)
	}
	// since we don't know how big where will be this might be better, we do have an upper limit though.
	// Which is faster? allocating bigger memory? Or dealing with slices?
	//fmt.Println(curHash)
	//fmt.Println(searchHash)
	if curHash == searchHash {
		where = append(where, 0)
	}

	for i := hashLen; i < len(s); i++ {
		//curHash = ((curHash-s[i-hashLen]*int(maxPow))*int(BASE) + s[i]) % int(MOD)
		//fmt.Println(i, hashLen, maxPow)
		//fmt.Println(curHash)
		curHash -= s[i-hashLen]
		//fmt.Println(curHash)
		curHash *= int(maxPow)
		//fmt.Println(curHash)
		curHash *= int(BASE)
		//fmt.Println(curHash)
		curHash += s[i]
		//fmt.Println(curHash)
		curHash %= int(MOD)
		//fmt.Println(curHash)
		//fmt.Println(searchHash)
		if curHash == searchHash {
			where = append(where, i-hashLen+1)
		}
	}
	//fmt.Println(where)
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	var lineHash = 0
	//var doneThis = 1
	scanner := bufio.NewScanner(os.Stdin)
	for {
		//var input string
		//_, err := fmt.Scanln(&input)
		scanner.Scan()
		// Holds the string that scanned
		input := scanner.Text()
		//if len(text) != 0 {
		if len(input) == 0 {
			break
		}
		if isPattern {
			isPattern = false
			lineHash = hashy(input)
			lineLen = len(input)
		} else {
			locations := whereHashPresent(input, lineLen, lineHash)
			//fmt.Println(locations)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
			isPattern = true
		}

		//fmt.Println("DONE THIS: ", doneThis, " TIMES")
		//doneThis += 1

	}
}
