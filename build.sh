#!/usr/bin/env bash

mkdir -p bin/cpp

clang++ -std=c++17 -o bin/cpp/Square.o -c cpp/Square.cpp
clang++ -std=c++17 -o bin/cpp/Cube.o -c cpp/Cube.cpp
clang++ -std=c++17 -o bin/cpp/main.o -c cpp/main.cpp
clang++ -std=c++17 -o bin/ShapesCpp bin/cpp/main.o bin/cpp/Cube.o bin/cpp/Square.o
