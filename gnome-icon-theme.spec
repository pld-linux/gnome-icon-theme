Summary:	Default icon themes for GNOME2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME2
Name:		gnome-icon-theme
Version:	1.0.9
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	f11da9541223537fc8f65a42a09fa49d
URL:		http://www.gnome.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for GNOME2 enviroment.

%description -l pl
Domy¶lne motywy ikon dla ¶rodowiska GNOME2.

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
%{_datadir}/icons/*
