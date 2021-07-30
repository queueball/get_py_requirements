# Overview

`get_py_requirements` is a simple script wrapper around pip that can help build a requirements.txt file without needing to actually install the dependencies in
a normal project folder. Mechanically, this does download all the dependencies into a temporary folder and then returns the text needed for a requirements.txt
file.

The usecase I have is that I want to build docker images, but not have any dependencies on the parent host that would not be used routinely.

# Notes

There is a dependency on `click`. Proper dependency management is forthcoming.
