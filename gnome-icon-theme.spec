Summary: 	Default icon themes for Gnome2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska Gnome2
Name:		gnome-icon-theme
Version:	1.0.4
Release:	1
License:	GPL
Group:		Themes
# Source0-md5:	23ef19615dcf27e09ff3edc8f69b2af8
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for Gnome2 enviroment.

%description -l pl
Domy¶lne motywy ikon dla ¶rodowiska Gnome2.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/icons/*
