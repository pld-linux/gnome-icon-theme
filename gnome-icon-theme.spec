Summary:	Default icon themes for GNOME2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME2
Name:		gnome-icon-theme
Version:	2.12.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	14d1ce7cdb1f23278bb9967900287183
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.3
BuildRequires:	intltool
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for GNOME2 enviroment.

%description -l pl
Domy¶lne motywy ikon dla ¶rodowiska GNOME2.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
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
%doc ChangeLog NEWS
%{_iconsdir}/gnome
%{_iconsdir}/hicolor/*/*/*.*
%{_iconsdir}/hicolor/*/stock/*/*.png
%{_pkgconfigdir}/*.pc
