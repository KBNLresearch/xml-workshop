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

# 10. Practical session: TEI and Beautiful Soup

In this section we will use Beautiful Soup to extract data from a book in the TEI format.
For this lesson, we assume that you have followed the practical lesson 5. When needed, refer back to previous lessons.
As you may have noticed, there is no lesson for extracting information from the TEI format using ElementTree. 
ElementTree has sometimes trouble parsing files (in this case due to '&nbsp' in the content). This can be fixed with a work around, however this work around need
to be adjusted when there is a new version of ElementTree. We therefore chose to only use Beautiful Soup, as this works without problems. 

We will follow these steps:

- Load the TEI file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
- Extract the complete content of the book from the TEI file <span style="color:#ef6079">(*basic*)</span>;
- Extract the content divided into chapters <span style="color:#ef6079">(*basic*)</span>;
- Extract the separate poems <span style="color:#ef6079">(*moderate*)</span>.
- Extract the poems per chapter <span sftyle="color:#ef6079">(*moderate*)</span>.

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook.

## Load the TEI file and examine the structure

We first need to prepare the Notebook by importing the package we need and loading the XML file into the enviroment. 
If you have not already installed Beautiful Soup, do this first with:

```
!pip install beautifulsoup4
```

```{admonition} Exercise
:class: attention
Import the Beautiful Soup package and load the XML file into your Notebook.
You can look back to lesson 5 if you need a reminder on how to do this. 
The XML file is named ‘TEI.xml’ and can be [downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data).
```

````{admonition} Solution
:class: tip, dropdown
```Python
from bs4 import BeautifulSoup    

with open("data/TEI.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
```
````

In order to extract the required information from the file, we have to examine the structure.

```{admonition} Exercise
:class: attention
Print the file in your Notebook or look at the file in your browser, either way you prefer.
```

```{code-cell}
:tags: [remove-input, hide-output]
from bs4 import BeautifulSoup    
with open("data/TEI.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
print(root)
```

The TEI XML contains a lot of information that is not part of the textual content of the book.
This information describes for example the layout and the type of the text.
It also contains elements in which the plain text is stored. 
We start by searching for this element, and the check whether the content is stored as the value of tags or as the value 
of an attribute.

```{admonition} Exercise
:class: attention
Look at the XML structure, in which element is the content stored? Is it stored as value of the tags or as the value of an attribute? 
Does it have any parents we have to consider while extracting the content?
```

```{admonition} Solution
:class: tip, dropdown
The content is stored in various elements, such as *title*, *head*, *l*, and *p*.
The content is stored as a value of the tags.
```

```{note}
When working with TEI format it is very important to check the lay-out and which elements are present. 
This can vary a lot between files.

Because of this variation, it is wise to **always** check which elements you need to ensure you extract the correct data. 
TEI files of the same kind, for example all about one poet, usually are similar. However, double-checking this can save a lot of work (and frustration) later on.
```

Remember namespaces? Before we start to extract the data we are interested in we need to stop 
for a moment and examine the file to see if we need to take namespaces into account.

```{admonition} Exercise
:class: attention
Are there any namespaces in the file that we have to take into account? 
If there are, how can we declare these?
```

````{admonition} Solution
:class: tip, dropdown
The XML file does not contain any namespaces. 
````

## Extract the complete content of the book from the TEI file

There are a lot of elements containing the data. 
One option is to print the whole XML. This way no content will be missed and all possible text is extracted. 

```{admonition} Exercise
Print the complete content of the book. 
```

````{admonition} Solution
:class: tip, dropdown
```
root.text
```
````

```{code-cell}
:tags: [remove-input, hide-output]
root.text
```
A disadvantage of this option is that a lot of metadata is printed as well, for example the text:

"Dit bestand biedt, behoudens een aantal hierna te noemen ingrepen, een diplomatische weergave van 
De dichtwerken van Bilderdijk. Deel 1</hi> van Willem Bilderdijk in de eerste druk uit 1856."

This sentence gives information about this edition of the book and its alterations. 
Usually you would not want to have the metadata within the content. Filtering this out afterwards is very work-intensive.

## Extract the content divided into chapters

