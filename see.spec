%define name	see
%define version	2.1.1206
%define release %mkrel 3

%define major	1
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	JavaScript interpreter and runtime library
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}_snapshot.tar.bz2
URL:		http://www.adaptive-enterprises.com.au/~d/software/see/
License:	BSD
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgc-devel

%description
ECMAScript is a standardized language also known variously as JavaScript,
JScript, and LiveScript. SEE is a library that provides a parser and runtime
environment for this language. It conforms to ECMAScript Edition 3, and to
JavaScript 1.5, with some compatibility switches for earlier versions of
JavaScript and Microsoft's JScript.

SEE comes with a shell (see-shell) that allows javascript programs to be run
interactively, from plain or from HTML files.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %{name}-%{version}_snapshot

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO doc/*.html
%{_bindir}/see-shell

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%dir %{_libdir}/see
%{_libdir}/see/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_bindir}/libsee-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/see/*.so
%{_libdir}/*.a
%{_libdir}/see/*.a
%{_libdir}/*.la
%{_libdir}/see/*.la
