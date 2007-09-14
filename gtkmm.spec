# TODO
# - think of eliminating cpp runtime dep, as cpp pulls gcc
#
# Conditional build:
%bcond_without	examples	# don't build examples
%bcond_without	static_libs	# don't build static libraries
#
%include	/usr/lib/rpm/macros.perl
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl.UTF-8):	Wrapper C++ dla GTK+
Name:		gtkmm
Version:	2.12.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	b7a6adb1c9c7e1b6464b4240a4b7ba19
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	atk-devel >= 1:1.19.6
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairomm-devel >= 1.4.4
BuildRequires:	glibmm-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	pango-devel >= 1:1.18.1
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	%{name}-atk = %{version}-%{release}
Requires:	%{name}-pango = %{version}-%{release}
Requires:	cairomm >= 1.4.4
Requires:	cpp
Requires:	gtk+2 >= 2:2.12.0
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
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest biblioteką
służącą do tworzenia graficznych interfejsów. W pakiecie znajduje się
także biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

%package devel
Summary:	GTK-- and GDK-- header files, development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe GTK-- i GDK--, dokumentacja dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-atk-devel = %{version}-%{release}
Requires:	%{name}-pango-devel = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0

%description devel
Header files and development documentation for GTK-- library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla programistów do biblioteki GTK--.

%package doc
Summary:	Reference documentation and examples for GTK-- and GDK--
Summary(pl.UTF-8):	Szczegółowa dokumentacja i przykłady dla GTK-- i GDK--
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation and examples for GTK-- and GDK--.

%description doc -l pl.UTF-8
Szczegółowa dokumentacja i przykłady dla GTK-- i GDK--.

%package static
Summary:	GTK-- and GDK-- static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GTK-- i GDK--
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GTK-- and GDK-- static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GTK-- i GDK--.

%package atk
Summary:	A C++ interface for atk library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk
Group:		X11/Development/Libraries
Requires:	atk >= 1:1.19.6
Requires:	glibmm >= 2.14.0

%description atk
A C++ interface for atk library.

%description atk -l pl.UTF-8
Interfejs C++ dla biblioteki atk.

%package atk-devel
Summary:	A C++ interface for atk library - header files
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-atk = %{version}-%{release}
Requires:	atk-devel >= 1:1.19.6
Requires:	glibmm-devel >= 2.14.0

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

%package pango
Summary:	A C++ interface for pango library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango
Group:		X11/Development/Libraries
Requires:	cairomm >= 1.4.4
Requires:	glibmm >= 2.14.0
Requires:	pango >= 1:1.18.1

%description pango
A C++ interface for pango library.

%description pango -l pl.UTF-8
Interfejs C++ dla biblioteki pango.

%package pango-devel
Summary:	A C++ interface for pango library - header files
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-pango = %{version}-%{release}
Requires:	cairomm-devel >= 1.4.4
Requires:	glibmm-devel >= 2.14.0
Requires:	pango-devel >= 1:1.18.1

%description pango-devel
A C++ interface for pango library - header files.

%description pango-devel -l pl.UTF-8
Interfejs C++ dla biblioteki pango - pliki nagłówkowe.

%package pango-static
Summary:	A C++ interface for pango library - static version
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-pango-devel = %{version}-%{release}

%description pango-static
A C++ interface for pango library - static version.

%description pango-static -l pl.UTF-8
Interfejs C++ dla biblioteki pango - wersja statyczna.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
# exceptions and rtti are used in this package --misiek
%configure \
	--disable-demos \
	%{!?with_examples:--disable-examples} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

mv -f $RPM_BUILD_ROOT%{_docdir}/gtkmm-2.4/{examples,tests} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	atk -p /sbin/ldconfig
%postun	atk -p /sbin/ldconfig

%post	pango -p /sbin/ldconfig
%postun	pango -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES NEWS PORTING README
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so
%{_libdir}/libg[dt]kmm*.la
%{_libdir}/g[dt]kmm-2.4
%{_includedir}/g[dt]kmm-2.4
%{_pkgconfigdir}/g[dt]kmm*.pc

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/gtkmm-2.4
%{?with_examples:%{_examplesdir}/%{name}-%{version}}
%doc %{_datadir}/devhelp/books/gtkmm-2.4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libg[dt]kmm*.a
%endif

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so.*.*

%files atk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so
%{_libdir}/libatkmm*.la
%{_pkgconfigdir}/atkmm*.pc
%{_includedir}/atkmm-1.6

%if %{with static_libs}
%files atk-static
%defattr(644,root,root,755)
%{_libdir}/libatkmm*.a
%endif

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so.*.*

%files pango-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so
%{_libdir}/libpangomm*.la
%{_pkgconfigdir}/pangomm*.pc
%{_includedir}/pangomm-1.4

%if %{with static_libs}
%files pango-static
%defattr(644,root,root,755)
%{_libdir}/libpangomm*.a
%endif
