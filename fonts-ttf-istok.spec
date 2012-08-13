%define pkgname istok-ttf

Summary:	Sans serif typeface
Name:		fonts-ttf-istok
Version:	1.0
Release:	%mkrel 1
License:	GPLv3 with font exception
Group:		System/Fonts/True type
URL:		http://code.google.com/p/istok/
Source0:	http://istok.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
Istok is new sans serif typeface. At present it has four fonts
with support for Latin and Cyrillic. Most glyphs are manually instructed using
xgridfit, but another ones are autoinstructed in fontforge. Truetype
instructions are specifically intended for rendering on LCD displays.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/istok

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/istok
ttmkfdir %{buildroot}%{_xfontdir}/TTF/istok -o %{buildroot}%{_xfontdir}/TTF/istok/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/istok/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/istok \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-istok:pri=50

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog AUTHORS TODO
%dir %{_xfontdir}/TTF/istok
%{_xfontdir}/TTF/istok/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/istok/fonts.dir
%{_xfontdir}/TTF/istok/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-istok:pri=50
