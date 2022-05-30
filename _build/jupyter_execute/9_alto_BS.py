#!/usr/bin/env python
# coding: utf-8

# # 9. Practical session: Alto and Beautiful Soup
# 
# In this lesson we are going to work with the Alto and Didle format. As shown in lesson ***6***, the Alto and Didle are connected to each other. 
# The Alto stores the plain text and the Didl the metadata of the newspaper. For this lesson, we assume that you have followed the practical lesson 5. 
# 
# This lesson contains the following content:
# * Load the Alto file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
# * Extract the complete content of a newspaper page from the Alto file <span style="color:#ef6079">(*basic*)</span>;
# * Load the Didl file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
# * Extract newspaper metadata from the Didl file. <span style="color:#ef6079">(*basic*)</span>;
# * Extract all separate articles from the total newspaper from the Didl file <span style="color:#ef6079">(*moderate*)</span>;
# * Extract all separate articles from a specific newspaper from the Didl file <span style="color:#ef6079">(*advanced*)</span>.
# 
# Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook.
# 
# ## Load the Alto file and examine the structure
# 
# We first need to prepare the Notebook by importing the package we need and loading the XML file into the enviroment.
# 
# ```{admonition} Exercise
# :class: attention
# Import the ElemenTree package and load the XML file into your Notebook.
# You can look back to lesson 4 if you need a reminder on how to do this. 
# The XML file is named ‘alto.xml’ and can be [downloaded here](https://github.com/MirjamC/xml-workshop/tree/master/data).
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# from bs4 import BeautifulSoup    
# 
# with open("data/alto_id1.xml", encoding='utf8') as f:
#     root_alto = BeautifulSoup(f, 'xml')
# ```
# ````
# 
# In order to extract the required information from the file, we have to examine the structure.
# 
# ```{admonition} Exercise
# :class: attention
# Print the file in your Notebook or look at the file in your browser, either way you prefer.
# ```
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# print(root_alto)
# ```
# ````

# In[1]:


from bs4 import BeautifulSoup    

with open("data/alto_id1.xml", encoding='utf8') as f:
    root_alto = BeautifulSoup(f, 'xml')
print(root_alto)


# ```{note}
# We will work with two XML files in this lesson. Therefore, we will name the root of the XML files according to the type of the XML: 'root_alto' for the alto XML and 'root_didl' for the Didl XML. 
# ```
# 
# The alto XML contains a lot of information that is not part of the textual content of the newspaper.
# There is information about the layout (where the content is placed on the page), about word confidence etc. 
# It also contains elements in which the plain text is stored. 
# We start by searching for this element, and the check whether the content is stored as the value of tags or as the 
# value of an attribute.
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML structure, in which element is the content stored? 
# *Hint: one of the news articles mentiones the
# word 'spoorwegmaatschappij'.* 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content of the news paper articles is stored in the element 'ns0:String', for example:
# 
# 	<String ID="P1_ST00323" HPOS="244" VPOS="2387" WIDTH="318" HEIGHT="35" CONTENT="spoorwegmaatschappij" WC="0.99" CC="88668080809486709965"/>
# 
# It is stored as an attribute of the element. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# If we compare the element 'String' to our example XML, we see that there is a difference in how the content is stored. 
# What is the difference? 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content of the elements of the example XML were stored als values from the elements. 
# The content of the String element is stored in an attribute called 'CONTENT'. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# There are a lot of nested element in this XML file.
# Do we have to bother about these parents while extracting content from the file?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# With Beautiful Soup you can call any item directly without worrying about their parents. 
# ```
# 
# Remember namespaces? Before we start to extract the data we are interested in we need to stop for a moment and examine the file to 
# see if we need to take namespaces into account.
# 
# ```{admonition} Exercise
# :class: attention
# Are there any namespaces in the file that we have to take into account? If there are, how can we declare these?
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# The XML file does contain namespace, however, since we are working with BeautifulSoup we don’t have to do antyhing special to deal with them.
# ````
# 
# Now we know some important information about this Alto file, so let's see if we can extract the content. 
# 
# ## Extract the complete content of a newspaper page from the Alto file
# 
# We will start by extracting all the text, without worrying about the division between the articles. 
# 
# ```{admonition} Exercise
# :class: attention
# As you have seen, the plain text of the news paper is stored in the 'CONTENT' attribute of the 'String' element. 
# How can you extract the values from attributes?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# This can be done with the .get method, for example: book.get('id'). 
# ```
# 
# In lesson 5 we learned that is is possible to acces the elements with a for loop, like:
# ```Python
# for book in root.find_all('book'):
# ```
# 
# ````{admonition} Exercise
# :class: attention
# The text content that we wish to extract is stored in the Unicode element. 
# Use Python and ElementTree to extract this content.
# ````
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# for page in root_alto.find_all('String'):
#     content = page.get('CONTENT')
#     print(content)	
# ```
# ```` 
# 
# This leads to the following output:

