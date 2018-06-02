# LaTeX_magic tutorials



## Organisation

Each tutorial is a folder which must include the following folders:
* Examples
* Explanations

In addition, a "README.md" file, located at the tutorial's root level, must provide a short description 
of the content.



## Rules


### How to name a tutorial

The folder including the whole tutorial must be named according to the following template:
*Xyyy__short_description*,
where
* *X* is a letter indicating the target audience (see table below),
* *yyy* is a number (starting from 001) for indexing the tutorial,
* *short_description* is a short name describing the subject of the tutorials
(single underscores must be used between each word).

| Letter  | Description                              |        
| :-----: | :--------------------------------------- | 
|    B    | Mainly for beginners.                    | 
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
