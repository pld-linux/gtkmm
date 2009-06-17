#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl.UTF-8):	Wrapper C++ dla GTK+
Name:		gtkmm
Version:	2.16.0
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	a82e3b5b93008421ff67df16d1e51ec2
URL:		http://www.gtkmm.org/
BuildRequires:	atk-devel >= 1:1.24.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairomm-devel >= 1.6.3
BuildRequires:	glibmm-devel >= 2.18.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	pangomm-devel >= 2.14.0
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
Requires:	%{name}-atk = %{version}-%{release}
Requires:	cairomm >= 1.6.3
Requires:	glibmm >= 2.18.0
Requires:	gtk+2 >= 2:2.16.0
Requires:	pangomm >= 2.14.0
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
Requires:	%{name}-atk-devel = %{version}-%{release}
Requires:	glibmm-devel >= 2.18.0
Requires:	gtk+2-devel >= 2:2.16.0
Requires:	pangomm-devel >= 2.14.0

%description devel
Header files for gtkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkmm.

%package doc
Summary:	Reference documentation for gtkmm and gdkmm
Summary(pl.UTF-8):	Szczegółowa dokumentacja gtkmm i gdkmm
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation for gtkmm and gdkmm.

%description doc -l pl.UTF-8
Szczegółowa dokumentacja gtkmm i gdkmm.

%package static
Summary:	gtkmm and gdkmm static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtkmm i gdkmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gtkmm and gdkmm static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtkmm i gdkmm.

%package atk
Summary:	A C++ interface for atk library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk
Group:		X11/Libraries
Requires:	atk >= 1:1.24.0
Requires:	glibmm >= 2.18.0

%description atk
A C++ interface for atk library.

%description atk -l pl.UTF-8
Interfejs C++ dla biblioteki atk.

%package atk-devel
Summary:	A C++ interface for atk library - header files
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-atk = %{version}-%{release}
Requires:	atk-devel >= 1:1.24.0
Requires:	glibmm-devel >= 2.18.0

%description atk-devel
A C++ interface for atk library - header files.

%description atk-devel -l pl.UTF-8
Interfejs C++ dla biblioteki atk - pliki nagłówkowe.

%package atk-static
Summary:	A C++ interface for atk library - static version
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-atk-devel = %{version}-%{release}

%description atk-static
A C++ interface for atk library - static version.

%description atk-static -l pl.UTF-8
Interfejs C++ dla biblioteki atk - wersja statyczna.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--disable-demos \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	atk -p /sbin/ldconfig
%postun	atk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES NEWS PORTING README
%attr(755,root,root) %{_libdir}/libgdkmm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdkmm-2.4.so.1
%attr(755,root,root) %{_libdir}/libgtkmm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmm-2.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkmm-2.4.so
%attr(755,root,root) %{_libdir}/libgtkmm-2.4.so
%{_libdir}/libgdkmm-2.4.la
%{_libdir}/libgtkmm-2.4.la
%{_libdir}/gdkmm-2.4
%{_libdir}/gtkmm-2.4
%{_includedir}/gdkmm-2.4
%{_includedir}/gtkmm-2.4
%{_pkgconfigdir}/gdkmm-2.4.pc
%{_pkgconfigdir}/gtkmm-2.4.pc

%files doc
%defattr(644,root,root,755)
%{_docdir}/gtkmm-2.4
%{_datadir}/devhelp/books/gtkmm-2.4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkmm-2.4.a
%{_libdir}/libgtkmm-2.4.a
%endif

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatkmm-1.6.so.1

%files atk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm-1.6.so
%{_libdir}/libatkmm-1.6.la
%{_pkgconfigdir}/atkmm-1.6.pc
%{_includedir}/atkmm-1.6

%if %{with static_libs}
%files atk-static
%defattr(644,root,root,755)
%{_libdir}/libatkmm-1.6.a
%endif
