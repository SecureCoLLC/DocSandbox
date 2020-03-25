#include <cstdint>
#include <iostream>

namespace sandbox
{

/// @class Cube
/// This is Cube, it operates on int32_t and can compute areas
class Cube
{
public:
    /// Constructor which creates a cube by taking three values in
    /// @param width The width value
    /// @param height The height value
    /// @param depth The depth value
    Cube(int32_t width, int32_t height, int32_t depth)
        : width_{width}
        , height_{height}
        , depth_{depth}
    {
    }

    /// Generic destructor
    ~Cube()
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

    int32_t depth()
    {
        return depth_;
    }

    /// Returns the area (width x height)
    /// @returns Value of area
    int64_t area()
    {
        return int64_t(width_) * height_ * depth_;
    }

private:
    /// Internal width value
    int32_t width_{0};

    /// Internal height value
    int32_t height_{0};

    /// Internal depth value
    int32_t depth_{0};
};

}
