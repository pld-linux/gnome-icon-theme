Summary:	Default icon themes for GNOME enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME
Name:		gnome-icon-theme
Version:	2.13.6
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	2edf79faf48511635fe697c0e51e1403
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.8.1
BuildRequires:	gtk+2 >= 2:2.8.0
BuildRequires:	icon-naming-utils >= 0.6.7
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
