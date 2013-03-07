cgaljs
======

This is a project to aid porting [CGAL](http://www.cgal.org/) code to Javascript using an amazing tool called [Emscripten](https://github.com/kripken/emscripten) 

Dependencies:

* Emscripten (and all its requirements including Python, Clang, Java, and NodeJS)
* Emscripten tools must be on the path
* Linux build tools
 
To get started:

* Clone the Git repo
* Run the build_all.py script
* You should find the generated libs in the libs dir, and includes for each dependency in the includes dir
* In examples there's a simple test script you can run to demontrate the output running in NodeJS

Issues:

* There is no way to tell Javascript how to round floating point ops, so currently non-simple CGAL kernals will likely produce assertion errors


NB Emscripten Git revision at time of writing:230c0e80dfcd44870bec3254c399db430f6e1d98
