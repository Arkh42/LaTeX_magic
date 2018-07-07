%                    %
%%                  %%
%%% IDENTIFICATION %%%
%%                  %%
%                    %

% Version of LaTeX required
\NeedsTeXFormat{LaTeX2e}

% Class declaration
\ProvidesClass{_class_template}[2018/07/07 Additional information about the _class_template class]%mandatory argument is the file name without the .cls extension


%                              %
%%                            %%
%%% PRELIMINARY DECLARATIONS %%%
%%                            %%
%                              %

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

% New option (useful commands: \CurrentOption, \OptionNotUsed, PassOptionsToPackage{options-list}{package-name}, \PassOptionsToClass{options-list}{class-name})
\DeclareOption{option_name}{code}

% Management of not explicitly declared options (default: warning)
\DeclareOption*{code}

% Default option list
\ExecuteOptions {options-list}

% Processing the options
\ProcessOptions\relax


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