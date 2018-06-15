# Setting language and typography

This tutorial explains how to set the language in LaTeX in order to automatically respect the typographical rules of the specified language.
It also provide a short description about font encoding and font selection.

User's attention must be drawn on the fact that **the setting is compiler-dependent**.


## References

From CTAN:
* the [inputenc](https://ctan.org/pkg/inputenc) package,
* the [fontenc](https://ctan.org/pkg/fontenc) package,
* a document about [LaTeX font encodings](https://ctan.math.illinois.edu/macros/latex/doc/encguide.pdf),
* the [fontspec](https://ctan.org/pkg/fontspec) package,
* the [babel](https://ctan.org/pkg/babel) package,
* the [polyglossia](https://ctan.org/pkg/polyglossia) package,
* the [csquotes](https://ctan.org/pkg/csquotes) package,
* the [microtype](https://www.ctan.org/pkg/microtype) package.

Tutorials from the internet:
* [Mais à quoi bon servent les packages ‘fontenc’ et ‘inputenc’ ?](http://blog.dorian-depriester.fr/latex/mais-a-quoi-bon-servent-les-packages-fontenc-et-inputenc),
a very quick and clear explanation about the use of both *fontenc* and *inputenc* packages;
* [LaTeX et encodage](http://www.xm1math.net/doculatex/encodage.html),
mainly focusing on *utf8* and *latin1* (ISO-8859-1) encoding;
* [LaTeX font packages](http://www.icl.utk.edu/~mgates3/docs/latex-fonts.pdf),
a guide about existing packages to use specific fonts.

Fora from the internet:
* [fontenc vs inputenc](https://tex.stackexchange.com/questions/44694/fontenc-vs-inputenc),
* [How to use all variants of Latin Modern Roman with fontspec?](https://tex.stackexchange.com/questions/79086/how-to-use-all-variants-of-latin-modern-roman-with-fontspec),
* [Polyglossia vs Babel](https://tex.stackexchange.com/questions/88481/polyglossia-vs-babel).


## Compilation information

All LaTeX documents in this tutorial have been compiled:
* with compilers included in the TeXLive (2017) distribution,
* under the TeXstudio editor,
* on a Windows 10 OS.