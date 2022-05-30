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

# 12. Practical lesson: Automatically extract information from a batch of files

In the previous lessons, we have seen how we can extract information from the Alto, Didl, Tei and Page XML files. 
In this lesson, we will show you how you can use the codes from the previous lessons and, with a little bit of alteration, use them to automatically extract content from batches of XML files and save them as either textfiles or csv files. 

We will provide the following examples:

- Extract complete page content with newspaper metadata from various Alto and corresponding Didle files <span style="color:#ef6079">(*basic*)</span>.
- Extract the poems from various Tei files and store them in seperate csv files per book <span style="color:#ef6079">(*moderate*)</span>.
- Extract the content, including reading order, from various Page files and store the content in csv files <span style="color:#ef6079">(*advanced*)</span>.

##  Extract complete page content with newspaper metadata from various Alto and corresponding Didle files.

In lesson 7, we used the following code to extract the content and page number from a newspaper Alto XML and the title and publication year from the corresponding Didle file. 

```{code-cell} Python
:tags: [hide-output]
import xml.etree.ElementTree as ET

tree_alto = ET.parse('data/alto_id1.xml')
root_alto = tree_alto.getroot()

tree_didl = ET.parse('data/didl_id1.xml')
root_didl = tree_didl.getroot()

ns_alto = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'} 

ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
          'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
          'ns4' : 'info:srw/schema/1/dc-v1.1' }

article_content = ""

for book in root_alto.findall('.//ns0:TextBlock', ns_alto):
    for article in book.findall('.//ns0:String', ns_alto):
        content = article.get('CONTENT')
        article_content = article_content + content
    article_content = article_content + "\n"

    
for book in root_alto.findall('.//ns0:Page', ns_alto):
    pagenr = book.get('ID')
    
item = root_didl.find('.//ns2:Resource', ns_didl)
    
for article in item.findall('.//ns4:dcx', ns_didl):
    title = article.find('.//dc:title', ns_didl).text
    date = article.find('.//dc:date', ns_didl).text

        
filename = f'{title}_{date}_{pagenr}.txt'

with open(filename, "w", encoding="utf-8") as f:
    f.write(article_content)
```

With few little alterations, we can use this code to automatically work with a batch of files. 

- We need a code that automatically search through folder in your computer;
- We need to add a piece of code that finds the corresponding Didle file for every alto file. 

For the following code, we assume you have a folder called 'alto', which contains the Alto XML files, and a folder
'didl' that contains the Didl files ([downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data)). Both alto and didle have a filename that starts with an identifier, followed by 
either _alto or _didl. Make sure that there are no other files in the folder.

We start with a little loop that runs through your alto folder an returns all the file names

```{code-cell} Python
import os
# assign directory
directory = 'data/alto/'
 
for filename in os.listdir(directory):
    print(filename)
```

Now we need a code to strip the identifier from the alto file, and create the filename for the Didl file. 
This can be done with string alterations in Python, as we also did in lesson 7 and 8. 

```{code-cell} Python
filename = 'ddd_010097934_alto.xml'
filename_didl = filename.split('_alto')[0] ## Split the string by the underscore and only keep the first part
filename_didl = filename + "_didl.xml"
print(filename_didl)
```

Now, we have a way to retreive all alto files and corresponding Didl files, so the only thing left is to put it in one big loop. 

```{code-cell} Python
import xml.etree.ElementTree as ET
import os

directory_alto = 'data/alto/'
directory_didl = 'data/didl/'
 
for filename in os.listdir(directory):

    tree_alto = ET.parse(directory_alto + filename)
    root_alto = tree_alto.getroot()
    
    filename_didl = filename.split('_alto')[0] ## Split the string by the underscore and only keep the first part
    filename_didl = filename_didl + "_didl.xml"

    tree_didl = ET.parse(directory_didl + filename_didl)
    root_didl = tree_didl.getroot()

    ns_alto = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'} 

    ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
              'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
              'ns4' : 'info:srw/schema/1/dc-v1.1' }

    article_content = ""

    for book in root_alto.findall('.//ns0:TextBlock', ns_alto):
        for article in book.findall('.//ns0:String', ns_alto):
            content = article.get('CONTENT')
            article_content = article_content + content
        article_content = article_content + "\n"


    for book in root_alto.findall('.//ns0:Page', ns_alto):
        pagenr = book.get('ID')

    item = root_didl.find('.//ns2:Resource', ns_didl)

    for article in item.findall('.//ns4:dcx', ns_didl):
        title = article.find('.//dc:title', ns_didl).text
        date = article.find('.//dc:date', ns_didl).text


    filename = f'{title}_{date}_{pagenr}.txt'

    with open(filename, "w", encoding="utf-8") as f:
        f.write(article_content)
```

## Extract the poems from various Tei files and store them in seperate csv files per book.

In lesson 10, we extracted poems from a Tei file and stored them in a csv file. The code for this looked like this:

