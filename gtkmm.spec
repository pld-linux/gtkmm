%include        /usr/lib/rpm/macros.perl
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl):	Wrapper C++ dla GTK
Name:		gtkmm
Version:	1.3.26
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://prdownloads.sourceforge.net/gtkmm/gtkmm-%{version}.tar.gz
URL:		http://gtkmm.sourceforge.net/
Requires:	cpp
BuildRequires:	esound-devel
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRequires:	perl
BuildRequires:	autoconf
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Gtk--


%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%description -l pl
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK jest bibliotek±
s³u¿±c± do tworzenia graficznych interfejsów. W pakiecie znajduje siê
tak¿e biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

%package devel
Summary:	GTK-- and GDK-- header files, development documentation
Summary(pl):	Pliki nag³ówkowe GTK-- i GDK--, dokumentacja dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.0.6
Requires:	libsigc++-devel >= 1.2.1

%description devel
Header files and development documentation for GTK-- library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla programistów do biblioteki GTK--.

%package static
Summary:	GTK-- and GDK-- static libraries
Summary(pl):	Biblioteki statyczne GTK-- i GDK--
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GTK-- and GDK-- static libraries.

%description static -l pl
Biblioteki statyczne GTK-- i GDK--.

%prep
%setup -q -n gtkmm-%{version}

%build
# exceptions and rtti are used in this package --misiek
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

cp -dpr examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%dir %{_libdir}/gtkmm-*
%{_libdir}/gtkmm-*/include
%dir %{_libdir}/gtkmm-*/proc
%{_libdir}/gtkmm-*/proc/m4
%{_libdir}/gtkmm-*/proc/pm
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/gtkmmproc
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/*.pl

%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
