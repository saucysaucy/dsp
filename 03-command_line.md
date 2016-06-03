# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > For Files
    

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
ls = bare format
ls -a = all files and folders
ls -l = long format with UNIX file types
ls -lh = provides units for file/folder size
ls -lah = long format of all files/folders with size units
ls -t = bare format sorted by modification time
ls -Glp = Colors the all files that are directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -R = returns subdirectories
ls -1 = returns each file on a new line
ls -u = shows file access times
ls -m = separates each item as a CSV
ls -i = returns with inode of each file

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs receives a standard input and executes it as an echo command. 
One example of its use it to execute a command over files with a certain 
criteria like removing files that are smaller than 10 kilobytes:
"find . -size -10K | xargs rm"

 

