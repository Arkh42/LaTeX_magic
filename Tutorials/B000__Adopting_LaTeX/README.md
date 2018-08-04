# Adopting LaTeX

LaTeX is a very powerful system which aims to help the user in writing well formated documents.
It generates PDF files and possibly embedded metadata and properties.



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


### Example with LaTeX

Let us take the same example.
In LaTeX, to make

text

in bold, you must write

\textbf\{text\}

\textbf\{\} being the command which formats the text in bold.
After compilation, the user will see this:

**text**

as with any other WYSIWYG editor.
Of course, current LaTeX editors provide the same shortcuts as common WYSIWYG editors.
Hence, selecting the text and pressing Ctrl+B will automatically add the \textbf\{\} command.


An expected question could be something like: "Why the hell should I use this horrible tool while a WYSIWYG editor is so easy"?
Well, there are several answers to that:

* you never face an unexpected text formatting because you clearly see the beginning (\{) and the end (\}) of the formatting,
* LaTeX is amazing for typing mathematics,
* LaTeX is crossplatform and is more stable than many text editors which makes teamwork a pleasure instead of a nightmare,
* source files are text files (not binary files), which make versioning tools (e.g., git) very efficient with LaTeX,
* LaTeX is free and open-source.


While it could seem a complex to people not used to programming, it has the advantage to highlight what is done.





## For what LaTeX is well-suited



## For what LaTeX is less suited