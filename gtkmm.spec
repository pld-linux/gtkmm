Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl):	Wrapper C++ dla GTK
Name:		Gtk--
Version:	1.0.3
Release:	1
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	LGPL
Vendor:		PLD
Source:		http://lazy.ton.tut.fi/gtk--/Gtk---%{version}.tar.gz
URL:		http://lazy.ton.tut.fi/terop/iki/gtk/gtk--.html
Requires:	cpp
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	/usr/share

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++ programmers
to create GUIs with GTK+'s flexible object-oriented framework. Features
include type safe callbacks, widgets that are extensible using inheritance
and over 110 classes that can be freely combined to quickly create complex
user interfaces.

%description -l pl
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK jest bibliotek± s³u¿±c±
do tworzenia graficznych interfejsów. W pakiecie znajduje siê tak¿e
biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

%package gnome
Summary:	GTK-- GNOME library
Summary(pl):	Biblioteka GTK-- z wsparciem do GNOME
Group:		X11/GNOME/Libraries
Group(pl):	X11/GNOME/Biblioteki
Requires:	%{name} = %{version}

%description gnome
GTK-- GNOME library.

%description -l pl gnome
Biblioteka GTK-- z wsparciem do GNOME.

%package devel
Summary:	GTK-- and GDK-- header files, development documentation
Summary(pl):	Pliki nag³ówkowe GTK-- i GDK--, dokumentacja dla programistów
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-gnome = %{version}

%description devel
Header files and development documentation for GTK-- library.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla programistów do biblioteki GTK--.

%package static
Summary:	GTK-- and GDK-- static libraries
Summary(pl):	Biblioteki statyczne GTK-- i GDK--
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GTK-- and GDK-- static libraries.

%description -l pl static
Biblioteki statyczne GTK-- i GDK--.

%prep
%setup -q

%build
autoconf

LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
export LDFLAGS CXXFLAGS
%configure \
	--prefix=/usr/X11R6 \
	--enable-static=yes \
	--oldincludedir=/usr/X11R6/include
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

cp -dpr examples $RPM_BUILD_ROOT/usr/src/examples/%{name}

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README ChangeLog AUTHORS NEWS

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_libdir}/libgdkmm*.so.*.*
%attr(755,root,root) %{_libdir}/libgtkmm*.so.*.*

%files gnome
%attr(755,root,root) %{_libdir}/libgnomemm.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/*
%doc /usr/src/examples/%{name}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.sh

%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/Gtk--
%{_datadir}/aclocal/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
