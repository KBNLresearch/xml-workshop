---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 5. Practical session: Working with Beautiful Soup


In this lesson, we are going to explore how we can use the package Beautiful Soup to extract content from XML files. 
We use the same example file that was used in lesson **2** ([download here](https://github.com/MirjamC/xml-workshop/tree/master/data).

This lesson is divided into the following steps:
- Load the XML file;
- Examine the structure of the XML file;
- Extract the booktitles and descriptions;
- Extract name and surname of the author;
- Extract the book identifier;
- Structure all information;
- Explore namespaces;
- Extra: Filter information

Open a new Jupyter Notebook and type all the code examples and code exercises in your Notebook. 

## Install Beautiful Soup

Beautifull Soup is not a standard Python package, so it needs to be installed first.
This can be done directly in the Jupyter Notebook using:

```
!pip install beautifulsoup4
```

or through the command line (see lesson *1*)

```
pip install beautifulsoup4
```

## Import Beautiful Soup and load the xml file

Before we can use the package, we have to let Python know we want to use it. We do this by importing the package.
Type the following in a code cell:

```{code-cell}
from bs4 import BeautifulSoup  
```

Now we can use the package to extract data from the XML. 

## Examine the structure of the file


Now we want to open the XML file from which we want to extract information. 
Add a new code cell and type:

```{code-cell}
with open("data/example.xml") as f:
    root = BeautifulSoup(f, 'xml')
```
```{note}
In the code above, alter the 'data/example' with the path to the folder and the filename of where you stored the file. 
```

When you want to extract information from an XML file, it is important that you are familiar with the structure of the file. 
There are two ways to do this. 

1. You can open the file in a program like Notepad++ or open it in your browser
2. You can show the file in your Jupyter Notebook with the following code:

```{code-cell} ipython3
:tags: [hide-output]

print(root)
```

## Extract the book titles and descriptions

```{admonition} Exercise
:class: attention
Look at the XML structure. Which elements do we need to extract the title and the description?
```


```{admonition} Solution
:class: tip, dropdown
We need the element 'book', and its children 'title' and 'description'. 
```

First, type the following code in your Jupyter Notebook to get the *title* from every book:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    title = book.find('title').text
    print(title)
```

````{note}
Although the basic *for loop* for ElementTree en Beautiful Soup look identical, please note that
there is a small difference: ElementTree uses 'findall' and Beautiful Soup 'find_all' (with an underscore).
````
We shall explain what every line of the code does.

First, we iterate through the complete XML file and search for every element with the tag name 'book'. 

```
for book in root.find_all('book'):
```

Then, for every book element that exist, we create a temporarly new variable with the name 'title'. 
As value for this variable, we use the content of the tag 'title' (which is a direct child of the element 'book'). 
we add '.text'. to let Python know that we are interested in the value between the tags. 
Without the '.text' addition, Python would simply present us the tag in its location, like '<Element 'title' at 0x000001995B4718B0>'

```
title = book.find('title').text
```

Then, we print the output of the title
```
print(title)
```

After this, the loop proceeds to the following book elements, extraxts the title and print the title etc. 

We can get the description of each book in the same way.

```{admonition} Exercise
:class: attention
Alter the code above to retreive all the *descriptions* and print out the descriptions. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	description = book.find('description').text
	print(description)
```	
````
This leads to the following output:
```{code-cell}
:tags: [remove-input, hide-output]
for book in root.find_all('book'):
	description = book.find('description').text
	print(description)
```

We can use one *for loop* to extract both the book title *and* the description from the XML file. 
Combining multiple items is preferable because it saves unnecessary lines of codes and merges the part of the code which does the same thing.
This makes the code more readable and better maintainable. 

Combining the two codes above leads to the following code:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
	title = book.find('title').text
	description = book.find('description').text
	print(title, description)

```


## Extract name and surname of the author
You can use the same method as described above to extract all the names and surnames from the authors from the example XML. 
However, if we look at the structure of the XML file, there is a difference between the placement of the elements 'title' and 'description', and the 
elements 'name' and 'surname' in the XML structure. 

```XML
<catalog>
	<book id="bk101">
		<author>
			<name>Matthew</name>
			<surname>Gambardella</surname>
		</author>
		<title>XML Developer's Guide</title>
		<genre>Computer</genre>
		<price>44.95</price>
		<publish_date>2000-10-01</publish_date>
		<description>An in-depth look at creating applications with XML.</description>
   </book>
```


```{admonition} Exercise
:class: attention
Look at the XML snippet above. What is the difference between the element 'title' and the element 'name'?
```

```{admonition} Solution
:class: tip, dropdown
	
The element 'title' is a child of the element 'book'. 
The element 'name' however, is a child of the element 'author' and a *sub*child of the element 'book'. 
	
```

Because of the difference in the place between elements, we need to alter our code a bit. 
We can use two approaches:
* Add another *for loop* inside or first loop;
* 'escape' the element hierarchie. 

For the first approach, instead of a single *for loop* that iterates through all the 'book' elements, 
we also need a second *for loop* that runs through the 'author' element of 'book'. We can do this with the following code:


```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    for author in book.find_all('author'):
        name = author.find('name').text
        print(name) 
```

```{admonition} Exercise
:class: attention
The above code extracts only the name of an author. Alter the code, so that it extracts both the name and the surname. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```
````

```{code-cell}
:tags: [remove-input, hide-output]
for book in root.find_all('book'):
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```
The second approach is to ‘escape’ the element hiearchy and directly select all subelements, 
on all levels beneath the current element. This is usefull if you have an XML with a lot of 
As explained in lesson *3*, you can just insert the name of the subchild, as shown in the following code:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('author'):
    name = book.find('name').text
    surname = book.find('surname').text
    print(name, surname)  
```

## Extract the book identifier

As you can see in the XML, each book has its own ***identifier***. 
As books can have the same name, and authors can have written multiple books, it is good practise to always use the identifier to point to a specific item. 

In the previous exercises, we extracted the content that was presented between the tags of an element.
For example:


```XML
<title>XML Developers Guide</title>
```

In this example, you see that the title 'XML Developer's guide' is stored between the tags **title** and **/title**. We extracted this content by adding '.text'. 

````{admonition} Exercise
:class: attention
Look at this example of the 'book' element with its identifier. 
What is the difference between the place of the content of the identifier and the place of the content of the title?

```XML
	<book id="bk101">
	</book>
```
````

```{admonition} Solution
:class: tip, dropdown
The content of the identifier is stored in an *attribute* of the 'book' element, with the name 'id'. 
	
```

To extract content from attributes, we need to use the '.get' method. 
We still use the *for loop* to iterate through all the books, but instead of the content of certain elements, we now extract the content of the attribute. 

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    identifier = book.get('id')
    print(identifier)

```

## Structure all information

We can combine the different codes we have used above into one cell. 
To do this we can use the following scheme:

```
Iterate through all books	
	Get content from id attribute
	Get title content	
	Get description content	
	Iterate through all authors
		Get name
		Get surname
	Print id, title, description, name and surname
```

```{admonition} Exercise
:class: attention
Create the code that extracts all information we have used so far, from every book. And print this information (see scheme above). 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```
````

This leads to the following output:
```{code-cell} 
:tags: [remove-input,hide-output]
for book in root.find_all('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```

As you can see, it displays all information we wanted, but the output is quite unreadable. 
For example, it is not clear which part of the content belongs to the title, and which to the description. 

To make the output more readable, we can put text before our output variables. 
In Python, this can be done like this:
```Python
print(f"This is the string we type and {this_is_the_variable}")
```

So in our example, we could add the following:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
	## add text to identify the extracted parts
    print(f"Identifier= {identifier} title= {title} description= {description} name= {name} {surname}")
```

As you can see, we can now detect the various parts that we extracted. 
However, it is still not easy to read.
To resolve this, we can add linebreaks between each variable and between the different books. W
e add a line break by adding '\n' after each variable, 
leading to the following code:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
	## add linebreaks
    print(f"Identifier= {identifier }\n title= {title}\n description= {description} \n name= {name} {surname}\n")

```

Well, that output looks way better, does it not? 

## Store the information in a .csv or .txt file.
In a lot of cases, you not only want the extracted content in your Jupyter Notebook, but you also want to store them 
for future use. 
We will show you how to store the output in two different ways:
- as one file with the information of all books in .csv format (which, for example, can be opened in Excel)
- as one textfile per book. 

### Store in one file
The easiest way to store and save Python output in one file is through storing it in a Dataframe from the Python package 'Pandas' and then saving this Dataframe. 
You can add data directly from the *for loops* we created above in a Pandas Dataframe, but we prefer the method in which you first create a list and then transform this list in the output, as Pandas Dataframe execution can become fairly slow with large amounts of data. 

To create a list, we first have to declare an empty list. This is done with the following syntax:
```
booklist = []
```

Now, we alter our *for loop* a bit. Instead of printing the output to the screen, as we did above, we store our output in a list. 
We can use the following code:
```{code-cell}
:tags: [hide-output]

booklist = []

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    booklist.append([identifier, title, description, name+" "+surname])
```
This leads to a list, called 'booklist', in which for every book all extracted information is stored. 
We can then easily transform this list to a pandas DataFrame. 
To do so, we need to import pandas first with the code
```
import pandas as pd
```

Then we type:
``` 
books = pd.DataFrame(booklist, columns=["identifier", "title", "description", "name"])
```


This code works as follows. You declare the variable 'books', which will be used to store all 
the information. Then you let Python know that you want to create a Dataframe. 
The content of this Dataframe is the list 'booklist', which we just created. 
We then tell Python how we want to name the columns (this should be in the same order as the order of the variables in the list). 

You can show the dataframe you just created by typing:
``` 
books
```

This results in the following output:
```{code-cell}
:tags: [remove-input, hide-output]


import pandas as pd
books = pd.DataFrame(booklist, columns=["identifier","title", "description", "name"])
books
```

Now we can save this dataframe into a csv file by typing:
```
books.to_csv('book.csv')
``` 

```{note}
This saves the csv in the root folder of your jupyter installation. 
If you want it saved in a specific location you need to specify the path before the filename followed by a '/,
for example ```books.to_csv('C:/Users/Documents/book.csv')```
Please remember to use a backward slash ('/') between the folders
```


### Create a textfile per book

If you want to create a textfile for every book, you can add the code directly in your *for loop*. 

First, you have to declare a textfile in Python and give it a name. Then, you open the file and write content to it. After this, you close the file. Closing the file is important, else the loop will keep adding data to the file.
You can try this with the following code:

```
with open("test.txt", "w") as f:
    f.write("This is just a test file")
```

````{note}
By default, Python stores the text file in the same folder as where you run your Jupyter Notebook. You can alter this by adding a path to your textfile, for example:
```
 myfile = open('C:/Users/Documents/test.txt', 'w') 
```
Please remember to use a backward slash (/) between the folders
````

With a few alterations, we can use this code to save our book information to a seperate file per book. 
First, we give the text file the name of the book identifier. We can do that by adding the variable into the name of the file like this:
```
with open(f"{identfier}.txt", "w") as f:
```

Then, we create the content of the file based on the content we extracted from the book. 
```
f.write(name + " " + surname + "\n" + title + "\n" + description)
```

If we put these lines into our *for loop*, Python will save every book with its own name and information. 
The code looks like this:
```
for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    with open(f"{identfier}.txt", "w") as f:
		f.write(name + " " + surname + "\n" + title + "\n" + description)
```

## Filter information

You can also search for specific elements in your XML. 
For example, just the title information from the book 'bk109'. 
To do so, you can start with the same *for loop* as we created in this lesson. 
However, before you print the output, you first check if you have the element you want (in this case: book 109). This can be done with an 'if' statement and it looks like this:

```{code-cell}
for book in root.find_all('book'):
    identifier = book.get('id')
    if identifier == "bk109":
        title = book.find('title').text
        print(title)
```

You can also search the content from XML elements, searching the content for a match. For example, if we want to print all titles that contain the word 'XML', 
we can use the following code:

```{code-cell}
for book in root.find_all('book'):
    title = book.find('title').text
    if "XML" in title:
        print(title)
```

```{note}
Strings in Python are capital senstive! This means that 'XML' is not equal to 'xml' or 'Xml' in Python. 
```


```{admonition} Exercise
:class: attention
Print out the title of all books that have England in their description. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	description = book.find('description').text
	if "England" in description:
		print(book.find('description').text)
```
````	

```{code-cell}
:tags: [remove-input, hide-output]
for book in root.find_all('book'):
	description = book.find('description').text
	if "England" in description:
		print(book.find('description').text)
```	
		
### Namespaces  

As we mentioned in lesson *2* during our introduction to XML, some XML files contain namespaces. 
In lesson *3*,we mentioned that Beautiful Soup omits these namespaces in elements, so you don't have to declare them. 

Let's look at the example with namespaces from lesson 2:

```XML
<p:student xmlns:p="http//www.imaginarypythoncourses.com/student">
  <p:id>3235329</p:id>
  <p:name>Jeff Smith</p:name>
  <p:language>Python</p:language>
  <p:rating>9.5</p:rating>
</p:student>
```

Imagine, we want to extract the name of the student from this XML file. 

First, we load the file into our Notebook (the file is called 'namespaces.xml' and can be [downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data)

```{code-cell} Python
with open("data/namespaces.xml") as f:
    root_ns = BeautifulSoup(f, 'xml')
```

Then, we create a *for loop* that iterates through the file and returns the values of all 'name' elements. 

```{code-cell} Python
for student in root_ns.find_all('name'):
    print(student.text)
```

As you can see, Beautiful Soup has no problem with printing the name of the student. 

However, in some XML documents, *attributes* can have a namespace. 
In such cases, you have to put the namespace identifier in your code. 

Let's imagine the XML looks as follows:

```XML
<p:student xmlns:p="http//www.imaginarypythoncourses.com/student">
  <p:name p:id='3235329'>Jeff Smith</p:name>
  <p:language>Python</p:language>
  <p:rating>9.5</p:rating>
</p:student>
```

Imagine we want to extract the attribute 'id'. We see that this attribute has a namespace, so we need to declare it in the code. 
This can only be done by putting the identifier into curly brackets before the attribute name. 

The code should looks as follows:
```
for student in root.find_all('name'):
    identifier = student.get('{http//www.imaginarypythoncourses.com/student}id')
```

We now have a good basis to try exploring some reallife examples of XML files used in Digital Humanities research. We will introduce some of these formats in the following section.


