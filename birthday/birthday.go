package main

import "fmt"

func min(one, two int) int {
	if one < two {
		return one
	}
	return two
}

func _bridgeHelper(graph [][]int, node int, time *int, visited *[]bool, parent, low, disc *[]int) bool {
	(*visited)[node] = true
	(*disc)[node] = *time
	(*low)[node] = *time
	*time += 1

	for _, connectedNode := range graph[node] {
		if !(*visited)[connectedNode] {
			(*parent)[connectedNode] = node
			_bridgeHelper(graph, connectedNode, time, visited, parent, low, disc)
			(*low)[node] = min((*low)[node], (*low)[connectedNode])

			if (*low)[connectedNode] > (*disc)[node] {
				return true
			}
		} else if connectedNode != (*parent)[node] {
			(*low)[node] = min((*low)[node], (*disc)[connectedNode])
		}
	}

	return false
}

func graphHasABridge(graph [][]int, numNodes int) bool {
	time := 0
	parent := make([]int, numNodes)
	disc := make([]int, numNodes)
	low := make([]int, numNodes)
	visited := make([]bool, numNodes)
	for i := range parent {
		parent[i] = -1
		disc[i] = numNodes + 1
		low[i] = numNodes + 1
		visited[i] = false
	}

	for i := 0; i < numNodes; i++ {
		if !visited[i] {
			if _bridgeHelper(graph, i, &time, &visited, &parent, &low, &disc) {
				return true
			}
		}
	}
	return false
}

func analyzeGraph(numNodes, numEdges int) string {
	graph := make([][]int, numNodes)
	var from = -1
	var to = -1
	for i := 0; i < numEdges; i++ {
		_, err := fmt.Scanln(&from, &to)
		if err != nil {
			fmt.Println("Error occurred:", err)
			return "err"
		}
		graph[from] = append(graph[from], to)
		graph[to] = append(graph[to], from)

	}
	for _, connections := range graph {
		if len(connections) < 2 {
			return "yes"
		}
	}
	if graphHasABridge(graph, numNodes) {
		return "yes"
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
