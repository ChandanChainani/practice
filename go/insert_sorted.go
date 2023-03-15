package main

import (
  "fmt"
)

/*
inserts elt at the correct place in seq, to keep it in sorted order
:param seq: A sorted list
:param elt: An element comparable to the content of seq
Effect: mutates the param seq.
Does not return a result
*/
func insert_sorted(seq []int, elt int) []int {
    idx := 0
    if elt > seq[len(seq) - 1] {
        return append(seq, elt)
    }

    for elt > seq[idx] && idx < len(seq) {
        idx += 1
    }
    newSeq := append(seq[:idx+1], seq[idx:]...)
    newSeq[idx] = elt
    return newSeq
}

func main() {
  num_list := []int{5, 10, 15, 20}
  fmt.Println(num_list)
  num_list = insert_sorted(num_list, 21)
  fmt.Println(num_list)
  num_list = insert_sorted(num_list, 18)
  fmt.Println(num_list)
}
