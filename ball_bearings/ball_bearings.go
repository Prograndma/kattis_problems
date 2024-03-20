package main

import (
	"fmt"
	"math"
)

// This function is a decent enough first attempt, but it won't work. It's thinking of the balls and spaces as if
// they're on a straight line. This is not the case, the balls and spaces take up angles in a circle. My next function
// will account for that.
//func _findMaximumBallsAssumeFlatCircumference(innerDiameter, ballDiameter, minDist float32) int {
//	var workingCircumference = math.Pi * (innerDiameter - ballDiameter)
//	return int(workingCircumference / (ballDiameter + minDist))
//}

// this function doesn't do it either, because it assumes that the diameter of the bearing and the space also lie on a
// circle, which they don't. The start of the left edge of a ball and the start of the right edge of a ball to the first
// balls left are points that lie on a circle. We need to use the rule of cosines to find the angle of a triangle
// using those two points and the center of a circle.
//func findMaximumBallsAssumeDiameterIsOnCircumference(innerDiameter, ballDiameter, minDist float64) int {
//	var arcLength = ballDiameter + minDist
//	var radius = (innerDiameter - ballDiameter) / 2
//	var angle = arcLength / radius
//	return int((2 * math.Pi) / angle)
//}

func findMaximumBalls(innerDiameter, ballDiameter, minDist float64) int {
	var b = (innerDiameter - ballDiameter) / 2
	var c = minDist + ballDiameter

	// Here you can't use the hypotenuse formula, since it isn't a right angle triangle, and you don't know the angle
	// between b and c, so you can't use a^2 = b^2 + c^2 - 2bc cos(a). Luckily, it's the same value as b.
	var a = b
	var numerator = math.Pow(a, 2) + math.Pow(b, 2) - math.Pow(c, 2)
	var denominator = 2 * a * b
	var angle = math.Acos(numerator / denominator)

	return int((2 * math.Pi) / angle)
}

func main() {
	var count int
	_, err := fmt.Scanf("%d\n", &count)
	if err != nil {
		fmt.Println(err)
	}
	for i := 0; i < count; i++ {
		var innerDiameter, ballDiameter, minDist float64
		_, err := fmt.Scanf("%f %f %f\n", &innerDiameter, &ballDiameter, &minDist)
		if err != nil {
			fmt.Println("Error reading input:", err)
			return
		}
		maxBalls := findMaximumBalls(innerDiameter, ballDiameter, minDist)
		fmt.Println(maxBalls)
	}

}
