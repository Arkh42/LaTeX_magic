# Automating LaTeX

As explained at the root level of this repository, LaTeX is often perceived as difficult to use.
This assertion can be mitigated if two conditions are fulfilled.
On the one hand, clear and concise tutorials must be provided.
On the other hand, user-friendly interfaces must be built so that only the compilation and some usual LaTeX commands remain as the "exotic" use of LaTeX.
The latter is the goal of this section.


## Organisation

The folder is organised as follow:
* Classes
* Packages
* Templates

Here below is shown a list of the content of each part.


### Contents


#### Classes

Empty.


#### Packages

Empty.


#### Templates

| Name							| Short description														|
| :---------------------------- | :-------------------------------------------------------------------- |
| report_standard__EN__LUA_XE	| Report (standard class) for medium-size document including chapters.	|
| report_standard__EN__PDF		| Report (standard class) for medium-size document including chapters.	|


## Rules for contribution


### How to name a template

The template files must be named regarding the following rule:
*class_name__XX__YYY*,
where
* *class_name* is the name of the class on which the template is based,
* *XX* are the letters corresponding to the main language of the template (see table below),
* *YYY* are the letters corresponding to the compilers which can be used for the proposed template.

| Symbol | Compiler	|
| :----: | :------- |
| LUA	 | LuaLaTeX |
| PDF	 | PDFLaTeX |
| XE	 | XeLaTeX  |