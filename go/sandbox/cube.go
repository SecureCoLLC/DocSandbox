package sandbox

// @class Cube
// This is Cube, it operates on int32 and can compute areas
type Cube struct {
	// Internal width value
	width int32

	// Internal height value
	height int32

	// Internal depth value
	depth int32
}

// Constructor which creates a cube by taking three values in
// @param width The width value
// @param height The height value
// @param depth The depth value
func NewCube(width int32, height int32, depth int32) *Cube {
	return &Cube{
		width:  width,
		height: height,
		depth:  depth,
	}
}

// Width returns the width value
func (cb *Cube) Width() int32 {
	return cb.width
}

// Height returns the height value
func (cb *Cube) Height() int32 {
	return cb.height
}

// Depth returns the height value
func (cb *Cube) Depth() int32 {
	return cb.depth
}

// Area calculates and returns the area (width x height)
func (cb *Cube) Area() int64 {
	return int64(cb.width) * int64(cb.height) * int64(cb.depth)
}