```{admonition} Exercise
:class: attention
Can you think of a way to structure the text in a more logical manner? 
```
```{admonition} Solution
:class: tip, dropdown
One option would be to print it out per chapter.
```

In lesson 5 we learned that is is possible to acces the elements with a for loop, like:
```
for book in root.find_all('book'):
```

However, there are various 'div' elements and we only want the one that contain a chapter. 

```{admonition} Exercise
:class: attention
How do we know which div is a chapter?
```
```{admonition} Solution
:class: tip, dropdown
The type of the div is stored in the attribute 'type'. 
```

We can iterate through all divs and only proceed with the divs that have 'chapter' as type.
This can be done with an *if* statement. 

This leads to the following code:

```{code-cell}Python
:tags: [hide-output] 
## the for loop iterates through every div 
for div in root.find_all('div'):
	## all actions within the loop are performed div by div.
	## here we select only divs with type chapter
    if div.get('type') == 'chapter':
		## and we print the div
        print(div.text)
```

The code still prints out everything as a single piece of text without anything to distinguish the different chapters. 
Adding a chapter header is an easy way to be able to seperate the different chapters. 
This can be done by making a counter and print the text 'chapter [counter]' before every chapter. After every *div* that the code iterates through the counter is raised by one, so every chapter gets a distinguishing number.

This can be achieved with the following code:

```Python
## initialise the counter at 1
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print("chapter " + str(counter))
        print(div.text)
		## add 1 to the counter every iteration of the loop
        counter += 1
```

Try the code above to see how the output now contains increasing chapter count

```{code-cell}
:tags: [remove-input,hide-output]

from bs4 import BeautifulSoup    

with open("data/TEI.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')

counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print("chapter " + str(counter))
        print(div.text)
		## add 1 to the counter every iteration of the loop
        counter += 1
```

Great! we now have all the chapters in order, and numbered. However, this is not the most readable output.

Printing to the output is great for prototyping, but to make sure the extracted data can be used for further analysis and to keep the workspace a bit uncluttered it is best to save the extracted content to file. 
This can be done chapter for chapter or by creating one larger file containting a chapter per row.

```{admonition} Exercise
:class: attention
Expand the code so it saves the extracted chapters as seperate text files, using the chapter name and number as file name.
Hint: do you remember f strings?
```

````{admonition} Solution
:class: tip, dropdown
```Python
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        chapter = "chapter_" + str(counter)
        with open(f"{chapter}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(div.text)
            counter += 1
```
Remember that this saves the files in the root folder of your Jupyter installation. If you want it saved in a specific location you need to specify the path before the filename followed by a '/; .
````

Now we have a lot of text files. Each one containing one chapter of the book . For some uses this may be preferable, but for other a single, ordered file may be preferred. 
In the next exercises we will write code that will store the chapters in an ordered format in a single file.

```{admonition} Exercise
:class: attention
If you recall, it is also possible to save the data as .csv.  
What are the easiest steps to do this?
```

```{admonition} Solution
:class: tip, dropdown
1. Saving the content in a list
2. Transforming into a Pandas Dataframe
3. Save the DataFrame to .csv
```

Having refreshed our memory we will now put it into practice. 

```{admonition} Exercise
:class: attention
Change the code to store the chapter and content in a list. Note that this will create one long list with all the extracted content.
```

````{admonition} Solution
:class: tip, dropdown
```Python
chapter_list = []
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        chapter = "chapter_" + str(counter)
        content = div.text
        chapter_list.append([chapter, content])
        counter += 1
```
````

With the first step done the list can now be transformed into a Dataframe. Don't forget to think about the order of the list content and the Dataframe columns.

```{admonition} Exercise
:class: attention
Transform the list into a Dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```Python
import pandas as pd
book = pd.DataFrame(chapter_list , columns = ['chapter', 'content'])
```
````

```{admonition} Exercise
:class: attention
It is good practice to check what you transformed, so print out the dataframe.
```

```{admonition} Solution
:class: tip, dropdown
	book
