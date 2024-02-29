package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strings"
)

var PRE = "string_matching\\goOutputFor"
var END = ".txt"
var TEST_FILE = "string_matching\\test_strings.txt"

func listToSpaceSeperatedString(toConvert []*big.Int) string {
	//return strings.Trim(strings.Replace(fmt.Sprint(a), " ", delim, -1), "[]")
	//return strings.Trim(fmt.Sprint(toConvert), "[]")
	return strings.Trim(fmt.Sprint(toConvert), "[]")
}

func generateOutputForCharsToArbitraryNumbers() {
	file, err := os.Open(TEST_FILE)
	if err != nil {
		fmt.Println("ERROR in opening", TEST_FILE)
		fmt.Println(err)
		return
	}
	name := PRE + "charsToArbitraryNumbers" + END
	writeFile, err := os.Create(name)
	if err != nil {
		fmt.Println("ERROR in opening", TEST_FILE)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	const maxCapacity int = 5000000 // your required line length
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	for scanner.Scan() {
		numbers := charsToArbitraryNumbers(scanner.Text())
		strResults := listToSpaceSeperatedString(numbers)
		_, err := writeFile.WriteString(strResults + "\n")
		if err != nil {
			fmt.Println(err)
			fmt.Println("Error writing to file")
		}
	}

	//if err := scanner.Err(); err != nil {
	//	fmt.Println(err)
	//	return
	//}
	fmt.Println("SUCCESS")

}

func main() {
	generateOutputForCharsToArbitraryNumbers()
}
