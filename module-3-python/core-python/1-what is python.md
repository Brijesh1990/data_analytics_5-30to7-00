# what is python  ?

Python is a high-level, interpreted programming language known for its simple and readable syntax. 

It supports multiple programming paradigms including procedural, object-oriented, and functional programming. 

Python is widely used in web development, data analysis, artificial intelligence, scientific computing, and automation due to its extensive standard library and rich ecosystem of third-party packages.

## Key Features

- **Easy to Learn**: Clean syntax similar to natural English

- **Versatile**: Used across various domains and industries

- **Interpreted Language**: Code executes line by line without compilation

- **Dynamically Typed**: Variables don't require explicit type declaration

- **Large Community**: Extensive documentation and community support

- **Rich Libraries**: NumPy, Pandas, Django, Flask, and many more available through pip

## Common Use Cases

- Data analysis and visualization
- Web application development
- Machine learning and AI
- Scientific computing
- Automation and scripting
- Backend development


# how to install python 

 1. https://www.python.org/downloads/
 2. python --version


 # how to run python programme

   1. python via REPL (read | evaluate | print | loop)
      
      **via REPL***
      ```
      >>> a=10
      >>> b=20
      >>> c=a+b
      >>> print(c)
      30
      >>>


      >>> a=input('enter a name :')
      enter a name :brijesh
      >>> print('your name is :',a)
      your name is : brijesh
      >>>
      

      >>> age=18
      >>> if age>=18:
      ...     print('eliegible')
      ... else:
      ...     print('not eligle')
      ...
      ...
      eliegible
      
      >>> def name():
      ...     print("My name brijesh")
      ... name()
      ...
      My name brijesh
      >>>


      My name brijesh
      >>> for i in range(1,5):
      ...     print(i)
      ...
      1
      2
      3
      4
      >>>
      ```
   
   2. python via script

      **examples of script method**

      **examples.py**
      ```
      name="i am Het kumar"
      print(name) 
      ```` 


  3. run using jupyter  

     1. download and install jupyter via pip
     2. open terminal and write 

        ```
         jupyter notebook 
        ```

     3. write a programme in jupyter 

       ```
        a=int(input("Enter a Numbers :"))
        b=int(input("Enter b Numbers :"))
        c=a+b
        print("additions of numbers is :",c)

       ````   


# what is operator in python ?

  **operator in python**     

  An operator performed some action 
  An operator compared values 
  An assigned values and check true and false 

## types of operator 

1. airthematic operator   
   examples : +, -, *, /, %

2. assingment operator   
   examples : =, ==, !=

3. comparision operator   
   examples : ===, > , >= , < , <=

4. airthematic operator   
   examples : +, -, *, /, %      

5. betwise  operator   
   examples : >>, << , +=, -=,  *=, /=, %=, XNOR , XOR 

6. logical operator 
   examples : and , or, not

7. increment/decrement operator 

   examples : ++ , --

8. string concatenate operator 

   examples : "" + ""


# what is variables in python ?

  1. A variables is just like container where we stored information about data 
  2. variables will be changed the values dynamically 
  3. variables is stored information about data 

    **examples of variable**

    **rules to defined variables in python**

    1. simple defined with variables 
       a=10
       b=20
       c="brijesh"

    2. don't take the name start with keyword 

       if=10
       def=20
       in=20
       Note: can not take a variables name with reserved keyword 

      **examles**

      ```
      str1="Brijesh kumar";
      str2="krish kumar";
      # print(str1 + "\n" + str2)
      print(str1 + " " + str2)
      
      ```

## all keyword list 

  **keyword**

  ```
   import keyword
   print(keyword.kwlist)

  ```

  ```
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```

## what is data type of variables 