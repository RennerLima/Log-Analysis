#Log Analysis

This an udacity FSND project present at Udacity`s Full Stack Developer Nanodegree Program.

## Project Overview

In this project, students are asked to create a reporting tool that prints out reports based on the data in the database. This database contain over a thousand rows and students need to fetch results using a single query to answer the questions.

### Questions

* What are the most popular three articles of all time?
* Who are the most popular authors from all time?
* On which days did more than 1% of requests lead to errors?

## Instructions

* To run this code you need to have installed both <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a>

* Also, it`s necessary to download this <a href="https://drive.google.com/file/d/1chRgPv6H9cnxK0espfc23WSr8MXoT9MA/view?usp=sharing">Database</a> to run this code.

* Unzip the database file inside your vagrant directory.

* When everything is installed, from your terminal, go to the vagrant directory, run the command 'vagrant up'. This command will download and install a Linux operating System in your machine.

* When the installation finish, run command 'vagrant ssh' to log into the virtual machine.

* Go to the /vagrant directory and load the database with this code:
```sh
psql -d news -f newsdata.sql
```

* Finaly, run the scrpit to see the results.
```sh
python Project.py
```