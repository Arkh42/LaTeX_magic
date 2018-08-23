Templates
=========


Contents
--------

| Name									| Short description																	|
| :-------------------------------- 	| :-------------------------------------------------------------------- 			|
| _class_template.cls					| Structure for class definition to speed the writing up.							|
| _class_template__keyval_option.cls	| Structure for class definition with key=value options to speed the writing up.	|
| _package_template.sty					| Structure for package definition to speed the writing up.							|
| _package_template__keyval_option.sty	| Structure for package definition with key=value options to speed the writing up.	|
| report_komascript__EN__LUA_XE.tex		| Report (Koma-Script class) for medium-size document including chapters.			|
| report_komascript__EN__PDF.tex		| Report (Koma-Script class) for medium-size document including chapters.			|
| report_standard__EN__LUA_XE.tex		| Report (standard class) for medium-size document including chapters.				|
| report_standard__EN__PDF.tex			| Report (standard class) for medium-size document including chapters.				|



Rules for contribution
----------------------


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