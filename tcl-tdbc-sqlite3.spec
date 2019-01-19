Summary:	TDBC driver to access SQLite 3 databases
Summary(pl.UTF-8):	Sterownik TDBC służący do dostępu do baz danych SQLite 3
Name:		tcl-tdbc-sqlite3
Version:	1.1.0
Release:	1
License:	Tcl (BSD-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tcl/tdbcsqlite3-%{version}.tar.gz
# Source0-md5:	a5469cba079949c77b7ca004f8c68d56
URL:		http://tdbc.tcl.tk/
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	tcl-tdbc-devel >= %{version}
Requires:	tcl >= 8.6
Requires:	tcl-sqlite3
Requires:	tcl-tdbc >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl TDBC SQLite 3 module is the driver for Tcl Database Connectivity
(TDBC) to access SQLite 3 databases.

%description -l pl.UTF-8
Moduł Tcl TDBC SQLite 3 to sterownik szkieletu Tcl Database
Connectivity (TDBC) służący do dostępu do baz danych SQLite 3.

%prep
%setup -q -n tdbcsqlite3-%{version}

%build
%configure \
	--libdir=%{_prefix}/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.terms
%dir %{_prefix}/lib/tcl8/8.*/tdbc
%attr(755,root,root) %{_prefix}/lib/tcl8/8.*/tdbc/sqlite3-%{version}.tm
%{_mandir}/mann/tdbc_sqlite3.n*
