# FurnitureWebSite
A presentation website written with the python web framework django &amp; java script  frontend React. The site will host products as well as the capability to make request for handmade furniture 



## How to...

1. Create a virtual enviorment to encapsulate all FurnitureWebSite dependencies in one virtual machine

   Install virtaulenv through pip package manager:

   `sudo pip install virtualenv`

   Create a virtaul enviroment special directory
 
   `mkdir virt_env`

   Generate the virtual enviorment...

   `virtualenv virt_env/FurnitureVirt --no-site-packages --verbose`
 

   Activate the enviroment...

   `source virt_env/FurnitureVirt/bin/activate`


   To deactivate it write..
 
   `deactivate`

2. Install the requierd dependencies

   First make sure the virtualenv is activated ( a FurnitureVirt tag name should appear in paranthesis a the start of shell command line in 
left corner)

   `pip install -r pipackage/requierments.txt`  

   Now you should have a fully functional enviroment with all the dependencies installed. 


## Regex shortcuts 
 
   `^`| Matches the expression to its right at the start of a string. It matches every such instance before each `\n` in the string
   `$`| Matches the expression to its left at the end of a string. It matches every such instance before each `\n` in the string
   `.`| Matches any character except line terminator like `\n`.
   `\`| Escapse special characters or denotes characters classes
   `A|B`| Matches expression `A` or `B`. If `A` is matched first, `B` is left untried.
   `+`| Greedily matches the expression to its left 1 or more times.
   `*`| Greedily matches the expression to its left 0 or more times.
   `?`| Greedilt matches the expression to its left 0 or 1 times. But if `?` is added to qualifiers (`+`, `*` and `?` itself) it will perform 
   matches in a non-greedy manner.

    
