Summary:	Default icon themes for GNOME2 enviroment
Summary(pl):	Domy�lne motywy ikon dla �rodowiska GNOME2
Name:		gnome-icon-theme
Version:	1.1.8
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	f4f1315dd01b4845fd7f7b9757b75d70
URL:		http://www.gnome.org/
BuildRequires:	intltool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.3.0
Requires:	hicolor-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for GNOME2 enviroment.

%description -l pl
Domy�lne motywy ikon dla �rodowiska GNOME2.

%prep
%setup -q

%build
glib-gettextize --force
intltoolize --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-hicolor-check

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/stock/*/*.png
%{_datadir}/icons/gnome
%{_pkgconfigdir}/*.pc
