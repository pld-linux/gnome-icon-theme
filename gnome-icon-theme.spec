Summary: 	Default icon themes for Gnome2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska Gnome2
Name:		gnome-icon-theme
Version:	0.1.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.1/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/*
