%global tl_name filecontentsdef
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	filecontents + macro + verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filecontentsdef
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two environments called filecontentsdef and
filecontentshere. They are derived from the LaTeX filecontents
environment as provided by Scott Pakin's filecontents package. In
addition to the file creation they either store the (verbatim) contents
in a macro (filecontentsdef) or typeset them (verbatim) on the spot
(filecontentshere). The author developed the package to display TeX code
verbatim in documentation and the same time produce the corresponding
files during the LaTeX run in order to embed them in the PDF as file
attachment annotations (by using Scott Pakin's package attachfile).

