Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl):	Wrapper C++ dla GTK
Name:		gtkmm
Version:	1.2.5
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gtkmm/%{name}-%{version}.tar.gz
URL:		http://gtkmm.sourceforge.net/
Requires:	cpp
BuildRequires:	esound-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	libsigc++-devel >= 0.8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Gtk--

%define		_prefix		/usr/X11R6

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
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	gtk+-devel
Requires:	libstdc++-devel
Requires:	libsigc++-devel
Obsoletes:	Gtk---devel

%description devel
Header files and development documentation for GTK-- library.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla programistów do biblioteki GTK--.

%package static
Summary:	GTK-- and GDK-- static libraries
Summary(pl):	Biblioteki statyczne GTK-- i GDK--
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	Gtk---static

%description static
GTK-- and GDK-- static libraries.

%description -l pl static
Biblioteki statyczne GTK-- i GDK--.

%prep
%setup -q

%build
autoconf
CXXFLAGS="%{rpmcflags} -fno-exceptions"
%configure \
	--enable-static=yes \
	%{?_without_gnome:--without-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

cp -dpr examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9nf README ChangeLog AUTHORS NEWS

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkmm*.so.*.*
%attr(755,root,root) %{_libdir}/libgtkmm*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz 
%doc /usr/src/examples/%{name}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/*

%{_includedir}/*

%dir %{_libdir}/gtkmm
%{_libdir}/gtkmm/include
%dir %{_libdir}/gtkmm/proc
%{_libdir}/gtkmm/proc/*.m4
%attr(755,root,root) %{_libdir}/gtkmm/proc/gtkmmproc

%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
