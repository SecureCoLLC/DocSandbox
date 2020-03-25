package sandbox

/// @class Square
/// This is Square, it operates on int32 and can compute areas
type Square struct {
	/// Internal width value
	width int32

	/// Internal height value
	height int32
}

/// Constructor which creates a square by taking two values in
/// @param width The width value
/// @param height The height value
func NewSquare(width int32, height int32) *Square {
	return &Square{
		width:  width,
		height: height,
	}
}

/// Returns the width value
/// @returns width
func (sq *Square) Width() int32 {
	return sq.width
}

/// Returns the height value
/// @returns height
func (sq *Square) Height() int32 {
	return sq.height
}

/// Returns the area (width x height)
/// @returns Value of area
func (sq *Square) Area() int64 {
	return int64(sq.width) * int64(sq.height)
}
