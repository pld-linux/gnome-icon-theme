Summary:	Default icon themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy ikon dla środowiska GNOME
Name:		gnome-icon-theme
Version:	2.91.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	3b91f996a9c3559c8c03374e12b67dbc
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2 >= 2:2.14.0
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post):	gtk+2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
Default icon themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy ikon dla środowiska GNOME.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_iconsdir}/gnome
%{_pkgconfigdir}/gnome-icon-theme.pc