```{code-cell} Python
from bs4 import BeautifulSoup
import pandas as pd

with open("data/tei.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')

poem_list = []
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        content = div.text
        poem_list.append([poem, content])
        counter += 1
        
poems = pd.DataFrame(poem_list , columns = (['poem', 'content']))

poems.to_csv('poems.csv')
```

Just as we did with the alto files in the previous section, we can do the same for the TEI files. 

For the following exercises, we assume you have a folder on your computer with the name 'tei', in which you stored the various tei files ([downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data)). 

```{admonition} Exercise
:class: attention
what steps do we need to take to be able to create a batch output?
```

````{admonition} Solution
:class: tip, dropdown
- create a loop that runs through the tei folder 
- create a file name for each file, based on the identifier
````

```{admonition} Exercise
:class: attention
Create a loop that runs through the files in your tei folder and print their names.
```

````{admonition} Solution
:class: tip, dropdown
```Python
import os
# assign directory
directory = 'data/tei/'
 
for filename in os.listdir(directory):
    print(filename)
```
````

```{admonition} Exercise
:class: attention
create the variable 'filename' with the value 'bild001dich01_01.xml'. Strip the filename from the suffix .xml 
and print the filename.    
```

````{admonition} Solution
:class: tip, dropdown
```Python
filename = 'bild001dich01_01.xml'
filename = filename.split('.')[0]
print(filename)
```
````

Now we have all ingredients to automatically extracts the poems from the batch of tei files, and save them as csv
with their identifier as name. 

```{admonition} Exercise
:class: attention
Write a code that loops through the tei files, extracts the poems and stores them as csv.     
```

````{admonition} Solution
:class: tip, dropdown
```Python
from bs4 import BeautifulSoup
import pandas as pd
import os

# assign directory
directory = 'data/tei/'
 
for filename in os.listdir(directory):
    with open(directory + filename, encoding='utf8') as f:
        root = BeautifulSoup(f, 'xml')

    identifier = filename.split('.')[0]
    
    poem_list = []
    counter = 1

    for div in root.find_all('lg'):
        if div.get('type') == 'poem':
            poem = "poem_" + str(counter)
            content = div.text
            poem_list.append([poem, content])
            counter += 1

    poems = pd.DataFrame(poem_list , columns = ['poem', 'content'])

    poems.to_csv(identifier + '.csv')
```
````

## Extract the content, including reading order, from various Page files and store the content in csv files

And off course, we can do the same for the page XML. Lets start by repeating the code we made to extract the content, including the region information, and save it to a csv file. 

```{code-cell} Python
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('data/page.xml')
root = tree.getroot()

ns = {'ns0': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19'}

dict_order = {}

for order in root.findall('.//ns0:ReadingOrder', ns):
    for group in root.findall('.//ns0:OrderedGroup', ns):
        groupnr = group.get('id')
        for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
            region = suborder.get('regionRef')
            index = suborder.get('index')
            dict_order.setdefault(region,[]).append([groupnr, index])
                
content_list = []

for newspaper in root.findall('.//ns0:TextRegion', ns):
    region = newspaper.get('id')
    if region in dict_order:
        groupvalues = dict_order[region]
        group = groupvalues[0][0]
        index = groupvalues[0][1]
    else:
        group = 0
        index = 0
    for content in newspaper.findall('.//ns0:Unicode', ns):
        content = content.text
    content_list.append([group, index, region, content])

newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"]) 
newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'], ascending = [True, True])

newspaper_with_order.to_csv('newspaper_with_order.csv')
```

For the following exercises, we assume you have a folder on your computer with the name 'page', in which you stored the various page files ([downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data)).

```{admonition} Exercise
:class: attention
Write a code that loops through the page files in your 'page' folder, extracts the content with region information, and
store them in a .csv file with as name the identifier of the page file.     
```

````{admonition} Solution
:class: tip, dropdown
```Python
import xml.etree.ElementTree as ET
import pandas as pd
import os

directory = 'data/page/'
 
for filename in os.listdir(directory):

    tree = ET.parse(directory + filename)
    root = tree.getroot()
    
    identifier = filename.split('.')[0]
    print(filename)

    ns = {'ns0': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19'}

    dict_order = {}

    for order in root.findall('.//ns0:ReadingOrder', ns):
        for group in root.findall('.//ns0:OrderedGroup', ns):
            groupnr = group.get('id')
            for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
                region = suborder.get('regionRef')
                index = suborder.get('index')
                dict_order.setdefault(region,[]).append([groupnr, index])
                
    content_list = []

    for newspaper in root.findall('.//ns0:TextRegion', ns):
        region = newspaper.get('id')
        if region in dict_order:
            groupvalues = dict_order[region]
            group = groupvalues[0][0]
            index = groupvalues[0][1]
        else:
            group = 0
            index = 0
        for content in newspaper.findall('.//ns0:Unicode', ns):
            content = content.text
        content_list.append([group, index, region, content])

    newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"]) 
    newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'], ascending = [True, True])


    newspaper_with_order.to_csv(identifier + '.csv')

```
````

And that's all! 
You have now seen multiple ways of automatically extracting content from batches of files which can save a lot of time and errors. 