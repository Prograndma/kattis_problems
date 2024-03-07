package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"unicode"
)

var BASE64 = 29.
var MOD64 = 1_000_000_007.

func charsToArbitraryNumbers64(inStr string) []int64 {
	inStr = strings.TrimSpace(inStr)
	var returnArray = make([]int64, len(inStr))
	for i, char := range inStr {
		if unicode.IsLetter(char) {
			if unicode.IsUpper(char) {
				returnArray[i] = int64(char) - 66 + 28
			} else {
				returnArray[i] = int64(char) - 96
			}
		} else {
			returnArray[i] = int64(char) + 53
		}
	}
	return returnArray
}

func hashy64(inStr string) int64 {
	s := charsToArbitraryNumbers64(inStr)
	var curHash int64 = 0
	for i := 0; i < len(s); i++ {
		curHash = (curHash*int64(BASE64) + s[i]) % int64(MOD64)
	}
	return curHash
}

func rollingHash64(currentChar, maxPow, nextChar, oldHash int64) int64 {
	return ((oldHash-currentChar*maxPow)*int64(BASE64) + nextChar) % int64(MOD64)
}

func compare64(curHash, searchHash int64, writeFile *os.File) bool {
	val := curHash == searchHash
	if writeFile != nil {
		_, err := writeFile.WriteString(strconv.FormatBool(val) + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to rolling hash file")
		}
	}
	return val
}

func whereHashPresent64(inStr string, hashLen int, searchHash int64, writeFile, compareFile *os.File) []int64 {
	if hashLen == 0 {
		a := make([]int64, len(inStr))
		for i := range a {
			a[i] = int64(i)
		}
		return a
	}
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
		curHash = rollingHash64(s[i-hashLen], maxPow, s[i], curHash)
		if writeFile != nil {
			_, err := writeFile.WriteString(strconv.FormatInt(curHash, 10) + "\n")
			if err != nil {
				fmt.Println(err)
				fmt.Println("Error writing to rolling hash file")
			}
		}
		if compare64(curHash, searchHash, compareFile) {
			where = append(where, int64(i-hashLen+1))
		}
	}
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	var lineHash int64
	//file, _ := os.Open("\\string_matching\\input.txt")
	info, infoErr := os.Stdin.Stat()
	//info, infoErr := file.Stat()
	if infoErr != nil {
		panic(infoErr)
	}
	var maxSize int
	scanner := bufio.NewScanner(os.Stdin)
	//scanner := bufio.NewScanner(file)
	maxSize = int(info.Size())
	buffer := make([]byte, 0, maxSize)
	scanner.Buffer(buffer, maxSize)
	for {
		scanner.Scan()
		// Holds the string that scanned
		input := scanner.Text()
		input = strings.TrimSpace(input)
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
			locations := whereHashPresent64(input, lineLen, lineHash, nil, nil)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
		}

	}
}