# In[2]:


from bs4 import BeautifulSoup    

with open("data/alto_id1.xml", encoding='utf8') as f:
    root_alto = BeautifulSoup(f, 'xml')

for page in root_alto.find_all('String'):
    content = page.get('CONTENT')
    print(content)	


# As you can see, the text is printed in separate words, that all appear in one long list. 
# So, this is quit unreadable. 
# We can store the text in a *string* variable in which we concatenate all words.

# In[3]:


all_content = ""

for page in root_alto.find_all('String'):
	content = page.get('CONTENT')
	all_content = all_content + " " + content
	
print(all_content)


# The content is now more readable, however, it is still one long blob of the complete text of the newspaper.
# As you can see in the XML file, the content is divided into sections. 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML file. There are different elements that divide the text. Which element would likely be used to separate articles from each other?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The element 'TextBlock'
# ```
# 
# Now that we know how we can divide the various sections, let's put this into code.
# Instead of storing all the output into one variabele, we create a variable, and store within it the information of one 
# section. Then we print the variabele and empty it, so it can be re-used for a new section.
# 
# In code, this looks like this:

# In[4]:


article_content = ""

for book in root_alto.find_all('TextBlock'):
    for article in book.find_all('String'):
        content = article.get('CONTENT')
        article_content = article_content + " " + content
    print(article_content)
    print("") ## add a linebreak between the separate sessions
    article_content = ""


# Now we have a page of plain text that is better structured. 
# The only thing left is to retreive the page number, and then we'll have all the information to save this data to a textfile.
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML file. Where can we find the page number?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The page number is stored in the 'Page' element. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Write the code to extract the page number from the XML. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# for book in root_alto.find_all('Page'):
#     pagenr = book.get('ID')
#     print(pagenr)
# ```
# ````
# 
# The page number is:

# In[5]:


for book in root_alto.find_all('Page'):
    pagenr = book.get('ID')
    print(pagenr)


# ## Load the Didl file and examine the structure 
# 
# We now have a more readable page with the corresponding page number. However, if we store this as is, we will have no idea from which newspaper this page was extracted. This makes it of limited reuseability. 
# In lesson 6 we described that we can find metadata corresponding to an Alto file in a Didle file. 
# The alto and didle file have the same identifier, so you can match them.
# 
# In our case, they both have the identifier 1. 
# 
# ```{admonition} Exercise
# :class: attention
# Load the corresponding Didl file in your notebook. Name the root 'root_didl'. Look at the structure of the file. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# with open("data/didl_id1.xml", encoding='utf8') as f:
#     root_didl = BeautifulSoup(f, 'xml')
# print(root_didl)
# ```
# ````
# 
# This leads to the following output:

# In[6]:


with open("data/didl_id1.xml", encoding='utf8') as f:
    root_didl = BeautifulSoup(f, 'xml')
print(root_didl)


