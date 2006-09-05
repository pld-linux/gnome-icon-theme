Summary:	Default icon themes for GNOME enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME
Name:		gnome-icon-theme
Version:	2.16.0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	79acaaccddd5c3ffceb92c613a3e9729
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2:2.10.3
BuildRequires:	icon-naming-utils >= 0.8.1
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
