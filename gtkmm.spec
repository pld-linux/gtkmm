%include        /usr/lib/rpm/macros.perl
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl):	Wrapper C++ dla GTK+
Name:		gtkmm
Version:	2.2.4
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.2/gtkmm-%{version}.tar.bz2
# Source0-md5:	d760843722771b0401a37465d69efd76
Patch0:		%{name}-link.patch
Patch1:		%{name}-gcc33.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	atk-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	glib2-devel >= 2.2.1
BuildRequires:	gtk+2-devel >= 2.2.1
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.1
BuildRequires:	perl >= 5.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	zlib-devel
Requires:	%{name}-glib = %{version}
Requires:	%{name}-pango = %{version}
Requires:	%{name}-atk = %{version}
Requires:	cpp
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
Requires:	%{name}-glib-devel = %{version}
Requires:	%{name}-pango-devel = %{version}
Requires:	%{name}-atk-devel = %{version}
Requires:	gtk+2-devel >= 2.2.1
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

%package atk
Summary:	A C++ interface for atk library
Summary(pl):	Interfejs C++ dla biblioteki atk
Group:		X11/Development/Libraries
Requires:	%{name}-glib = %{version}

%description atk
A C++ interface for atk library.

%description atk -l pl
Interfejs C++ dla biblioteki atk.

%package atk-devel
Summary:	A C++ interface for atk library - header files
Summary(pl):	Interfejs C++ dla biblioteki atk - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-atk = %{version}
Requires:	%{name}-glib-devel = %{version}
Requires:	atk-devel >= 1.2.0

%description atk-devel
A C++ interface for atk library - header files.

%description atk-devel -l pl
Interfejs C++ dla biblioteki atk - pliki nag³ówkowe.

%package atk-static
Summary:	A C++ interface for atk library - static version
Summary(pl):	Interfejs C++ dla biblioteki atk - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-atk-devel = %{version}

%description atk-static
A C++ interface for atk library - static version.

%description atk-static -l pl
Interfejs C++ dla biblioteki atk - wersja statyczna.

%package glib
Summary:	A C++ interface for glib library
Summary(pl):	Interfejs C++ dla biblioteki glib
Group:		X11/Development/Libraries

%description glib
A C++ interface for glib library.

%description glib -l pl
Interfejs C++ dla biblioteki glib.

%package glib-devel
Summary:	A C++ interface for glib library - header files
Summary(pl):	Interfejs C++ dla biblioteki glib - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-glib-devel = %{version}
Requires:	glib2-devel >= 2.2.1
Requires:	libsigc++-devel >= 1.2.1

%description glib-devel
A C++ interface for glib library - header files.

%description glib-devel -l pl
Interfejs C++ dla biblioteki glib - pliki nag³ówkowe.

%package glib-static
Summary:	A C++ interface for glib library - static version
Summary(pl):	Interfejs C++ dla biblioteki glib - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-glib-devel = %{version}

%description glib-static
A C++ interface for glib library - static version.

%description glib-static -l pl
Interfejs C++ dla biblioteki glib - wersja statyczna.

%package pango
Summary:	A C++ interface for pango library
Summary(pl):	Interfejs C++ dla biblioteki pango
Group:		X11/Development/Libraries
Requires:	%{name}-glib = %{version}

%description pango
A C++ interface for pango library.

%description pango -l pl
Interfejs C++ dla biblioteki pango.

%package pango-devel
Summary:	A C++ interface for pango library - header files
Summary(pl):	Interfejs C++ dla biblioteki pango - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-pango = %{version}
Requires:	%{name}-glib-devel = %{version}
Requires:	pango-devel >= 1.2.1

%description pango-devel
A C++ interface for pango library - header files.

%description pango-devel -l pl
Interfejs C++ dla biblioteki pango - pliki nag³ówkowe.

%package pango-static
Summary:	A C++ interface for pango library - static version
Summary(pl):	Interfejs C++ dla biblioteki pango - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-pango-devel = %{version}

%description pango-static
A C++ interface for pango library - static version.

%description pango-static -l pl
Interfejs C++ dla biblioteki pango - wersja statyczna.

%prep
%setup -q -n gtkmm-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
# exceptions and rtti are used in this package --misiek
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

mv -f $RPM_BUILD_ROOT%{_docdir}/gtkmm-2.0/docs installed-docs
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv -f $RPM_BUILD_ROOT%{_docdir}/gtkmm-2.0/examples/* \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n %{name}-atk -p /sbin/ldconfig
%postun	-n %{name}-atk -p /sbin/ldconfig

%post	-n %{name}-glib -p /sbin/ldconfig
%postun	-n %{name}-glib -p /sbin/ldconfig

%post	-n %{name}-pango -p /sbin/ldconfig
%postun	-n %{name}-pango -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc installed-docs/*
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so
%{_libdir}/libg[dt]kmm*.la

%{_libdir}/gtkmm-*/include/g[dt]kmm*
%dir %{_libdir}/gtkmm-2.0/proc
%{_libdir}/gtkmm-*/proc/m4
%{_libdir}/gtkmm-*/proc/pm
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/gtkmmproc
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/*.pl

%{_includedir}/gtkmm-2.0/g[dt]kmm*
%{_pkgconfigdir}/g[dt]kmm*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libg[dt]kmm*.a

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so.*.*

%files atk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so
%{_libdir}/libatkmm*.la
%{_pkgconfigdir}/atkmm*.pc
%{_includedir}/gtkmm-2.0/atkmm*

%files atk-static
%defattr(644,root,root,755)
%{_libdir}/libatkmm*.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibmm*.so.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibmm*.so
%{_libdir}/libglibmm*.la

%dir %{_libdir}/gtkmm-2.0
%dir %{_libdir}/gtkmm-2.0/include
%{_libdir}/gtkmm-*/include/glibmm*

%dir %{_includedir}/gtkmm-2.0
%{_includedir}/gtkmm-2.0/glibmm*
%{_pkgconfigdir}/glibmm*.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libglibmm*.a

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so.*.*

%files pango-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so
%{_libdir}/libpangomm*.la
%{_pkgconfigdir}/pangomm*.pc
%{_includedir}/gtkmm-2.0/pangomm*

%files pango-static
%defattr(644,root,root,755)
%{_libdir}/libpangomm*.a