# ```{admonition} Exercise
# :class: attention
# Look at the Didle file and see if you can find in which element the title of the newspaper is scored. Hint: the title is 'Algemeen Handelsblad'. 
# What parent of this element contains all information we need to extract the title and the publication date?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The title is stored in the element 'title', and the publication date in the element 'date'. 
# They can both be found in an element called 'Resource'. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Are there any namespaces in the file that we have to take into account? 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# Yes, there are multiple namespaces in the Didle file, both with in element tags and in element attributes.
# However, since we work with Beautiful Soup, we don't have to bother about them. 
# ```
# 
# ## Extract newspaper metadata from the Didl file
# 
# We have seen that the element 'resource' contains all the information we want. If we look closely at the file, 
# we see that there are multiple elements with the name 'resource', but the one we want is the first. 
# If you want all the information from all resource blocks, we can use the findall method as we did before. 
# However, we now only want information from the first block. In that case, you can just simply use find() as follows:
# 
# ```
# item = root_didl.find('Resource')
# ```
# This will return the first element it finds. 
# 
# 
# ```{admonition} Exercise
# :class: attention
# Write a code that gets the only the first 'Resource' element, and then from this element create a for loop that loops through the dcx element. 
# Extract the title of the newspaper and the publication date. Store them in two separate variables. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```
# item = root_didl.find('Resource')
# 
# for article in item.find_all('dcx'):
#     title = article.find('dc:title')
#     date = article.find('dc:date')
#     print(title.text, date.text) 
# ```
# ````
# 
# This leads to the following output:

# In[7]:


item = root_didl.find('Resource')

for article in item.find_all('dcx'):
    title = article.find('dc:title')
    date = article.find('dc:date')
    print(title.text, date.text) 


# Now we can store the content of this newspaper page in a text file with as name the a combination of the title of the newspaper, the publication date, and the page number. 
# We can create the filename like this:
# 
# ```
# filename = f'{title}_{date}_{pagenr}.txt'
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Save the content in a file.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```
# with open(filename, "w", encoding="utf-8") as f:
# 	f.write(article_content)
# ```
# ````
# 
# ## Extract all separate articles from the total newspaper from the Didl file 
# 
# As you saw in the above sections, the Alto format has no clear separation between the articles and is therefore especially suitable when you are interested in the complete newspaper page.
# 
# However, there are a lot of cases in which you would be interested in the separate articles en metadata about these articles (for example, the type of article).
# 
# The collection of the KB makes use of Didl XML files to store additional information. You can use the Didle XML to extract this information and to gather the articles. 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the Didl file, do you see information about the articles?
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Yes, they are stored in the 'Resource' elements.  
# ```
# <didl:Resource mimeType="text/xml">
# <srw_dc:dcx>
# <dc:subject>artikel</dc:subject>
# <dc:title>Het jaar 1869.</dc:title>
# <dcterms:accessRights>accessible</dcterms:accessRights>
# <dcx:recordIdentifier>ddd:010097934:mpeg21:a0001</dcx:recordIdentifier>
# <dc:identifier>http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001</dc:identifier>
# <dc:type xsi:type="dcterms:DCMIType">Text</dc:type>
# </srw_dc:dcx>
# </didl:Resource>
# ```
# ````
# 
# As you can see, there are blocks with information about the articles. The articles themself are not present in the Didl, but we can retreive them through their identifier. To do this we will perform the following two steps:
# 
# - Extract article information and identifier from the Didl;
# - Download the articles and extract the plain text.
# 
# We start by extracting the subject, title and identifier from the resource element. 
# However, as we saw before, there is also other information stored in the resource elements, such as the news paper title
# and publication date. 
# 
# You can distinguish the articles using the newspaper metadata based on the element 'subject'.
# All articles have a subject ('artikel', 'familiebericht' etc) whilst the other metadata does not.
# 
# This distinction can be done with an 'if' statement, in which we check if there is a element with the name 'subject' present in the element block. 
# 
# We will start with extracting the type of article, title, and identifier from the Didl XML. The identifier will later be used to download the articles.

# In[8]:


