#!/bin/sh
set -e

# create a temporary directory for all work to happen in
temp_dir=$(mktemp -d)
cd "$temp_dir"
pwd


echo 'problem 1'
echo 'hello world' > README.md
echo "hello world" >> README.md
echo hello world > README.md
cat README.md | wc -l



echo 'problem 2'
git init > /dev/null 2> /dev/null
git add README.md
git commit -m 'first commit' > /dev/null 2> /dev/null
ls -a | wc -l



echo 'problem 3'
git checkout -b new_branch > /dev/null 2> /dev/null
echo test > README.md
git add README.md
touch example
git commit -m 'new_branch' > /dev/null 2> /dev/null
git checkout master > /dev/null 2> /dev/null
ls | wc -l



echo 'problem 4'
mkdir dir
for file in a b c d; do echo 'hello world' > dir/file; done
ls dir | wc -l



echo 'problem 5'
touch 'this is "an example" with spaces'
for file in "$(ls)"; do echo $file; done | wc -l



echo 'problem 6'
cd dir
touch "*"
rm *
ls | wc -l
