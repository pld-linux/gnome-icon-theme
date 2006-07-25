Summary:	Default icon themes for GNOME enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME
Name:		gnome-icon-theme
Version:	2.15.90
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	e2d9221450d2f4ac3d77d353b5e0df7a
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2 >= 2:2.10.1
BuildRequires:	icon-naming-utils >= 0.7.4
BuildRequires:	intltool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default icon themes for GNOME enviroment.

%description -l pl
Domy¶lne motywy ikon dla ¶rodowiska GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir='%{_pkgconfigdir}'

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%{_iconsdir}/gnome
%{_pkgconfigdir}/*.pc
