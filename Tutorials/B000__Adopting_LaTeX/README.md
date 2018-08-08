# Adopting LaTeX

LaTeX is a very powerful system which aims to help the user in writing well formated documents.
It generates PDF files and possibly embedded meta-data and properties.

To avoid bad surprises, we will first illustrate that LaTeX is not a WYSIWIG editor.
Then we will review the cases for which LaTeX is well suited and the ones for which it is less suited.



## LaTeX is not WYSIWYG

Contrary to other known text editor, LaTeX is not WYSIWYG (What You See Is What You Get) but must be compiled.


### Example with a WYSIWYG editor

For the users who do not know what WYSIWYG mean, let us take an example: format a text in bold.
So, we start with this:

text

With a WYSIWYG editor, 
you select the text, then you click on the bold formatting button, 
or you press the equivalent shortcut (usually Ctrl+B), and you end up with:

**text**

The user does not know how the program handles the bold formatting.
He actually *sees* that the text is bold.
This is the meaning of "What You See Is What You Get".


### Example with LaTeX

Let us take the same example.
In LaTeX, to turn

text

in bold, you must write

\textbf\{text\}

\textbf\{\} being the command which formats the text in bold.
After compilation, the user will see this:

**text**

as with any other WYSIWYG editor.
Of course, current LaTeX editors provide the same shortcuts as common WYSIWYG editors.
Hence, selecting the text and pressing Ctrl+B will automatically add the \textbf\{\} command.



## For what LaTeX is well-suited

An expected question could be something like: "Why the hell should I use this horrible tool while a WYSIWYG editor is so easy"?
Well, there are several answers to that.

Here follows a summary of the LaTeX's features:
* free and open-source,
* cross-platform,
* teamwork-friendly,
* layout and typography automatic handling,
* enhanced mathematics typing,
* compatible with versioning tools.

Each characteristic is explained here below.


### LaTeX is free and open-source

If you care about sharing (*open-source* philosophy),
if you care about money (and honestly who does not),
if you are afraid about licensing for using programs...
do not. LaTeX is here for you.


### LaTeX is cross-platform 

LaTeX works on Linux, Windows and Mac, and it works on many versions of them.


### LaTeX is intended for teamwork

Who has never faced the destruction of a document's layout because two team-mates used different versions of the same text editor?
Well, if you make sure at the very beginning to encode your documents the same way (e.g., UTF-8) and to use the same compiler, you will never face problems with LaTeX.
In addition, LaTeX is quite stable thanks to the way it is built and extended (today, mainly through packages and classes).
Therefore, it makes teamwork a pleasure instead of a nightmare.

Today, it also exists platforms dedicated to LaTeX team-working.
As an example, the more and more popular [Overleaf](https://www.overleaf.com/).


### LaTeX handles automatically many important features

Based on document classes (report, books, etc.), LaTeX automatically sets the *layout*.
LaTeX's philosophy is the following: class authors (the ones who like preparing documents layout) cares about margins, sections styling and other characteristics which belong to the documents layout.
Then, the document writer writes his text and does not care about the layout: LaTeX handles it for him.
And, in most cases, LaTeX can be trusted because it is based on internal rules which have been created by people who analysed what makes a document good-looking.

Even more interesting, LaTeX automatically handles the bibliography better than any other text editor I have ever tried.
For instance, in French, a semi-colon must be preceded by a fine space, while in English there is no space.
Many writers do not know it and in fact do not (want to) care about that.
Well, the do not need to.


### LaTeX makes mathematics typing a pleasure

LaTeX is amazing for typing mathematics.
Even though the user must learn the commands corresponding to mathematic symbols, from my own experience, I have never seen any other editor performing so well for rendering mathematics.


### LaTeX works perfectly with versioning tools

Source files are text files (not binary files), which make versioning tools (e.g., [git](https://git-scm.com/)) very efficient with LaTeX.
This is true for documents writing but also for classes and packages (which are base elements to configure LaTeX's behaviour).



## For what LaTeX is less suited

TODO