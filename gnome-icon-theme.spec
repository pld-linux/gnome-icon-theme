Summary:	Default icon themes for GNOME2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME2
Name:		gnome-icon-theme
Version:	1.1.4
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	ea2327112f03372fdbc9521a4f641ffb
URL:		http://www.gnome.org/
BuildRequires:	intltool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for GNOME2 enviroment.

%description -l pl
Domy¶lne motywy ikon dla ¶rodowiska GNOME2.

%prep
%setup -q

%build
glib-gettextize --force
intltoolize --force
%{__aclocal}
%{__autoconf}
%{__automake}
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
%{_datadir}/icons/*
%{_pkgconfigdir}/*.pc
