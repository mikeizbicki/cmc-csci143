#!/bin/sh
# line 1 above is called the "shbang" haSH !=bang
# /bin/sh is the DASH shell; when you're typing directly in the terminal that's the BASH
# DASH only supports POSIX commands
set -e # ignore this for now

# create a temporary directory for all work to happen in
temp_dir=$(mktemp -d)
cd "$temp_dir"
pwd


echo 'problem 1'
# echo outputs to 'stdout'; pronounced "standard out"; normally stdout=terminal
# > called output redirection ; changes stdout to a filename
# >> output redirection
# >> "appends", > erases the file, then writes
echo 'hello world' > README.md
echo "hello world" >> README.md
echo hello world > README.md
cat README.md | wc -l



echo 'problem 2'
# /dev/null is a special file that just "eats" the input and does nothing
# 2> redirects "stderr" to the specified file
git init > /dev/null 2> /dev/null
git add README.md
git commit -m 'first commit' > /dev/null 2> /dev/null
ls -a | wc -l



echo 'problem 3'
git checkout -b new_branch > /dev/null 2> /dev/null
echo test > README.md
git add README.md
touch example # this file is never "added" to git, so checkout doesn't delete it;  README.md was added, and so it will be reverted on checkout to master
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
