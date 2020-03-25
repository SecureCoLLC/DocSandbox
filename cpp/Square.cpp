#include <cstdint>
#include <iostream>

namespace sandbox
{

/// @class Square
/// This is Square, it operates on int32_t and can compute areas
class Square
{
public:
    /// Constructor which creates a square by taking two values in
    /// @param width The width value
    /// @param height The height value
    Square(int32_t width, int32_t height)
        : width_{width}
        , height_{height}
    {
    }

    /// Generic destructor
    ~Square()
    {
    }

    /// Returns the width value
    /// @returns width
    int32_t width()
    {
        return width_;
    }

    /// Returns the height value
    /// @returns height
    int32_t height()
    {
        return height_;
    }

    /// Returns the area (width x height)
    /// @returns Value of area
    int64_t area()
    {
        return int64_t(width_) * height_;
    }

private:
    /// Internal width value
    int32_t width_{0};

    /// Internal height value
    int32_t height_{0};
};

}
