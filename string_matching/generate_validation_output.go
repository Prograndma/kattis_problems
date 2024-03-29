package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

var PRE = "string_matching\\goOutputFor"
var END = ".txt"
var TEST_FILE = "string_matching\\test_strings.txt"
var TEST_SEARCH_FILE = "string_matching\\test_search_strings.txt"

func listToSpaceSeperatedString(toConvert []*big.Int) string {
	//return strings.Trim(strings.Replace(fmt.Sprint(a), " ", delim, -1), "[]")
	//return strings.Trim(fmt.Sprint(toConvert), "[]")
	return strings.Trim(fmt.Sprint(toConvert), "[]")
}

func getScannerAndReadWriteFiles(readName, writeName string) (*bufio.Scanner, *os.File, *os.File) {
	readFile, err := os.Open(readName)
	if err != nil {
		fmt.Println("ERROR in opening", readName)
		fmt.Println(err)
		panic("Uh oh.")
	}
	writeFile, err := os.Create(writeName)
	if err != nil {
		fmt.Println("ERROR in creating", writeName)
		panic("Uh oh.")
	}

	reader := bufio.NewScanner(readFile)
	const maxCapacity int = 5000000 // your required line length
	buf := make([]byte, maxCapacity)
	reader.Buffer(buf, maxCapacity)
	return reader, readFile, writeFile
}

func generateOutputForCharsToArbitraryNumbers() {
	name := PRE + "charsToArbitraryNumbers" + END
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_FILE, name)
	defer file.Close()
	defer writeFile.Close()

	for reader.Scan() {
		numbers := charsToArbitraryNumbers(reader.Text())
		strResults := listToSpaceSeperatedString(numbers)
		_, err := writeFile.WriteString(strResults + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to file")
		}
	}
	fmt.Println("SUCCESS")
}

func generateOutputForHashy() {
	name := PRE + "Hashy" + END
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_FILE, name)
	defer file.Close()
	defer writeFile.Close()

	for reader.Scan() {
		hashed := hashy(reader.Text())
		_, err := writeFile.WriteString(hashed.String() + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to file")
		}
	}
	fmt.Println("SUCCESS")
}

func getWriteFile(writeName string) *os.File {
	writeFile, err := os.Create(writeName)
	if err != nil {
		fmt.Println("ERROR in creating", writeName)
		fmt.Println(err)
		panic("Uh oh.")
	}
	return writeFile
}

func generateOutputForWhereHashPresent() {
	name := PRE + "WhereHashPresent" + END
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_SEARCH_FILE, name)
	otherWriteFile := getWriteFile(PRE + "RollingHash" + END)
	compareWriteFile := getWriteFile(PRE + "Compare" + END)
	defer file.Close()
	defer writeFile.Close()
	var i = 0
	var hashed *big.Int
	var firstLine string
	var nextLine string
	for reader.Scan() {
		if i%2 == 0 {
			firstLine = strings.TrimSpace(reader.Text())
			hashed = hashy(firstLine)
		} else {
			nextLine = strings.TrimSpace(reader.Text())
			whereResults := whereHashPresent(nextLine, len(firstLine), hashed, otherWriteFile, compareWriteFile)
			where := listToSpaceSeperatedString(whereResults)
			_, err := writeFile.WriteString(nextLine + ", " + strconv.Itoa(len(firstLine)) + ", " + hashed.String() + "\n")
			if err != nil {
				fmt.Println(err)
				fmt.Println("Error writing to file")
			}
			_, err = writeFile.WriteString(where + "\n")
			if err != nil {
				fmt.Println(err)
				fmt.Println("Error writing to file")
			}
		}
		i++
	}
	fmt.Println("SUCCESS")

}

func main() {
	generateOutputForCharsToArbitraryNumbers()
	generateOutputForHashy()
	generateOutputForWhereHashPresent()
}
