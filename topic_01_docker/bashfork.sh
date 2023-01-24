#!/bin/bash

echo hello world

# in bash; the & calls the fork syscall
./longrunning.py &
./longrunning.py &
./longrunning.py &
./longrunning.py &
