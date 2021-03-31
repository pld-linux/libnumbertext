Summary:	Number to number name and money text conversion library
Summary(pl.UTF-8):	Biblioteka do konwersji liczb i pieniędzy na tekst
Name:		libnumbertext
Version:	1.0.7
Release:	1
License:	BSD or LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/Numbertext/libnumbertext/releases
Source0:	https://github.com/Numbertext/libnumbertext/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	f5ae7ef8f0f49b28bac8cb93311153fc
URL:		https://numbertext.github.io/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel >= 6:4.9
BuildRequires:	libtool >= 2:1.5
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number to number name and money text conversion libraries in C++,
Java, JavaScript and Python & LibreOffice Calc Extension.

%description -l pl.UTF-8
Biblioteka C++ do konwersji liczb i pieniędzy na tekst dla C++,
Javy, JavaScriptu i Pythona oraz rozszerzenia LibreOffice Calc.

%package devel
Summary:	Header files for libnumbertext
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnumbertext
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.9

%description devel
This package contains the header files for developing applications
that use libnumbertext.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libnumbertext.

%package static
Summary:	Static libnumbertext library
Summary(pl.UTF-8):	Statyczna biblioteka libnumbertext
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnumbertext library.

%description static -l pl.UTF-8
Statyczna biblioteka libnumbertext.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnumbertext-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md THANKS
%attr(755,root,root) %{_bindir}/spellout
%attr(755,root,root) %{_libdir}/libnumbertext-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnumbertext-1.0.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnumbertext-1.0.so
%{_includedir}/libnumbertext
%{_pkgconfigdir}/libnumbertext.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnumbertext-1.0.a
