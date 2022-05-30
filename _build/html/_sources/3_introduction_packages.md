# 3. Introduction to the packages ElementTree and Beautiful Soup

In the previous two sections we introduced Python and XML. The structured way XML is built makes it relatively easy to navigate it and obtain the required data programmatically. 
With Python there are multiple ways of extracting data and information from XML files. The most straightforward is to use packages that are specifically built to deal with XML.

In this section we will introduce two packages that are commonly used when dealing with XML: *ElementTree* and *Beautiful Soup*.

## ElementTree

*ElementTree* is a built-in package of Python. The benefit of this is that it is already present in the base Python installation and therefore no extra packages need to be installed. 
This means less complexity and dependencies, which can make it more reproducable and easier to maintain.
When working with ElementTree, it is important to specify the hierarchy precisely or to specificly 'escape' the hierarchy for subelements, or it does not find them. Also, namespaces need to be declared for ElementTree to recognize them. 
*ElementTree* has specifically been designed to work with XML files. It features tools to navigate and manipulate XML files in multiple ways and is generally held to be intuitive.

## Beautiful Soup
 
*Beautiful Soup* is one of the most popular packages for webscraping with Python. Not specificially built for XML, HTML and XML have a very similar structure. Because of this similarity Beautiful Soup is also able to parse XML files. 
However, it is best to use it in conjunction with the *lxml* package. In contrast to ElementTree, in Beautiful Soup you do not need to declare the hierarchy when you want to reach subelements. 
It will always search the all elements nested in the element you specified. It also does not need you to declare namespaces. 
However: when an attribute has a namespace, you need to add the namespace prefix before the attribute name, or Beautiful Soup won't recognize the element.
*Beautiful Soup* comes with numerous methods for searching XML and is very popular due to its neat style. It is also one of the few packages that has no problems dealing with broken or non-standard XML.
 
## Which is best?

Which package is the right tool for a project depends on the requirements. Each has its own benefits and drawbacks and it mostly comes down to personal preferences. 

ElementTree is included with Python, which means there are less dependencies on other packages and less chance of version. This also makes it slightly easier to maintain. 
ElementTree has also been developed with XML parsing in mind, the whole package is geared towards XML.
A downside is the specific need of hierarchy and namespace declaration. 

Beautiful Soup is very versatile and can parse HTML and XML with ease. This is especially good if the project involves XML and HTML in any way.
Beautiful Soup is also able to work with broken and non-standard XML. Which can be very beneficial in research settings.
A downside of Beautiful Soup is that is requires an additional package (lxml) to be installed for optimal use. While this should not give any problems, it does increase the chance of version and dependency conflicts.

Switching between packages can be somewhat challenging as both implement their code is slightly different ways. However, when running into problems parsing a certain XML file it is always good to know that there may be another package that may be able to help.

The similarities and differences in an overview:

|                              					| ElementTree | Beautiful Soup                                              |
|-----------------------------------------------|-------------|-------------------------------------------------------------|
| Is part of the standard Python installation 	| Yes 		  | No 															|
| Needs to be installed        					| No          | Yes                                                         |  
| Needs an explicit hierarchy 					| Yes         | No                                                          |  
| Needs namespace declaration  					| Yes         | No (however, for attributes the namespaces prefix be added) | 
| Can work with malfunctioning XML files 		| No 		  | Yes 														|