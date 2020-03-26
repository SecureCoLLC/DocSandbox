package main

import (
	"fmt"

	"github.com/SecureCoLLC/DocSandbox/sandbox"
)

// assert is a method to confirm that a condition is true and panics otherwise
func assert(cond bool) {
	if !cond {
		panic("Assertion failed")
	}
}

// main is the entry point of go function
func main() {
	sq := sandbox.NewSquare(3, 2)
	cb := sandbox.NewCube(5, 4, 3)

	fmt.Printf("SQ = %v\n", sq.Area())
	fmt.Printf("CB = %v\n", cb.Area())

	assert(sq.Area() == 6)
	assert(cb.Area() == 60)
}