for item in root_didl.find_all('Resource'):
	for article in item.find_all('dcx'):
		a_type = article.find('subject')
		## The first block will not have a subject as it contains newspaper metadata instead of article metadata.
		## This can be filtered out using an 'if [subject] is None' control structure.
		if a_type is not None:
			title = article.find('title')
			identifier = article.find('identifier')
			print(a_type.text, title.text, identifier.text)


# ```{admonition} Exercise
# :class: attention
# Adapt the code above to store the variables into a list of articles.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below:
# ```
# article_list = []
# 
# for item in root_didl.find_all('Resource'):
# 	for article in item.find_all('dcx'):
# 		a_type = article.find('subject')
# 		## The first block will not have a subject as it contains newspaper metadata instead of article metadata.
# 		## This can be filtered out using an 'if [subject] is None' control structure.
# 		if a_type is not None:
# 			title = article.find('title')
# 			identifier = article.find('identifier')
# 			article_list.append([a_type.text, title.text, identifier.text])
# ```
# ````
# 
# Now we have the identifier for every article in the dataset. This identifier can be used to download the XML of its article 
# and extract the text from it. We will demonstrate this for one article. 
# 
# As an example, we will use the identifier 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001'. 
# If we  click on this, we will be led to the image of the newspaper page on the digitale heritage website Delper.nl (property of the KB). 
# However, if we were to add ':ocr' to the identifier, we will be led to the XML containing the OCR of that newspaper page: 
# 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
# 
# This OCR can be saved to file, either manually or by using Python.
# 
# To save the OCR using Python we will need the *urllib* package.
# 
# ```{note}
# We recommend to always save the identifier in the name of the file, in this case the ***a0001*** indicates the article number, so we will save the whole identifier. Because Windows does not allow ***:*** in filenames we  will change this to an underscore. 
# Everything before ***urn*** will be removed from the identifier, as it has no distinguish features.
# We can perform these alteration through string manipulations in Python. 
# ```

# In[9]:


## import urllib, it is a standard library so does not need to be installed
from urllib.request import urlopen

filename = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
## Remove the first part from the filename, so you keep only ddd:010097934:mpeg21:a0001:ocr'
filename = filename.split('=')[1]
## Replace the : with _
filename = filename.replace(':', '_')

url = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'

## write XML to file, downloading happens in this step too.
with open(filename + ".xml", "w", encoding="utf-8") as f:
    f.write(urlopen(url).read().decode('utf-8'))


# Now, we can open this xml file and look at the structure.

# In[10]:


with open("ddd_010097934_mpeg21_a0001_ocr.xml", encoding='utf8') as f:
    root_article = BeautifulSoup(f, 'xml')
print(root_article)


