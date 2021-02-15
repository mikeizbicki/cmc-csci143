# pagila-hw

## Background

[Pagila](https://github.com/devrimgunduz/pagila) is a standard example database for postgresql.
The database implements a simple movie rental system like the company Blockbuster might have maintained (before Netflix killed them).
The following picture illustrates the database's structure:

<img src=dvd-rental-sample-database-diagram.png width=80% />

## Downloading

Notice that this repo uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
These are a tool that allow us to work with very complicated projects by including git repos within other git repos,
and here we use submodules to include the original pagila repo.

By default, cloning a git repo does not download the submodules,
as a complex repo can have many hundreds of gigabytes of submodules.
In order to clone the repo with the submodules,
you need to run the commands
```
$ git clone https://github.com/mikeizbicki/pagila-hw
$ cd pagila-hw
$ git submodule init
$ git submodule update
```
