Summary:	Default icon themes for GNOME2 enviroment
Summary(pl):	Domy¶lne motywy ikon dla ¶rodowiska GNOME2
Name:		gnome-icon-theme
Version:	1.1.5
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	357695607adeefabf2b4079dcb5b1a62
Source1:	http://freedesktop.org/Software/icon-theme/releases/hicolor-icon-theme-0.2.tar.gz
# Source1-md5:	773d97c9a2360a72d4bf772fb45523ad
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
%setup -q -a1

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

install hicolor-icon-theme*/index.theme $RPM_BUILD_ROOT%{_datadir}/icons/hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/icons/*
%{_pkgconfigdir}/*.pc
