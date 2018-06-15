# LaTeX_magic tutorials



## Organisation

Each tutorial is contained in a folder which includes the following documents:
* an 'Examples' folder which include several *.tex example files to provide reade-to-use LaTeX codes to the user,
* a 'Quick_reference.*' file which is the main part of the tutorial,
*  a 'README.md' file which provides a short description of the content and references.

### Contents

| Index   | Title                           | Short description														| Status	|    
| :-----: | :------------------------------ | :-------------------------------------------------------------------- | :-----:	|
|  B001   | Installing LaTeX				| Distributions, editors, advices.										| TD		|
|  B002   | Compiling LaTeX					| Existing compilers, features, choice.									| V			|
|  B003   | Setting Language and Typography	| Font encoding & selection, language's rules, typography.				| TD		|
|  B004   | Choosing Document Class			| Existing document classes, features, choice.							| TD		|
|  Cxxx   | References						| Clickable table of contents, references to anything (e.g., figures).	| TD		|
|  Cxxx   | Floats							| Floats management, *sub*-environments, advanced tables.				| TD		|
|  Cxxx   | Mathematics						| Main environments, theorems.											| TD		|

*Legend*

* V = 	done,
* TD =	to do.


## Rules for contribution


### How to name a tutorial

The folder including the whole tutorial must be named according to the following template:
*Xyyy__short_description*,
where
* *X* is a letter indicating the target audience (see table below),
* *yyy* is a number (starting from 001) for indexing the tutorial,
* *short_description* is a short title describing the subject of the tutorials
(single underscores must be used between each word).

| Letter  | Description                              |        
| :-----: | :--------------------------------------- | 
|    B    | Mainly for beginners.                    | 
|    C    | Classic subject: frequently asked.       |
|    S    | Specialised subject: for advanced users. |


### How to write the explanations inside a tutorial

Explanations must comply with the following rules:
* explanations shall be written in English as main language, even though other languages can be used
to illustrate a specific feature (e.g., typography);
* explanations shall be written with one of the following formats
	* LaTeX (first choice);
	* Markdown.

	
### Which files to commit

Only source files (\*.tex, \*.bib, \*.cls, \*.sty) and result files (\*.pdf) must be committed.
