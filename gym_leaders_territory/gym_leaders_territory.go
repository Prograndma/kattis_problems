package main

import (
	"fmt"
)

func remove(s []int, i int) []int {
	var index = -1
	for j, thing := range s {
		if thing == i {
			index = j
			break
		}
	}

	s[index] = s[len(s)-1]
	return s[:len(s)-1]
}

func analyzeGraph(numNodes, numEdges, target int) string {
	graph := make([][]int, numNodes)
	var from = -1
	var to = -1
	for i := 0; i < numEdges; i++ {
		_, err := fmt.Scanln(&from, &to)
		if err != nil {
			fmt.Println("Error occurred:", err)
			return "err"
		}
		from--
		to--
		graph[from] = append(graph[from], to)
		graph[to] = append(graph[to], from)

	}
	madeDifference := true
	for madeDifference {
		if len(graph[target]) < 2 {
			return "yes"
		}
		madeDifference = false
		for i, connections := range graph {
			if len(connections) == 1 {
				graph[connections[0]] = remove(graph[connections[0]], i)
				graph[i] = []int{}
				madeDifference = true
			}
		}
	}
	return "no"
}

func main() {
	var numNodes = -1
	var numEdges = -1
	var target = -1
	_, err := fmt.Scanln(&numNodes, &target, &numEdges)
	if err != nil {
		fmt.Println("Error occurred:", err)
		return
	}

	result := analyzeGraph(numNodes, numEdges, target-1)
	fmt.Println(result)
}
