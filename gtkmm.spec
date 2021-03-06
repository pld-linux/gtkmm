#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl.UTF-8):	Wrapper C++ dla GTK+
Name:		gtkmm
Version:	2.24.5
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.24/%{name}-%{version}.tar.xz
# Source0-md5:	6c59ae8bbff48fad9132f23af347acf1
URL:		http://www.gtkmm.org/
BuildRequires:	atkmm-devel >= 2.22.2
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairomm-devel >= 1.6.3
BuildRequires:	glibmm-devel >= 2.28.0
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	mm-common >= 0.9.8
BuildRequires:	pangomm-devel >= 2.28.0
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	atkmm >= 2.22.2
Requires:	cairomm >= 1.6.3
Requires:	glibmm >= 2.28.0
Requires:	gtk+2 >= 2:2.24.0
Requires:	pangomm >= 2.28.0
Obsoletes:	Gtk--
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%description -l pl.UTF-8
gtkmm jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest biblioteką
służącą do tworzenia graficznych interfejsów. W pakiecie znajduje się
także biblioteka gdkmm - wrapper C++ dla GDK (General Drawing Kit).

%package devel
Summary:	gtkmm and gdkmm header files
Summary(pl.UTF-8):	Pliki nagłówkowe gtkmm i gdkmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atkmm-devel >= 2.22.2
Requires:	glibmm-devel >= 2.28.0
Requires:	gtk+2-devel >= 2:2.24.0
Requires:	pangomm-devel >= 2.28.0

%description devel
Header files for gtkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkmm.

%package static
Summary:	gtkmm and gdkmm static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtkmm i gdkmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gtkmm and gdkmm static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtkmm i gdkmm.

%package apidocs
Summary:	Reference documentation for gtkmm and gdkmm
Summary(pl.UTF-8):	Szczegółowa dokumentacja gtkmm i gdkmm
Group:		Documentation
Requires:	devhelp
Obsoletes:	gtkmm-doc
BuildArch:	noarch

%description apidocs
Reference documentation for gtkmm and gdkmm.

%description apidocs -l pl.UTF-8
Szczegółowa dokumentacja gtkmm i gdkmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING README
%attr(755,root,root) %{_libdir}/libgdkmm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdkmm-2.4.so.1
%attr(755,root,root) %{_libdir}/libgtkmm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmm-2.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkmm-2.4.so
%attr(755,root,root) %{_libdir}/libgtkmm-2.4.so
%{_libdir}/gdkmm-2.4
%{_libdir}/gtkmm-2.4
%{_includedir}/gdkmm-2.4
%{_includedir}/gtkmm-2.4
%{_pkgconfigdir}/gdkmm-2.4.pc
%{_pkgconfigdir}/gtkmm-2.4.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkmm-2.4.a
%{_libdir}/libgtkmm-2.4.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gtkmm-2.4
%{_datadir}/devhelp/books/gtkmm-2.4
