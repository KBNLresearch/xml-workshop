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

# 11. Practical session: Page and Beautiful Soup

In this section we will use Beautiful Soup to extract data from a newspaper in the Page xml format.
For this lesson, we assume that you have followed the practical lesson 5. When needed, refer back to previous lessons.

We will follow these steps:

- Load the Page file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
- Extract the complete content of a newspaper page from the Page file <span style="color:#ef6079">(*basic*)</span>;
- Extract the text region with the corresponding content <span style="color:#ef6079">(*moderate*)</span>;
- Extract the reading order and use this to automatically sort the page <span style="color:#ef6079">(*advanced*)</span>.

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook.

## Load the Page file and examine the structure

We first need to prepare the Notebook  by importing the package we need and loading the XML file into the enviroment.
If you have not already installed Beautiful Soup, do this first with:

```
!pip install beautifulsoup4
```

```{admonition} Exercise
:class: attention
Import the Beautiful Soup package and load the XML file into your Notebook.  
You can look back to lesson 5 if you need a reminder on how to do this. 
The XML file is named 'page.xml' and can be [downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data).
```

````{admonition} Solution
:class: tip, dropdown
```
from bs4 import BeautifulSoup    
with open("data/page.xml", encoding='utf8') as f:
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
with open("data/page.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
print(root)
```

The page XML contains a lot of information that is not part of the textual content of the newspaper. 
This information describes the layout of the page. It also contains elements in which the plain
text is stored. We start by searching for this element, and the check whether the content is
stored as the value of tags or as the value of an attribute.  

```{admonition} Exercise
:class: attention
Look at the XML structure, in which element is the content stored?
Is it stored as value of the tags or as the value of an attribute?
Does it have any parents we have to consider while extracting the content?
```
```{admonition} Solution
:class: tip, dropdown
The content is stored in an element called 'Unicode', it is stored as a value of the tags.  
The elements has multiple parents, however, with Beautiful Soup you can call any item directly without worrying about their parents.
```

All Page XML files from the KB contain a reading order. This reading order guides the user through the file and indicates what the right order of all text elements is. 
To determine the correct reading order, we need three types of information. 

```{admonition} Exercise
:class: attention
Look carefully at the XML. What information do we need to correctly display the reading order?
```
````{admonition} Solution
:class: tip, dropdown
* The id attribute of each TextRegion element
* The OrderedGroup id for each TextRegion element
* The index of each region

With this information, you can determine the correct reading order, which is declared in 
the ReadingOrder element, e.g.:
 ```
<ReadingOrder>
	<UnorderedGroup id="ro357564684568544579089">
		<OrderedGroup id="r38">
			<RegionRefIndexed regionRef="r8" index="0"/>
			<RegionRefIndexed regionRef="r12" index="1"/>
			<RegionRefIndexed regionRef="r16" index="2"/>
			<RegionRefIndexed regionRef="r20" index="3"/>
			<RegionRefIndexed regionRef="r24" index="4"/>
			<RegionRefIndexed regionRef="r28" index="5"/>
			<RegionRefIndexed regionRef="r32" index="6"/>
			<RegionRefIndexed regionRef="r36" index="7"/>
			<RegionRefIndexed regionRef="r40" index="8"/>
			<RegionRefIndexed regionRef="r44" index="9"/>
			<RegionRefIndexed regionRef="r46" index="10"/>
			<RegionRefIndexed regionRef="r48" index="11"/>
			<RegionRefIndexed regionRef="r52" index="12"/>
			<RegionRefIndexed regionRef="r56" index="13"/>
			<RegionRefIndexed regionRef="r60" index="14"/>
			<RegionRefIndexed regionRef="r64" index="15"/>
			<RegionRefIndexed regionRef="r68" index="16"/>
			<RegionRefIndexed regionRef="r72" index="17"/>
			<RegionRefIndexed regionRef="r74" index="18"/>
		</OrderedGroup>
 ```
````

Remember namespaces? Before we start to extract the data we are interested in we need to stop 
for a moment and examine the file to see if we need to take namespaces into account.

```{admonition} Exercise
:class: attention
Are there any namespaces in the file that we have to take into account? 
If there are, how can we declare these?
```

````{admonition} Solution
:class: tip, dropdown
The XML file does contain namespace, however, since we are working with BeautifulSoup we don't have to do antyhing special to deal with them. 
````

Now that we know how the file is structured, and where the content we need is stored, we can start extracting the output

## Extract the complete content of a newspaper page from the Page file

Our first step is to just extract the complete content of the page, without worrying about the 
reading order. 

```{admonition} Exercise
The text content that we wish to extract is stored in the Unicode element. 
Use Python and Beautiful Soup to extract this content.
```

````{admonition} Solution
:class: tip, dropdown
```
## loop through all the Unicode elements and print the text data from each element
for newspaper in root.find_all('Unicode'): ## we don't have to escape the parents and their is no need to declare the namespace. 
    print(newspaper.text)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
for newspaper in root.find_all('Unicode'):
    print(newspaper.text)
```

## Extract the text region with the corresponding content

Now we have all the text content, but it is not in the right order. We need some more
information for that. 

