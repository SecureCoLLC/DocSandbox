package sandbox

// @class Square
// This is Square, it operates on int32 and can compute areas
type Square struct {
	// Internal width value
	width int32

	// Internal height value
	height int32
}

// Constructor which creates a square by taking two values in
// @param width The width value
// @param height The height value
func NewSquare(width int32, height int32) *Square {
	return &Square{
		width:  width,
		height: height,
	}
}

// Width returns the width value
func (sq *Square) Width() int32 {
	return sq.width
}

// Height returns the height value
func (sq *Square) Height() int32 {
	return sq.height
}

// Area calculates and returns the area (width x height)
func (sq *Square) Area() int64 {
	return int64(sq.width) * int64(sq.height)
}
