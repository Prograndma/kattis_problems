package main

import (
	"fmt"
	"io"
	"math/big"
)

func where_hash_present(in_str string, hash_len int, search_hash big.Int) {
	// finish this later.
}

func main() {
	var isPattern bool
	for {
		var input string
		_, err := fmt.Scan(&input)
		if err != nil {
			if err == io.EOF {
				break
			}
			// Do nothing, not my problem you did something bad.
		}
		if isPattern {
			// Finish later.
		} else {
			// Finish later.
		}

	}
}