```{admonition} Exercise
What information do we need for every text content to determine the right reading order?
Is this information stored as value of the tags or as a value of an attribute?
```

```{admonition} Solution
:class: tip, dropdown
We need the information stored in the id of TextRegion. 
The TextRegion id is an *attribute*.
```
Knowing this we will need to use the .get() method to find the TextRegion ids. 

```{admonition} Exercise
Alter the code to also extract the TextRegion id and print it out along with the content per newspaper. 

Hint: in the previous code we used the element 'Unicode' to extract the content. We must now
use an element that contains both the Unicode element and the TextRegion id. 
```

````{admonition} Solution
:class: tip, dropdown
The following code should print out all the content.
```
for newspaper in root.find_all('TextRegion'):
    regionid = newspaper.get('id')
    for content in newspaper.find_all('Unicode'):
        print(regionid)
        print(content.text)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
for newspaper in root.find_all('TextRegion'):
    regionid = newspaper.get('id')
    for content in newspaper.find_all('Unicode'):
        print(regionid)
        print(content.text)
```


Now we have all the data with its corresponding TextRegion id, however it is not very readable. Also, getting the correct reading other from this printout is not the easiest task.
To make our life a bit easier we will put the data into a Pandas Dataframe. 
As seen before in lesson 4, we will first put the whole set into a list.

```{admonition} Exercise
Instead of printing the TextRegion id and content, change the code so that it puts this 
information into a list. 
```

````{admonition} Solution
:class: tip, dropdown
```
## Create an empty list
content_list = []

for newspaper in root.find_all('TextRegion'):
    regionid = newspaper.get('id')
    for content in newspaper.find_all('Unicode'):
        content = content.text
    ## append the regionid and content to the list
    content_list.append([regionid, content])
```
````


Let us just peek at the list to see if everything went as expected.
````{admonition} Exercise
Print out the list that was made in the previous exercise to see if it was created correctly.
````

````{admonition} Solution
:class: tip, dropdown
```
print(content_list)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
content_list = []

for newspaper in root.find_all('TextRegion'):
    regionid = newspaper.get('id')
    for content in newspaper.find_all('Unicode'):
        content = content.text
    ## append the regionid and content to the list
    content_list.append([regionid, content])
	  
print(content_list)
```

Now that we have a list containing both the TextRegion id and the textual content, we can transform this into a Dataframe. 

```{admonition} Exercise
Create dataframe with the columns 'Region' and 'Content' from the list we have just created.
```

````{admonition} Solution
:class: tip, dropdown
```
import pandas as pd
newspaper = pd.DataFrame(content_list, columns = ["Region", "Content"])
```	
````

```{note}
Pay close attention to the order of the input list and column names! The first item added to the list should also have its name first in the columns parameter.
```

As before, check the result to make sure everything went as expected.
```{admonition} Exercise
Check if the Dataframe is made correctly. 
Remember to not use the print method, as without 'print' the formatting will be more readable for Dataframes.
```

````{admonition} Solution
:class: tip, dropdown
```
newspaper
``` 
````

```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
newspaper = pd.DataFrame(content_list, columns = ["Region", "Content"])
newspaper
```

Finally we can now save the dataframe to csv, after which it can be used for further research or manipulation. 

```
newspaper.to_csv('newspaper_content.csv')
```


## Extract the reading order and use this to automatically sort the page

By using the XML file  and the information about the reading order in the csv file, it is possible to order the file in the correct reading order manually. 
However this is a lot of work and when there are multiple, or very large files, this is not the best use of our time. 
Luckily Python offers us ways to automate this.

Because the information about the reading order and indexes are stored in a different location 
than the content itself, we will go through three steps: 

* From the element 'ReadingOrder', we will extract the information about the OrdererGroup id, the regionRef and the index and store them in a Python dictionary;
* We retrieve the textregion and corresponding content (see the code above);
* We combine the textregion information with the regionRef from the dictionary to combine everything.
* We store the information in a Dataframe and sort it based on the ReadingOrder. 

As you can see, we are going to create a Python dictionary. Dictionaries are an easy way to store
and query information. But more about dictionaries later, let's first see if we can retreive all desired values. 

```{admonition} Exercise
Write a code that prints out the id of every ordered group, with per id:
* The corresponding RegionRefs;
* The corresponding indexes;
```

````{admonition} Solution
:class: tip, dropdown
```
for order in root.find_all('ReadingOrder'):
	for group in root.find_all('OrderedGroup'):
		groupnr = group.get('id')
		print(groupnr)
		for suborder in group.find_all('RegionRefIndexed'):  
			region = suborder.get('regionRef')
			index = suborder.get('index')
			print(region, index)
```	
````
```{code-cell}
:tags: [remove-input, hide-output]
for order in root.find_all('ReadingOrder'):
	for group in root.find_all('OrderedGroup'):
		groupnr = group.get('id')
		print(groupnr)
		for suborder in group.find_all('RegionRefIndexed'):  
			region = suborder.get('regionRef')
			index = suborder.get('index')
			print(region, index)
```

Printing this information gives us a chance to check if our code is behaving the way we expect. 
However, we wish to further automate the process and store it into a Python dictionary.

