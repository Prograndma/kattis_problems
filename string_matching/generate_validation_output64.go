package main

import (
	"fmt"
	"strconv"
	"strings"
)

var END64 = "64.txt"

func listToSpaceSeperatedString64(toConvert []int64) string {
	return strings.Trim(fmt.Sprint(toConvert), "[]")
}

func generateOutputForCharsToArbitraryNumbers64() {
	name := PRE + "charsToArbitraryNumbers" + END64
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_FILE, name)
	defer file.Close()
	defer writeFile.Close()

	for reader.Scan() {
		numbers := charsToArbitraryNumbers64(reader.Text())
		strResults := listToSpaceSeperatedString64(numbers)
		_, err := writeFile.WriteString(strResults + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to file")
		}
	}
	fmt.Println("SUCCESS")
}

func generateOutputForHashy64() {
	name := PRE + "Hashy" + END64
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_FILE, name)
	defer file.Close()
	defer writeFile.Close()

	for reader.Scan() {
		hashed := hashy64(reader.Text())
		_, err := writeFile.WriteString(strconv.FormatInt(hashed, 10) + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to file")
		}
	}
	fmt.Println("SUCCESS")
}

func generateOutputForWhereHashPresent64() {
	name := PRE + "WhereHashPresent" + END64
	reader, file, writeFile := getScannerAndReadWriteFiles(TEST_SEARCH_FILE, name)
	otherWriteFile := getWriteFile(PRE + "RollingHash" + END64)
	compareWriteFile := getWriteFile(PRE + "Compare" + END64)
	defer file.Close()
	defer writeFile.Close()
	var i = 0
	var hashed int64
	var firstLine string
	var nextLine string
	for reader.Scan() {
		if i%2 == 0 {
			firstLine = strings.TrimSpace(reader.Text())
			hashed = hashy64(firstLine)
		} else {
			nextLine = strings.TrimSpace(reader.Text())
			whereResults := whereHashPresent64(nextLine, len(firstLine), hashed, otherWriteFile, compareWriteFile)
			where := listToSpaceSeperatedString64(whereResults)
			_, err := writeFile.WriteString(nextLine + ", " + strconv.Itoa(len(firstLine)) + ", " + strconv.FormatInt(hashed, 10) + "\n")
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
	generateOutputForCharsToArbitraryNumbers64()
	generateOutputForHashy64()
	generateOutputForWhereHashPresent64()
}
