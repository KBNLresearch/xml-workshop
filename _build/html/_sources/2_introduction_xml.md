# 2. Introduction to XML 

## XML

XML stands for eXtensible Markup Language. It is a language (but not a programming language) which goal is to store and transport data in a structured manner. It was designed to be self-descriptive and to be both human and machine readable. Because XML presents data in a structured format, and because it is platform independent, it is a popular format for applications to communicate. 
XML itself does not do anything. 

XML is very common in DH research and knowing how to process XML documents is an invaluable skill. 

## XML Structure

Below is a short example of XML:

```XML
<?xml version="1.0"?>
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
		<description>An in-depth look at creating applicationswith XML.</description>
	</book>
</catalog>
```

Although at first this may look unfamiliar, the XML above is mostly self-descriptive:
- It is a catalog;
- It contains a book; 
- It contains information about that book; 
- It has a description of the book.

This XML structure is called a *tree* and contains so-called elements. 

```{admonition} Exercise 
:class: attention
Looking at the example XML, what is the title of the book?
```

```{admonition} Solution
:class: tip, dropdown
The title of the book is: "XML Developer's Guide". This can be found by looking at the *tags* with the name 'title', more about these later.
```

## XML Tree

Similar to a real tree, an XML tree starts at a *root* and branches out into *childeren*.
Each of these children can have *sub childeren*. These root and childeren are called *elements*. 

The basic structure is this:
```XML
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```
The relation between elements is described with the terms *parent*, *child*, and *sibling*.
Like family trees, parents are on the top level, children below parents and siblings are on the same level.

````{admonition} Exercise 
:class: attention
Looking at the example XML,
1. What is the root element?
2. Does the element *book* have subchildren?
3. What are the siblings of *author*?
```XML
<?xml version="1.0"?>
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
		<description>An in-depth look at creating applicationswith XML.</description>
	</book>
</catalog>
```
````

```{admonition} Solution
:class: tip, dropdown
1. The root element is the first element of the tree. In this case it is *catalog*.
2. The element *book* has 2 subchildren, *name* and *surname*.
3. The siblings of author are: *title*, *genre*, *price*, *publish_date*, and *description*.
```

## Prolog

XML usually starts with the *prolog* a piece of code that defines the XML version and can contain character encoding. The prolog is optional, and if present it must come first in the document. It is good practice to include it.

For our example the prolog is:
```XML
<?xml version="1.0"?>
```

## Elements

All elements follow the same basic structure:

```
<Opening tag> + content + </closing tag> = element
```

