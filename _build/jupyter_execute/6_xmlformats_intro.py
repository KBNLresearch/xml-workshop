#!/usr/bin/env python
# coding: utf-8

# # 6. Introduction to the Alto/Didle, TEI and Page format
# 
# Although XML is a structured way to store data, the structuring itself is left to the user. This means that there is not one style or format of XML. This has led to a high variety of different formats and styles of storing data and information with XML. To battle this multiple standards have been developed. These standards offer a guideline or framework for developers to store data. 
# 
# In humanities research multiple standards are in use. In this chapter we will shortly describe some of the standards that are commonly used within the KB, national library of the Netherlands, and will be used in this workshop.
# 
# 
# ## Alto
# ALTO (Analyzed Layout and Text Object) is an open XML Schema developed by the EU-funded project called METAe. The standard was developed for the description of text OCR and layout information of pages for digitized material. The goal of this standard was to describe the layout and text in such a way that it would enable the reconstruction of the original appearance. 
# ALTO is often used with a metadata encoding file for the description of the whole digitized object and for creating references across mulitple ALTO files, such as reading order description. Commenly used files are Didl and METS.
# 
# The ALTO standard is hosted by the Library of Congress (USA) and maintained by the Editorial Board initialized at the same time.
# 
# Structure
# An ALTO file consists of three major sections as children of the root <alto> element:
# 
# ```XML
# <alto> 
# 	<Description> section contains metadata about the ALTO file itself and processing information on how the file was created.
# 	<Styles> section contains the text and paragraph styles with their individual descriptions:
# 		<TextStyle> has font descriptions
# 		<ParagraphStyle> has paragraph descriptions, e.g. alignment information
# 	<Layout> section contains the content information. It is subdivided into <Page> elements.
# ```
# 
# ## Didl
# 
# The MPEG-21 Digital Item Declaration Language, Didl, 
# 
# ISO MPEG has sought, in its development of the emerging MPEG-21 standard, to develop a multimedia framework that is capable of supporting the delivery and use of all content types by different categories of users in multiple application domains. Earlier this year, in response to the needs articulated above, the Multimedia Description Schemes (MDS) Group within MPEG released the first working draft of an XML vocabulary, the MPEG-2 Digital Item Declaration Language (DIDL). The overall goal for DIDL was to establish a uniform and flexible multimedia data abstraction and interoperabilty schema for declaring digital items. Within the MPEG-21 framework, a Digital Item is defined as a structured digital object with a standard representation, identification, and description. This Digital Item entity is also the fundamental unit of distribution and transaction within this framework. DIDL is based on an abstract model called the Digital Item Declaration Model. The primary concepts within the model appear below. Many of the model elements have directly corresponding DIDL XML elements.
# 
# 
# <DIDL>
#  <CONTAINER>
#     <DESCRIPTOR>
#       <STATEMENT TYPE="text/plain">Jones family 
#         on-line photo albums</STATEMENT>
#     </DESCRIPTOR>
#     <ITEM>
#       <DESCRIPTOR>
#         <STATEMENT TYPE="text/plain">Album #1: 
#            The Kids</STATEMENT>
#       </DESCRIPTOR>
#       <ITEM>
#         <DESCRIPTOR>
#           <STATEMENT TYPE="text/plain">
#           </STATEMENT>
#         </DESCRIPTOR>
#           <COMPONENT>
#             <RESOURCE REF="Pjn1.jpg" TYPE="image/jpg" />
#           </COMPONENT>
#       </ITEM>
#       <ITEM>
#         <DESCRIPTOR>
#           <STATEMENT TYPE="text/plain">
#               Jane's first day at Jefferson elementary school, 
#               accompanied by her Dad, Robert Williams
#            </STATEMENT>
#         </DESCRIPTOR>
#           <COMPONENT>
#             <RESOURCE REF="Pja1.bmp" TYPE="image/bmp" />
#           </COMPONENT>
#     </ITEM>
#  </CONTAINER>
# 
# </DIDL>    
# ## TEI
# 
# The Text Encoding Initiative (TEI) is a non-profit consortium which collectively develops and maintains a standard for the representation of texts in digital form. They have developed a set of Guidelines which specify encoding methods for machine-readable texts, moestly focused on the humanities, social sciences and linguistics. The TEI Guidelines are widely used by libraries, museums, publishers, and individual scholars to present texts for online research, teaching, and preservation. 
# 
# The TEI Consortium is a non-profit membership organization composed of academic institutions, research projects, and individual scholars from around the world. 
# 
# ``` XML
# Structure
# <TEI xmlns="http://www.tei-c.org/ns/1.0">
# <teiHeader>
# 	<!-- ... -->
# 	 </teiHeader>
# 	 <text>
# 		  <front>
# 		<!-- front matter of copy text, if any, goes here -->
# 		  </front>
# 		  <body>
# 		<!-- body of copy text goes here -->
# 		  </body>
# 		  <back>
# 		<!-- back matter of copy text, if any, goes here -->
# 		  </back>
# 	 </text>
# </TEI>bibliography 
# ```
