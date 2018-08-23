%                    %
%%                  %%
%%% IDENTIFICATION %%%
%%                  %%
%                    %


% Version of LaTeX required
\NeedsTeXFormat{LaTeX2e}

% Class declaration
\ProvidesClass{_class_template__keyval_option}[2018/08/23 Additional information about the _class_template__keyval_option class]%mandatory argument is the file name without the .cls extension



%                              %
%%                            %%
%%% PRELIMINARY DECLARATIONS %%%
%%                            %%
%                              %


% Loading 'kvoptions' package to manage key=value options
\RequirePackage{kvoptions}

% Loading 'etoolbox' for programming facilities
\RequirePackage{etoolbox}


% Packages needed in the declared options
\RequirePackage[options]{package-name}[date]


% Commands declaration needed in the declared options
\newcommand*{cmd}{def}
\renewcommand*{cmd}{def}
\DeclareRobustCommand*{cmd}{def}

\newcommand{cmd}{def}
\renewcommand{cmd}{def}
\DeclareRobustCommand{cmd}{def}



%             %
%%           %%
%%% OPTIONS %%%
%%           %%
%             %


% Setup key=value options (examble: 'foobar' family options)
\SetupKeyvalOptions{
	family=foobar,
	prefix=foobar@
}


% New options
\DeclareStringOption[initialValue]{keyName}[default]

\DeclareBoolOption[initialValue]{keyName}
\DeclareComplementaryOption{keyName}{complementName}% Example: \DeclareBoolOption{draft}\DeclareComplementaryOption{final}{draft}

\DeclareVoidOption{optionName}{code}


% Management of not explicitly declared options (default: error)
\DeclareDefaultOption{code}

% Processing the options (examble: 'foobar' family options)
\ProcessKeyvalOptions{foobar}\relax



%                       %
%%                     %%
%%% CORE DECLARATIONS %%%
%%                     %%
%                       %


% Building on another class
\LoadClass[options]{class-name}[date]
\LoadClassWithOptions{class-name}


% Call to specific packages
\RequirePackage[options]{package-name}[date]
\RequirePackageWithOptions{package-name}


% Commands definition
\newcommand*{cmd}{def}
\renewcommand*{cmd}{def}
\DeclareRobustCommand*{cmd}{def}

\newcommand{cmd}{def}
\renewcommand{cmd}{def}
\DeclareRobustCommand{cmd}{def}


% Use of declared StringOption
\ifdefstring{\foobar@keyName}{value}{% if true
	% code if true
}{% else
	% code if false
}

% Use of declared BoolOption
\ifbool{foobar@keyName}{% if true
	% code if true
}{% else
	% code if false
}