Elements consist of tags that describe the element, and content.
Most of the time, tags come in pairs: an opening tag and a closing tag. These are enclosed in **<>**.
Tags of an element must always be identical to each other, except that the closing tag includes a **/** before the tagname.
When an element is empty, a selfclosing tag can be used, which is an opening and closing tag in one. This looks like this:
```
<tagname /> 
```

Because of this structured build elements are self-describing.
One element in the example XML above is the title:

```XML
<title>XML Developer's Guide</title>
```

In the above example 
```
<title>
```
is the opening tag, 'XML Developer's Guide' is the content and 
```
</title>
``` 
is the closing tag. 

An element can contain other elements, such as in our first example. 
The element *book* contains the elements *author*, *title*, *genre*, *price*, *publish_date*, and *description*

As mentioned before, elements can also be empty, having tags but no content.

````{admonition} Exercise 
:class: attention
Looking at the example XML, what elements does the element *author* contain?
```XML
<?xml version="1.0"?>
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
		<description>An in-depth look at creating applicationswith XML.</description>
	</book>
</catalog>
```
````

````{admonition} Solution
:class: tip, dropdown
The element *author* contains the elements *name* and *surname*.
```XML
<author>
	<name>Matthew</name> 
	<surname>Gambardella</surname>
</author>
```
````

## Attributes

Elements can have attributes. Attributes give more information about XML elements and are used to distinguish between elements with the same name. Attributes always consists of a name-value pair.

Returning to our example XML, the element *book* has an atribute *id*.
```XML
<book id="bk101"> </book>
```
This attribute contains the unique id of the book. This is usefull as there may be books with the same name, and this way these can be identified separately. Attribute values are always quoted. 

## Namespaces

Tag names are defined by the person or application building the XML. Therefore, it is possible that different software use the same tag names for some or even all their elements. This can lead to problems when mixing XML from different applications. 

For example, below are two pieces of XML (Example XML re-used from [msdn-magazine](https://docs.microsoft.com/en-us/archive/msdn-magazine/2001/july/the-xml-files-understanding-xml-namespaces)). 
Both contain elements provide information about a student. 

```XML
<student>
  <id>3235329</id>
  <name>Jeff Smith</name>
  <language>Python</language>
  <rating>9.5</rating>
</student>

<student>
  <id>534-22-5252</id>
  <name>Jill Smith</name>
  <language>Spanish</language>
  <rating>3.2</rating>
</student>
```

The first contains information about a student following a Python course: their student number, name, the language studied in the course, and how they rated the course on a ten-point scale. 

The second contains information about an elementary school student: their social security number, name, native language and average rating on a five-point scale. 

Although the tag names are identical in both versions, they have very different meanings and are quite unmixable. 
But when querying the XML a machine will not know that difference and simply lump them together.

These naming conflicts can be resolved by using prefixes. This prefixes essentially work as an identifier for a specific XML structure.

The following example shows the XML with prefixes.

```XML
<p:student xmlns:p="http//www.imaginarypythoncourses.com/student">
  <p:id>3235329</p:id>
  <p:name>Jeff Smith</p:name>
  <p:language>Python</p:language>
  <p:rating>9.5</p:rating>
</p:student>

<e:student xmlns:e="http//www.isthisevenarealschool.com/students">
  <e:id>534-22-5252</e:id>
  <e:name>Jill Smith</e:name>
  <e:language>Spanish</e:language>
  <e:rating>3.2</e:rating>
</e:student>
```

You can see that the part about the Python student has the prefix 'p', and the part about the elementary school kid has 
the prefix 'e'. Now there will not be any conflict as the prefix ensures that a machine will see the difference between the 
tag names. 

The prefix is not the only addition to the code. This is because when using prefixes, they must be assigned to a ***namespace***. 
A namespace must be declared within the XML structure, be it the root or the element it applies to. 
A namespace helps the machine to interpret the prefixes. Multiple namespaces can be used in an XML file. 

In the example of the Python student, the namespace is:

```XML
xmlns:p="http//www.imaginarypythoncourses.com/student"'
```

The general namespace syntax is:
```
xmlns:<prefix>='<namespace identifier>'
```

Most OCR software use namespaces. If you are not familiar whith them, they can cause some unexpected behavior while parsing XML files with Python. 
So being able to understand and utilize namespaces is very important.

## Comments

In XML comments may be added, these can contain descriptions about the data or other information.
Comments are written as:
```XML
<!-- This is a comment -->
```

## Rules

There are some rules regarding XML.
* Each tags must have a closing tag;
* Tag names are case sensitive, in XML title, Title, and TITLE are three different tag names;
* Tag names can only begin with a letter or an underscore;
* Tag names can contain letters, digits, hyphens, underscores, and periods. No other signs are allowed, including spaces;
* XML documents **must** have a root element.

````{admonition} Exercise 
:class: attention
Keeping the rules in mind, is the following XML correctly defined? If not, what is wrong?
```XML
<book>
	<author>
		<name>Matthew</name>
		<surname>Gambardella</surname>
	</Author>
	<title>XML Developer's Guide
	<price>44.95</price>
	<publish_date>2000-10-01</publish_date>
	<description>An in-depth look at creating applications with XML. /description>
</book>

	<author>
		<name>Kim</name>
		<surname>Ralls<surname>
	</author>
	<title>Midnight Rain</>
	<price/>5.95</price>
	<publish_date>v</publishdate>
	<description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.. </description>
</book>

```
````

````{admonition} Solution
:class: tip, dropdown
From top to bottom:
1. There is no root present;
2. The first author tags are not the same, as the second one has a capital 'A'. Therefore, XML sees them as two different tags. 
3. The first title missed an closing tag;
4. The first description closing tags misses an '<';
5. The second surname misses an '/' in the closing tag;
6. The second title is missing the tagname 'title' in the closing tag;
7. The second price opening tag is a selfclosing tag, the '/' needs to be removed;
8. The second publishing date tags are not the same, as one has an underscore. 
````

## Exercise

You should now have a decent grasp of the structure and rules of XML. 
As a final excercise you will construct your own piece of XML using the data below.

````{admonition} Exercise 
:class: attention
Create a small piece of XML containing a catalog of newspapers. The following data must be in the XML:
* newspaper title
* publication date
* number of pages

Create the catalog for the following newspapers:
* Algemeen Handelsblad, 01-01-1870, 4 pages
* Trouw, 04-07-1970, 24 pages
````

````{admonition} Solution
:class: tip, dropdown
```XML
<catalog>
	<newspaper>
		<title>Algemeen handelsblad<?/title>
		<publication_date>01-01-1870</publication_date>
		<pages>4</pages>
	</newspaper>
	<newspaper>
		<title>Trouw</title>
		<publication_date>04-07-1970</publication_date>
		<pages>24</pages>
	</newspaper>
</catalog>
```
````


This concludes this brief introduction to XML. The next section will forcus on some common Python packages that are used to extract data and information from XML. 



