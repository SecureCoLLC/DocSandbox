#!/usr/bin/env bash

set -euo pipefail

mkdir -p bin/cpp
mkdir -p bin

echo "### Building ShapesCpp"
clang++ -std=c++17 -o bin/cpp/Square.o -c cpp/Square.cpp
clang++ -std=c++17 -o bin/cpp/Cube.o -c cpp/Cube.cpp
clang++ -std=c++17 -o bin/cpp/main.o -c cpp/main.cpp
clang++ -std=c++17 -o bin/ShapesCpp bin/cpp/main.o bin/cpp/Cube.o bin/cpp/Square.o

echo "### Running ShapesCpp"
bin/ShapesCpp

echo "### Building ShapesGo"
pushd go
go build -o ../bin/ShapesGo .
popd

echo "### Running ShapesGo"
./bin/ShapesGo

echo "### Generate C++ documentation"
./scripts/doxygen.sh

# echo "### Generate Go documentation"

git add docs