# ```{admonition} Exercise
# :class: attention
# Extract the title and content from the article, and store these in separate variables.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below
# ```Python
# for titles in root_article.find_all('title'):
#     title = titles.text 
# 
# for contents in root_article.find_all('p'):
#     content = contents.text + "\n"
# ```
# ````
# 
# This can than be saved to a textfile
# 
# ```Python
# with open(filename + ".txt", "w", encoding="utf-8") as f:
#     f.write(title + "\n" + content)
# ```
# 
# The above workflow now consists of the folowing steps:
# - Downloading the file;
# - Opening the file;
# - Extracting the contents;
# - Saving the contents to file.
# 
# This can also be combined into one piece of code that handles all these steps. An advantage of this method is that 
# there is no need to manually save and re-open every separate article file. 
# 
# ```Python
# from urllib.request import urlopen
# 
# identifier = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
# filename = identifier.split('=')[1]
# filename = filename.replace(':', '_')
# 
# file=urlopen(identifier)
# root = BeautifulSoup(file, 'xml')
# 
# for titles in root.find_all('title'):
#     title = titles.text + "\n"
# 
# for contents in root.find_all('p'):
#     content = contents.text + "\n"
# 
# with open(filename + ".txt", "w", encoding="utf-8") as f:
#     f.write(title + "\n" + content)
# ```
# 
# Until now we have manually selected a single article from a page and saved this. Of course one article is generally not enough and manually changing the identifier for every file is a lot of work.
# Luckily, just as we have used a for loop to iterate through an XML file, we can use a for loop to iterate through a list of identifiers.
# 
# The folowing code does just that. It iterates through **article_list** and grabs the identifier of an article. 
# Then it adds *:ocr* behind the identifier, downloads the file, and extracts the text. 
# Finally, it saves the result as a textfile, with the identifier as filename.
# 
# ```Python
# from urllib.request import urlopen
# 
# for article in article_list:
#     # We want the third object of the list, but Python counts from 0.    
#     identifier = article[2] + ":ocr"
#     # Prepare the filename
#     filename = identifier.split('=')[1]
#     filename = filename.replace(':', '_')
#     
#     # Download the xml and load into Python
#     file=urlopen(identifier)
# 	root = BeautifulSoup(file, 'xml')
# 
#     
#     #Extract the content
# 	for titles in root.find_all('title'):
# 		title = titles.text + "\n"
# 
# 	for contents in root.find_all('p'):
# 		content = contents.text + "\n"
#         
#     # Some content, like advertisements, have no titles. 
# 	if title is None:
#         article = content
#     else:        
#         article = title + "\n" + content
#         
#     #Save the content in a file 
#     with open(filename + ".txt", "w", encoding="utf-8") as f:
#         f.write(article)
#  
# ```
# 
# ## Extract all separate articles from a specific page of the newspaper from the Didl file
# 
# In the above we treated two options:
# * Extracting the whole content of a page and saving into one file;
# * Extracting all the articles of a newspaper and saving this to file per article.
# 
# It is also possible to download the articles per page.
# If you look into the XML file you will see the element 'Component' with the attribute 'dc:identifier'.
# For example:
# ```XML
# <didl:Component dc:identifier="ddd:010097934:mpeg21:p001:a0003:zoning">
# ```
# 
# In this case the ***p001*** indicates that this concerns the first page. 
# If the code to retrieve all the articles from a newspaper is adapted to loop via the element 'Component' instead of 
# the element 'Resource , it becomes possible to filter out those elements whose attribute contains ***p001***. This can be done using: 
# 
# ```Python
# if 'p001' in [variable in which the content of dc:identifier is stored]
# ```
# 
# Then the rest of the code can be made similarly to the code we used to extract all identifiers of all articles of the whole newspaper. 
# 
# ```{admonition} Note
# If an ***attribute*** has a namespace, you HAVE to add the namespaces prefix before the attribute name in Beautiful Soup 
# for it to recognize it. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Write code to collect the identifiers from page 1 and store them row by row in a Dataframe together with the pagenumber, type of text, and title. Then print this Dataframe.
# 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below:
# ```Python
# article_list = []
# 
# # Declare the page variable here so it can easily be changed
# article_list = []
# page = 'p001'
# 
# for item in root_didl.find_all('Component'):
#     identifier_page = item.get('dc:identifier')
#     if page in identifier_page:
#         for article in item.find_all('dcx'):
#                 a_type = article.find('subject')
#                 if a_type is not None:
#                     title = article.find('title')
#                     identifier = article.find('identifier')
#                     article_list.append([page, a_type.text, title.text, identifier.text])
#  
# import pandas as pd
# articles = pd.DataFrame(article_list, columns = ['Page', 'Type', 'Title', 'Identifier'])
# 
# articles
# ```
# ````

# In[11]:


article_list = []
page = 'p001'

for item in root_didl.find_all('Component'):
    identifier_page = item.get('dc:identifier')
    if page in identifier_page:
        for article in item.find_all('dcx'):
                a_type = article.find('subject')
                if a_type is not None:
                    title = article.find('title')
                    identifier = article.find('identifier')
                    article_list.append([page, a_type.text, title.text, identifier.text])
 
import pandas as pd
articles = pd.DataFrame(article_list, columns = ['Page', 'Type', 'Title', 'Identifier'])

articles


# You now have a dataframe with metadata from all articles of one page. You can use the same steps as described above to download the content from this articles and store them in textfiles.
