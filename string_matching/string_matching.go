package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
	"unicode"
)

var BASE = 29.
var MOD = 1_000_000_007.

func charsToArbitraryNumbers(inStr string) []*big.Int {
	inStr = strings.TrimSpace(inStr)
	var returnArray = make([]*big.Int, len(inStr))
	for i, char := range inStr {
		if unicode.IsLetter(char) {
			if unicode.IsUpper(char) {
				returnArray[i] = big.NewInt(int64(char) - 66 + 28)
			} else {
				returnArray[i] = big.NewInt(int64(char) - 96)
			}
		} else {
			returnArray[i] = big.NewInt(int64(char) + 53)
		}
	}
	return returnArray
}

func hashy(inStr string) *big.Int {
	s := charsToArbitraryNumbers(inStr)
	var curHash = big.NewInt(0)
	for i := 0; i < len(s); i++ {
		//curHash = (curHash*int(BASE) + s[i]) % big.Int(MOD)
		curHash = curHash.Mul(curHash, big.NewInt(int64(BASE)))
		curHash = curHash.Add(curHash, s[i])
		curHash = curHash.Mod(curHash, big.NewInt(int64(MOD)))
	}
	return curHash
}

func rollingHash(currentChar, maxPow, nextChar, oldHash *big.Int) *big.Int {
	var temp = currentChar.Mul(currentChar, maxPow)
	oldHash = oldHash.Sub(oldHash, temp)
	oldHash = oldHash.Mul(oldHash, big.NewInt(int64(BASE)))
	oldHash = oldHash.Add(oldHash, nextChar)
	return oldHash.Mod(oldHash, big.NewInt(int64(MOD)))
}

func compare(curHash, searchHash *big.Int, writeFile *os.File) bool {
	val := curHash.Cmp(searchHash) == 0
	if writeFile != nil {
		_, err := writeFile.WriteString(strconv.FormatBool(val) + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to rolling hash file")
		}
	}
	return val
}

func whereHashPresent(inStr string, hashLen int, searchHash *big.Int, writeFile, compareFile *os.File) []*big.Int {
	//writeFile := getWriteFile("string_matching\\goOutputForRollingHash.txt")
	if hashLen == 0 {
		a := make([]*big.Int, len(inStr))
		for i := range a {
			a[i] = big.NewInt(int64(i))
		}
		return a
	}
	var base = big.NewInt(29)
	var mod = big.NewInt(1_000_000_007)
	maxPow := base.Exp(base, big.NewInt(int64(hashLen-1)), mod)
	var s = charsToArbitraryNumbers(inStr)
	var where []*big.Int
	var curHash = big.NewInt(0)
	for i := 0; i < hashLen; i++ {
		//curHash = (curHash*int(BASE) + s[i]) % big.Int(MOD)
		curHash = curHash.Mul(curHash, big.NewInt(int64(BASE)))
		curHash = curHash.Add(curHash, s[i])
		curHash = curHash.Mod(curHash, big.NewInt(int64(MOD)))
	}
	// since we don't know how big where will be this might be better, we do have an upper limit though.
	// Which is faster? allocating bigger memory? Or dealing with slices?
	if curHash.Cmp(searchHash) == 0 {
		where = append(where, big.NewInt(0))
	}

	for i := hashLen; i < len(s); i++ {
		//curHash = ((curHash-s[i-hashLen]*int(maxPow))*int(BASE) + s[i]) % big.Int(MOD)
		curHash = rollingHash(s[i-hashLen], maxPow, s[i], curHash)
		if writeFile != nil {
			_, err := writeFile.WriteString(curHash.String() + "\n")
			if err != nil {
				fmt.Println(err)
				fmt.Println("Error writing to rolling hash file")
			}
		}

		//var temp = s[i-hashLen].Mul(s[i-hashLen], maxPow)
		//curHash = curHash.Sub(curHash, temp)
		//curHash = curHash.Mul(curHash, big.NewInt(int64(BASE)))
		//curHash = curHash.Add(curHash, s[i])
		//curHash = curHash.Mod(curHash, big.NewInt(int64(MOD)))
		//if curHash == searchHash {
		if compare(curHash, searchHash, compareFile) {
			where = append(where, big.NewInt(int64(i-hashLen+1)))
		}
	}
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	var lineHash *big.Int
	info, infoErr := os.Stdin.Stat()
	if infoErr != nil {
		panic(infoErr)
	}
	var maxSize int
	scanner := bufio.NewScanner(os.Stdin)
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
			lineHash = hashy(input)
			lineLen = len(input)
		} else {
			isPattern = true
			locations := whereHashPresent(input, lineLen, lineHash, nil, nil)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
		}

	}
}
