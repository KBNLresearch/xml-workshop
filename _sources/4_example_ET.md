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

# 4. Practical session: Working with ElementTree

In this lesson, we are going to explore how we can use the package ElementTree to extract content from XML files. 
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

## Import ElementTree and import the xml file

ElementTree is part of the standard Python library and therefore does not need to be installed.

Before we can use the package, we have to let Python know we want to use it. We do this by importing the package.
Type the following in a code cell:

```{code-cell}
import xml.etree.ElementTree as ET
```
Now we can use the package to extract data from the XML. 

## Examine the structure of the file

Now we want to open the XML file from which we want to extract information. 
Add a new code cell and type:

```{code-cell}
tree = ET.parse('data/example.xml')
root = tree.getroot()
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
print(ET.tostring(root, encoding='utf8').decode('utf8'))
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

First, type the following code in your Jupyter Notebook to get the title from every book:

```{code-cell}
:tags: [hide-output]

for book in root.findall('book'):
    title = book.find('title').text
    print(title)
```

We shall explain what every line of the code does.

First, we iterate through the complete XML file and search for every element with the tag name 'book'. 

```
for book in root.findall('book'):
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

```{admonition} Solution
:class: tip, dropdown
	
	for book in root.findall('book'):
		description = book.find('description').text
		print(description)
	
```

This leads to the following output: 

```{code-cell}
:tags: [hide-output]

for book in root.findall('book'):
    description = book.find('description').text
    print(description)
```

We can use one *for loop* to extract both the book title *and* description from the XML file. 
Combining multiple items is preferable because it saves unnecessary lines of codes and merges the part of the code which does the same thing.
This makes the code more readable and maintainable. 

Combining the two codes above leads to the following code:

```{code-cell}
:tags: [hide-output]

for book in root.findall('book'):
	title = book.find('title').text
	description = book.find('description').text
	print(title, description)

```

## Extract name and surname of the author
You can use the same method as described above to extract all the names and surnames from the authors from the example XML. 
However, if we look at the structure of the XML file, there is a difference between the placement of the elements 'title' and 'description', and the elements 'name' and 'surname' in the XML structure. 

```
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

for book in root.findall('book'):
    for author in book.findall('author'):
        name = author.find('name').text
        print(name) 
```

```{admonition} Exercise
:class: attention
The above code extracts only the name of an author. Alter the code, so that it extracts both the name and the surname. 
```

````{admonition} Solution
:class: tip, dropdown
```
for book in root.findall('book'):
	for author in book.findall('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```
````

```{code-cell}
:tags: [remove-input, hide-output]
for book in root.findall('book'):
	for author in book.findall('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```

The second approach is to 'escape' the element hiearchy and directly select all subelements, on all levels beneath the current element.
This is usefull if you have an XML with a lot of children, and you want only specific content which you want to extract apart from their parents. 
To escape  the hierarchy, you type './/' before the name of the element you want to extract, as shown in the following code:

```{code-cell}
:tags: [hide-output]

for book in root.findall('.//author'):
    name = book.find('name').text
    surname = book.find('surname').text
    print(name, surname)  
```

## Extract the book identifier

As you can see in the XML, each book has its own ***identifier***. As books can have the same name, and authors can have written multiple books, it 
is good practise to always use the identifier to point to a specific item. 

In the previous exercises, we extracted the content that was presented between the tags of an element.
For example:


```
<title>XML Developers Guide</title>
```

In this example, you see that the title 'XML Developer's guide' is stored between the tags <title> and </title>. We extracted this content by adding '.text'. 

```{admonition} Exercise
:class: attention
Look at this example of the 'book' element with its identifier. What is the difference between the place of the content of the identifier and the
place of the content of the title?
	```
		<book id="bk101">
		</book>
	```
```

```{admonition} Solution
:class: tip, dropdown
The content of the identifier is stored in an *attribute* of the 'book' element, with the name 'id'. 
	
```

