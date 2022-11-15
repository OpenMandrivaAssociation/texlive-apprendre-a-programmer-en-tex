Name:		texlive-apprendre-a-programmer-en-tex
Version:	57179
Release:	1
Summary:	The book "Apprendre a programmer en TeX"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apprendre-a-programmer-en-tex
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprendre-a-programmer-en-tex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprendre-a-programmer-en-tex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This book explains the basic concepts required for programming
in TeX and explains the programming methods, providing many
examples. The package makes the compileable source code as well
as the compiled pdf file accessible to everyone. Ce livre
expose les concepts de base requis pour programmer en TeX et
decrit les methodes de programmation en s'appuyant sur de
nombreux exemples. Ce package met a disposition de tous le code
source compilable ainsi que le fichier pdf du livre.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/apprendre-a-programmer-en-tex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