```

If the Dataframe is in order we can save the Datframe directly to file.
 
```{admonition} Exercise
:class: attention
Save the Dataframe to csv.
```

````{admonition} Solution
:class: tip, dropdown
```Python
book.to_csv('book_with_chapters.csv')
```
Remember that this saves the csv in the root folder of your Jupyter installation. If you want it saved in a specific location you need to specify the path before the filename followed by a '/; .
````

## Extract the separate poems

For some uses only a specific piece of an XML is needed. Extracting everything and then either removing or ignoring part of the extracted content is a lot of work that can be omitted by specifically extracting what is needed.
The example TEI file contains a book that consists of both poems and pieces of prose. Both of these are specified somewhere in the XML. 
Over the coming exercises we will extract only the poems. To do this we need to know which elements contain the poems.

```{admonition} Exercise
:class: attention
Check the file to see which elements are needed to extract the poems from the file.
```

```{admonition} Solution
:class: tip, dropdown
To extract the poems the element **lg** with type **poems** is needed. 
```

Having found the elements with the poems, we will now need to extract them from the XML.

```{admonition} Exercise
:class: attention
Write a piece of code that extracts and prints all the poems from the file. You can look at the previous exercises for hints.
```

````{admonition} Solution
:class: tip, dropdown
```Python
for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        print(div.text)
```
````

```{code-cell}Python
:tags: [remove-input,hide-output]
for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        print(div.text)
```

As we did in the previous exercises where we extracted the whole chapters, we will save the extracted poems as seperate, and numbered, files. 

```{admonition} Exercise
:class: attention
Expand the code of the previous exercise to include a counter for numbering the poems, and saving the poems one by one. As with the previous exercises use 'poem + counter' or something similar as a filename. 
```

````{admonition} Solution
:class: tip, dropdown
```
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        with open(f"{poem}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(div.text)
            counter += 1
```
````

Again, we now have many seperate files. But we will also want to create a single file containing the poems in a structured manner.


```{admonition} Exercise
:class: attention
Adapt the code above to save the extracted poems to a single csv. If you feel lost, just go back a few exercises and look at what we did there. Remember, first list, then dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```Python
poem_list = []
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        content = div.text
        poem_list.append([poem, content])
        counter += 1

import pandas as pd
poems = pd.DataFrame(poem_list , columns = ['poem', 'content'])

poems.to_csv('poems.csv')
```
````

## Extract the poems per chapter

We now have extracted the separate chapters, or the separate poems. It can also be interesting to extract the separate chapters with their corresponding poems. 

```{admonition} Exercise
:class: attention
Create a Dataframe containing all the (numbered) chapters and poems:
- The chapters must be numbered consecutively
- The poems must be numbered consecutively per chapter

This means that you will need to extract chapter information from the XML, in addition to the poem information. Also, something to number the chapters is needed.
```

````{admonition} Solution
:class: tip, dropdown
You code should look similar to the code below. 
```
import pandas as pd
chapter_list = []
c_counter = 1
p_counter = 1 

for div in root.find_all('div'):
	if div.get('type') == 'chapter':
		chapter = "chapter_" + str(c_counter)
		content = div.text
		for poems in div.find_all('lg'):
			if poems.get('type') == 'poem':
				poem = "poem_" + str(p_counter)
				p_content = poems.text
				chapter_list.append([chapter, poem, p_content])
				p_counter += 1
		c_counter += 1
		p_counter = 1

poems  = pd.DataFrame(chapter_list, columns = ['chapter', 'poem', 'content'])
```
````

```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
chapter_list = []
c_counter = 1
p_counter = 1 

for div in root.find_all('div'):
	if div.get('type') == 'chapter':
		chapter = "chapter_" + str(c_counter)
		content = div.text
		for poems in div.find_all('lg'):
			if poems.get('type') == 'poem':
				poem = "poem_" + str(p_counter)
				p_content = poems.text
				chapter_list.append([chapter, poem, p_content])
				p_counter += 1
		c_counter += 1
		p_counter = 1

poems  = pd.DataFrame(chapter_list, columns = ['chapter', 'poem', 'content'])
poems
```

As you can see we now have the poems numbered per chapter, and each chapters nicely numbered as well. This datafame will make a nice and ordered dataset for further analysis or presentation.

Having extracted different types of content and saving them to text and csv, we could, for example, use these for further analyses. Remember that saving files without specifying a pathname saves them to the root folder of Jupyter. This folder might clutter up quickly and it is wise to clean it up regularly or keep it clean by specifying a pathname to a specific folder.






