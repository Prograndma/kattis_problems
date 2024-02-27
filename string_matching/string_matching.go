package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"unicode"
)

var BASE = 29.
var MOD = 1_000_000_007.

func charsToArbitraryNumbers(inStr string) []*big.Int {
	var returnArray []*big.Int
	for _, char := range inStr {
		if unicode.IsLetter(char) {
			if unicode.IsUpper(char) {
				returnArray = append(returnArray, big.NewInt(int64(char)-66+28))
			} else {
				returnArray = append(returnArray, big.NewInt(int64(char)-96))
			}
		} else {
			returnArray = append(returnArray, big.NewInt(int64(char)+53))
		}
	}
	return returnArray
}

func hashy(inStr string) *big.Int {
	s := charsToArbitraryNumbers(inStr)
	var curHash = big.NewInt(0)
	for i := 0; i < len(inStr); i++ {
		//curHash = (curHash*int(BASE) + s[i]) % big.Int(MOD)
		curHash = curHash.Mul(curHash, big.NewInt(int64(BASE)))
		curHash = curHash.Add(curHash, s[i])
		curHash = curHash.Mod(curHash, big.NewInt(int64(MOD)))
	}
	return curHash
}

func whereHashPresent(inStr string, hashLen int, searchHash *big.Int) []*big.Int {
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
		var temp = s[i-hashLen].Mul(s[i-hashLen], maxPow)
		curHash = curHash.Sub(curHash, temp)
		curHash = curHash.Mul(curHash, big.NewInt(int64(BASE)))
		curHash = curHash.Add(curHash, s[i])
		curHash = curHash.Mod(curHash, big.NewInt(int64(MOD)))
		//curHash -= s[i-hashLen] * big.Int(maxPow)
		//curHash *= big.Int(BASE)
		//curHash += s[i]
		//curHash %= big.Int(MOD)
		//if curHash == searchHash {
		if curHash.Cmp(searchHash) == 0 {
			where = append(where, big.NewInt(int64(i-hashLen+1)))
		}
	}
	return where
}

func main() {
	var isPattern = true
	var lineLen = 0
	var lineHash *big.Int
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
			lineHash = hashy(input)
			lineLen = len(input)
		} else {
			isPattern = true
			locations := whereHashPresent(input, lineLen, lineHash)
			for location := range locations {
				fmt.Print(locations[location], " ")
			}
			fmt.Println("")
		}

	}
}
