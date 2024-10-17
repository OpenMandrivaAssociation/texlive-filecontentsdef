Name:		texlive-filecontentsdef
Version:	52208
Release:	2
Summary:	filecontents + macro + verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filecontentsdef
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontentsdef.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two environments called filecontentsdef
and filecontentshere. They are derived from the LaTeX
filecontents environment as provided by Scott Pakin's
filecontents package. In addition to the file creation they
either store the (verbatim) contents in a macro
(filecontentsdef) or typeset them (verbatim) on the spot
(filecontentshere). The author developed the package to display
TeX code verbatim in documentation and the same time produce
the corresponding files during the LaTeX run in order to embed
them in the PDF as file attachment annotations (by using Scott
Pakin's package attachfile).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/filecontentsdef
%{_texmfdistdir}/tex/latex/filecontentsdef
%doc %{_texmfdistdir}/doc/latex/filecontentsdef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
