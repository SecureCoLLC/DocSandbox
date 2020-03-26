#!/usr/bin/env bash

set -euo pipefail

mkdir -p bin/cpp
mkdir -p bin

echo "### Building ShapesCpp"
clang++ -std=c++17 -o bin/cpp/Square.o -c cpp/sandbox/Square.cpp
clang++ -std=c++17 -o bin/cpp/Cube.o -c cpp/sandbox/Cube.cpp
clang++ -std=c++17 -o bin/cpp/main.o -c cpp/sandbox/main.cpp
clang++ -std=c++17 -o bin/ShapesCpp bin/cpp/main.o bin/cpp/Cube.o bin/cpp/Square.o

echo "### Running ShapesCpp"
bin/ShapesCpp

echo "### Building ShapesGo"
pushd go
go build -o ../bin/ShapesGo .
popd

echo "### Running ShapesGo"
./bin/ShapesGo

echo "### Generate and open documentation"
#./scripts/doxygen.sh

pushd docs
rm -rf sandbox sandbox.rst build html
make html
open build/html/index.html
popd

# git add docs
