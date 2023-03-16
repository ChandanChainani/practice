package main

import "fmt"

const (
	x = 7
	y
	z
)

func main() {
  fmt.Println(x, y, z)

	var x int
	arr := [3]int{3, 5, 2}
  // slice assignment to static array with fixed size is not possible
	// x, arr = arr[0], arr[1:]
	fmt.Println(x, arr)
}
