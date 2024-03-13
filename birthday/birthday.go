package main

import "fmt"

func analyzeGraph(numNodes, numEdges int) string {
	nodes := make([]int, numNodes)
	var from = -1
	var to = -1
	for i := 0; i < numEdges; i++ {
		_, err := fmt.Scanln(&from, &to)
		if err != nil {
			fmt.Println("Error occurred:", err)
			return "err"
		}
		nodes[from] += 1
		nodes[to] += 1

	}
	for _, num := range nodes {
		if num < 2 {
			return "yes"
		}
	}
	return "no"
}

func main() {
	var numNodes = -1
	var numEdges = -1
	_, err := fmt.Scanln(&numNodes, &numEdges)
	if err != nil {
		fmt.Println("Error occurred:", err)
		return
	}
	for numNodes != 0 && numEdges != 0 {
		result := analyzeGraph(numNodes, numEdges)
		fmt.Println(result)
		_, err := fmt.Scanln(&numNodes, &numEdges)
		if err != nil {
			fmt.Println("Error occurred:", err)
			return
		}

	}
}
