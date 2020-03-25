package sandbox

import "fmt"

func assert(cond bool) {
	if !cond {
		panic("Assertion failed")
	}
}

func main() {
	sq := NewSquare(3, 2)
	cb := NewCube(5, 4, 3)

	fmt.Printf("SQ = %v\n", sq.Area())
	fmt.Printf("CB = %v\n", cb.Area())

	assert(sq.Area() == 6)
	assert(cb.Area() == 60)
}
