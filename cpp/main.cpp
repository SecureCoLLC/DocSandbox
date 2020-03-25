#include "Cube.hpp"
#include "Square.hpp"

#include <iostream>

using namespace std;

using namespace sandbox;

int main()
{
    Square sq{3, 2};
    Cube cb{5, 4, 3};

    cout << "SQ = " << sq.area() << endl;
    cout << "CB = " << cb.area() << endl;

    return 0;
}