To extract content from attributes, we need to use the 'get' method. 
We still use the *for loop* to iterate through all the books, but instead of extracting the content of certain elements, we now extract the content of the attribute. 

```{code-cell}
:tags: [hide-output]

for book in root.findall('book'):
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
``` Pyhton
for book in root.findall('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.findall('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```	
````

This leads to the following output:
```{code-cell} Python
:tags: [remove-input, hide-output]
for book in root.findall('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.findall('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```	

As you can see, it displays all information we wanted, but the output is quite unreadable. For example, it is not clear which part of the content belongs
to the title, and which to the description. 

To make the output more readable, we can put text before our output variables. In Python, this can be done like this:
```
print(f"This is the string we type and {this_is_the_variable}")
```

So in our example, we could for example add the following:

```{code-cell}
:tags: ["hide-output"]

for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    print(f"Identifier= {identifier} title= {title} description= {description} name= {name} {surname}")
```

As you can see, we can now detect the various parts that we extracted. However, it is still not easy to read.
To resolve this, we can add linebreaks between each variable and between the different books. We add a line break by adding '\n' after each variable, 
leading to the following code:

```{code-cell}
:tags: ["hide-output"]

for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    print(f"Identifier= {identifier }\n title= {title}\n description= {description} \n name= {name} {surname}\n")
```

Well, that output looks way better, doesn't it?

## Store the information in a .csv or .txt file.
In a lot of cases, you not only want the extracted content in your Jupyter Notebook, but you also want to store them 
for future use. 
We will show you how to store the output in two different ways:
- as one file with the information of all books in .csv format (which, for example, can be opened in Excel)
- as one textfile per book. 

### Store in one file
The easiest way to store and save Python output in one file is through storing it in a dataframe from the Python package 'Pandas' and then saving this frame. 
You can add data directly from the *for loops* we created above in a pandas dataframe, but we prefer the method in which you first create a list and then transform this list in the output, as Pandas DataFrame execution can become fairly slow with large amounts of data. 

To create a list, we first have to declare an empty list. This is done with the following syntax:
```
booklist = []
```

Now, we alter our *for loop* a bit. Instead of printing the output to the screen, as we did above, we store our output in a list. 
We can use the following code:
```{code-cell}
:tags: ["hide-output"]

booklist = []

for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    booklist.append([identifier, title, description, name+" "+surname])
```

```{code-cell}
:tags: ["remove-input", "hide-output"]

booklist = []

for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    booklist.append([identifier, title, description, name+" "+surname])

booklist
```

This leads to a list, called 'booklist', in which for every book all information is stored. 

We can then easily transform this list to a pandas DataFrame. 
To do so, we need to import pandas first with the code
```
import pandas as pd
```

Then we type:
``` 
books = pd.DataFrame(booklist, columns=["identifier", "title", "description", "name"])
```

This code works as follows. You declare the variable 'books', which will be used to store all the information. 
Then you let Python know that you want to create a DataFrame. The content of this dataframe is the list 'booklist', which we just created. 
We then tell Python how we want to name the columns (they should be in the same order as the order of the variables in the list). 

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

First, you have to declare a textfile in Python and give it a name. Then, you open the file and write content to it. After this, you close the file. 
You can try this with the following code:

```
with open("test.txt", "w") as f:
    f.write("This is just a test file")
```

```{note}
By default, Python stores the text file in the same folder as where you run your Jupyter Notebook. You can alter this by adding a path to your textfile, for example:
``` with open('C:/Users/Documents/test.txt', 'w') as f ```
Please remember to use a backward slash ('/') between the folders
```

With a few alterations, we can use this code to save our book information to a seperate file per book. 
First, we give the text file the name of the book identifier. we can do that by adding the variable into the name of the file like this:
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
for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    with open(f"{identfier}.txt", "w") as f:
		f.write(name + " " + surname + "\n" + title + "\n" + description)
```

## Filter information

You can also search for specific elements in your XML. For example, just the title information from the book 'bk109'. To do so, you can start with the same *for loop* as we created in this lesson. However, before you print the output, you first check if you have the element you want (in this case: book 109). This can be done with an 'if' statement and it looks like this:

```{code-cell}
for book in root.findall('book'):
    if book.attrib['id']=="bk109":
        title = book.find('title').text
        print(title)
```

You can also search the content from XML elements, searching the content for a match. For example, if we want to print all titles that contain the word 'XML', 
we can use the following code:

```{code-cell}
for book in root.findall('book'):
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

```{admonition} Solution
:class: tip, dropdown
	for book in root.findall('book'):
		description = book.find('description').text
		if "England" in description:
			print(book.find('description').text)
```	

```{code-cell}
:tags: ["remove-input","hide-output"]

for book in root.findall('book'):
	description = book.find('description').text
	if "England" in description:
		print(description)
```


### Namespaces  

As we mentioned in lesson *2* during our introduction to XML, some XML files contain namespaces. 

When working with ElementTree, it is important to know if an XML file has namespaces, as it can cause
malfunctioning of your code if they are not properly declared. 

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
tree = ET.parse('data/namespaces.xml')
root_ns = tree.getroot()
```

Then, we create a *for loop* that iterates through the file and returns the values of all 'name' elements. 

```{code-cell} Python
for student in root_ns.findall('name'):
    print(student.text)
```

Although we know there is a student with the name 'Jeff Smith', Python returns nothing. 

So, what is going on? Why is there not any output? 
This is because there are namespaces defined in the XML file. 

```{admonition} Exercise
:class: attention
Open the XML file in your Notebook and look at the namespace declaration. 
```

````{admonition} Solution
:class: tip, dropdown
```
print(ET.tostring(root_ns, encoding='utf8').decode('utf8'))
```
````	

```{code-cell}
:tags: ["remove-input","hide-output"]
tree = ET.parse('data/namespaces.xml')
root_ns = tree.getroot()

print(ET.tostring(root_ns, encoding='utf8').decode('utf8'))
```


The package elementTree needs namespace declaration to handle namespaces correctly. 

This can be done in two ways:

1. Type the namespace before the element name between curly brackets: {http//www.imaginarypythoncourses.com/student}name

```{code-cell} Python
for student in root_ns.findall('{http//www.imaginarypythoncourses.com/student}name'):
    print(student.text)
```

2. Declare the namespace in elementTree. You therefore create a Python dictionary with the namespace abbreviation and the identifier *without* the curly brackets. 

```{important}
When you want to declare namespaces in Python, you can not blindly use the namespaces as you see them in your XML file when
it is opened in another programma. 

For example, when we open our file in the browser, we see the namespace '<p:student xmlns:p="http//www.imaginarypythoncourses.com/student">'.
However, if we look in or Python file, we see that the prefix of the namespace is changed, and the namespace is now
'<ns0:student xmlns:ns0="http//www.imaginarypythoncourses.com/student">'. 
```

```{code-cell} Python
ns = {"ns0": "http//www.imaginarypythoncourses.com/student"}
```

Now you can use the abbreviation of the namespace in your code:
```{code-cell} Python
ns = {"ns0": "http//www.imaginarypythoncourses.com/student"}

for student in root_ns.findall('ns0:name', ns):
    print(student.text)
```

```{note}
If you declare the namespace in Python with a dictionary, do not forget to put the dictionary name 
after your element name in the *.findall* or other functions where you need a namespace. 
Without this, Python does not recognize the namespace as such. 
```

```{important}
When there are *attributes* with a namespace, you can only use the first option as the namespace declaration does not work with attributes!
```

We now have a good basis of ElementTree, but we wish to show you another package, Beautiful Soup,
before moving on to introducing real-life examples of XML files used in Digital Humanities research.
The introduction to working with Beautiful Soup can be found in the following lesson. 