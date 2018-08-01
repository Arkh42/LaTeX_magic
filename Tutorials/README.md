# LaTeX_magic tutorials



## Organisation

Each tutorial is contained in a folder which includes the following documents:
* an 'Examples' folder which include several *.tex example files to provide ready-to-use LaTeX codes to the user,
* a 'Quick_reference.*' file which is the main part of the tutorial,
* one or several 'Mini_guide*' files that provide a complete description,
* a 'README.md' file which provides a short description of the content and references.

### Contents

| Index   | Title                           | Short description														| Status	|    
| :-----: | :------------------------------ | :-------------------------------------------------------------------- | :-----:	|
|  B000   | Adopting LaTeX					| Some answers to "Why should we (not) use LaTeX?"						| TD		|
|  B001   | Installing LaTeX				| Distributions, editors, advices.										| V			|
|  B002   | Compiling LaTeX					| Existing compilers, features, choice.									| V			|
|  B003   | Setting Language and Typography	| Font encoding & selection, language's rules, typography.				| V			|
|  B004   | Choosing Document Class			| Existing document classes, features, choice.							| TD		|
|  B005   | LaTeX Vocabulary				| Preamble & document, package & class, commands and environments.		| TD		|
|  B100   | Mathematics	 - Basics			| Basics to write mathematics with LaTeX.								| V			|
|  C100   | Maths - Systems					| Systems of equations and functions defined by domains.				| ...		|
|  C101   | Maths - Matrices				| Matrices with different surrounding delimiters.						| V			|
|  C102   | Maths - Derivatives				| How to write systems of equations and functions defined by domains.	| ...		|
|  Xyyy   | References						| Clickable table of contents, references to anything (e.g., figures).	| TD		|
|  Xyyy   | Floats							| Floats management, *sub*-environments, advanced tables.				| TD		|


*Legend*:

* V = 	done,
* TD =	to do,
* ... = ongoing.

### Mini-guide VS Quick reference

Quick references included in each tutorial aim to provide quickly useful information to the reader.
"Quickly" means that a short number of slides are sufficient to understand the topic and to start writing LaTeX.
Quick references are supported by examples including a compilable LaTeX code that helps the user to handle the subject of the tutorial.

However, some readers do prefer a complete text.
To do so, a 'The_LaTeX_mini_guide.tex' file is being written to provide a full tutorial grouping all topics.
This complete tutorial is fed on 'Mini_guide*' files that are available in their related tutorial folder.


## Rules for contribution


### How to name a tutorial

The folder including the whole tutorial must be named according to the following template:
*Xyyy__short_description*,
where
* *X* is a letter indicating the target audience (see table below),
* *yyy* is a number starting from 000 for indexing the tutorial (see table below),
* *short_description* is a short title describing the subject of the tutorials
(single underscores must be used between each word).

| Letter  | Description                              |        
| :-----: | :--------------------------------------- | 
|    B    | Mainly for beginners.                    | 
|    C    | Classic subject: frequently asked.       |
|    S    | Specialised subject: for advanced users. |

| 1st digit | Description                           |        
| :-------: | :-------------------------------------| 
| 	  0		| Usual/Generic topic.					| 
|	  1		| Scientific topic.					    |

Here are a few examples:
* subjects indexed as "B0yy" are general topics for beginners,
* tutorials indexed as "C1yy" focus on scientific topics that are commonly required.


### How to write the explanations inside a tutorial

Explanations must comply with the following rules:
* explanations shall be written in English as main language, even though other languages can be used
to illustrate a specific feature (e.g., typography);
* explanations shall be written with one of the following formats
	* LaTeX (first choice);
	* Markdown.

	
### Which files to commit

Only source files (\*.tex, \*.bib, \*.cls, \*.sty) and result files (\*.pdf) must be committed.
