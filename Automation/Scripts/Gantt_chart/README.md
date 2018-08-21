Script for Gantt chart
======================


This Python script aims the **generation of Gantt chart**
with LaTeX (upon the *pgfgantt* package)
from data contained in a *.csv* file.


Usage
-----


### Create the *.csv

Observing the *csv* format, each line of the file is like:
`symbol, data1, data2, data3, ...`
However, extra space can be added for display purpose:
it will be ignore by the Python script.


The symbol indicates the type of data.
The next table describes the meaning of each symbol and the expected fields:

|	Symbol	|	Meaning						|	field 1			|	field 2				|	field 3				|	field 4			|
|	:----:	|	:------						|	:------			|	:------				|	:------				|	:------			|
|	W		|	Workpackage (group)			|	Description		|	Start date (ISO)	|	End date (ISO)		|					|
|	T		|	Task						|	Label			|	Description			|	Start date (ISO)	|	End date (ISO)	|
|	M		|	Milestone					|	Label			|	Description			|	Start date (ISO)	|	End date (ISO)	|
|	L		|	Link (between two objects)	|	Label object 1	|	Label object 2		|						|					|

Date fields must be written in the ISO format: *yyyy-mm-dd*.
For example, 2018-08-21 is the correct form for the 21st August 2018.

A template file called "User_template.csv" is provided.


### Run the script

The **Gantt_Creator.py** Python script can be run in the following ways:
* from a *Windows* OS,
	* double click on the script file,
* from a *Linux* or a *Mac* OS,
	* open a terminal, go into the directory where the script is located and write `python Gantt_Creator.py`

It will automatically display a file browser to allow you to choose a file.
	
**/!\\** The script is written in Python 3.x.