A dictionary is structured as follows: key = value. 
In our case, the 'key' is the regionref, and the values for every key are the ordered group id and the index.

We shall demonstrate this using a small piece of our XML file:

```
<ReadingOrder>
	<OrderedGroup id="r38">
		<RegionRefIndexed regionRef="r8" index="0"/>
		<RegionRefIndexed regionRef="r12" index="1"/>
	</OrderedGroup>
</ReadingOrder>
```

This can be stored in a Python dictionary like this:
```{code-cell}
dict = {'r8': [['r38', '0']],
		'r12': [['r38', '1']]}
```

With this dict, we can ask Python specific information about every textregion.
For example: to which group does r8 belong?

```{code-cell}
group = dict['r8'][0][0] ## [0] for the first entry, [0] for the first element
print(group)
```

And what is the index of r12?
```{code-cell}
group = dict['r12'][0][1] ## [1] for the first entry, [0] for the second element
print(group)
```

The following code gives an example of how you can store the required information in a dictionary.

```{code-cell}
## First initialize an empty dictionary
dict_order = {}

for order in root.find_all('ReadingOrder'):
	for group in root.find_all('OrderedGroup'):
		groupnr = group.get('id')
		for suborder in group.find_all('RegionRefIndexed'):  
			region = suborder.get('regionRef')
			index = suborder.get('index')
			## the dictionary is filled with the three attributes
			## it sets region as the key and as value the groupnr and index as a list 
			dict_order.setdefault(region,[]).append([groupnr, index])
```

Let's print the dictionary to make certain it works.

```{code-cell}
:tags: [hide-output]
print(dict_order)
```

We have previously made the code to obtain the content and the region from the XML file. Now we will combine this by comparing the values from the dictionary with the value of the TextRegion id.
As not all content is in an ordered group, we also have to include an 'escape' mechanism. For now, we will store all content that does not belong in an OrderedGroup into group 0 with index 0. 

```{code-cell}
:tags: [hide-output]
for newspaper in root.find_all('TextRegion'):
	## here we extract from the dictionary the group and index value for the dictionary item that matches the region extracted with the orignal code.
	## if the content does not belong to an ordered group, we store them in group 0 with index 0
	region = newspaper.get('id')
	if region in dict_order:
		groupvalues = dict_order[region]
		group = groupvalues[0][0]
		index = groupvalues[0][1]
	else:
		group = 0
		index = 0
	for content in newspaper.find_all('Unicode'):
		content = content.text
	## then we can add them to the print statement
	print(group, region, index, content)
```

With this code we merge the reading order values that we stored in the dictionary with the content that we extract with the origial code. However, we still print the result instead of storing it in something more useful.

```{admonition} Exercise
Adapt the code above to store all relevant information in a list.

Don't forget to declare an empty list first.
```

````{admonition} Solution
:class: tip, dropdown
```
content_list = []

for newspaper in root.find_all('TextRegion'):
	region = newspaper.get('id')
	if region in dict_order:
		groupvalues = dict_order[region]
		group = groupvalues[0][0]
		index = groupvalues[0][1]
	else:
		group = 0
		index = 0
	for content in newspaper.find_all('Unicode'):
		content = content.text
	content_list.append([group, index, region, content])
```	
````

Now we have stored the merged information into a list, we can transform the list into a Pandas Dataframe. 


```{admonition} Exercise
Transform the list into a Dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```
import pandas as pd
newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
```	
````

We then check the result again.
```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
content_list = []

for newspaper in root.find_all('TextRegion'):
	region = newspaper.get('id')
	if region in dict_order:
		groupvalues = dict_order[region]
		group = groupvalues[0][0]
		index = groupvalues[0][1]
	else:
		group = 0
		index = 0
	for content in newspaper.find_all('Unicode'):
		content = content.text
	content_list.append([group, index, region, content])
newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
newspaper_with_order
```

Now that we have our data in a Dataframe, we have some easy options for manipulating the data. One of these is ordering, or sorting, the Dataframe. 
A Dataframe can be sorted by any of its columns, or even multiple columns. The original shape and content is maintained, but the order of the rows is changed to whatever is specified.
The syntax for sorting a Dateframe is:

```
Dataframe.sort_values([column(s) to sort by], [sorting order])
```
In the code below the Dataframe we just made is sorted by 'Group' and 'Index' in ascending order for both. 
Notice that the sorting columns are quoted. When adding more than one column a (comma separated) list must be passed. The sorting order default is 'ascending', for 'descending', the ascending attirbute is set to False.

```{code-cell}
newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'], ascending = [True, True])
```
With the reordered Dataframe in hand we can check if the sorting went as planned.


```{admonition} Exercise
Make sure you performed all of the above steps in your notebook and print out the ordered Dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```
newspaper_with_order
```	
````

```{code-cell}
:tags: [remove-input, hide-output]
newspaper_with_order
```
If everything worked as it was supposed to, the new dataframe should now be ordered by the Group and Index columns. Much easier to read, and better structured. Well done!

Of course, as before we could save this Dataframe to disk using .to_csv(), or pass it to other code for further analysis.
