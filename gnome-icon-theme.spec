Summary:	Default icon themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy ikon dla środowiska GNOME
Name:		gnome-icon-theme
Version:	2.20.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	56857a6d5f26c236b48fcf6760549d1b
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2:2.12.0
BuildRequires:	icon-naming-utils >= 0.8.2
BuildRequires:	intltool >= 0.35.5
BuildRequires:	pkgconfig >= 1:0.19
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

# add missing icon dirs, fixes broken directory deps
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/22x22/{filesystems,stock/{chart,code,data,document,emoticons,form,generic,image,io,media,navigation,net,object,table,text}}
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/24x24/stock/emoticons
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/32x32/{filesystems,stock/{chart,code,data,document,emoticons,form,image,io,media,navigation,net,object,table,text}}
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/48x48/{categories,emotes,mimetypes,places,status,stock/{chart,emoticons,form,image,media,navigation,object,table,text}}
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/scalable/{animations,filesystems,stock/{chart,code,data,document,emoticons,form,image,io,media,navigation,net,object,table,text}}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%{_iconsdir}/gnome
%{_pkgconfigdir}/*.pc
