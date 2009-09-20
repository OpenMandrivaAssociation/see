%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: 	 	see
Summary: 	JavaScript interpreter and runtime library
Version: 	3.0.1376
Release: 	%{mkrel 7}
Source0:	%{name}-%{version}.tar.gz
Patch0:		see-3.0.1376-underlink.patch
# Build the library with -fPIC (needed by tkhtml3) - AdamW 2008/12
Patch1:		see-3.0.1376-fpic.patch
# During 'temporary' move: http://125.168.50.158/~d/software/see/
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

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel < %{version}-%{release}
Obsoletes:	%{mklibname see 1 -d}

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
%patch0 -p1 -b .underlink
%patch1 -p1 -b .fpic

%build
autoreconf
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

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/libsee-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}/*.so
%{_libdir}/*.a
%{_libdir}/%{name}/*.a
%{_libdir}/*.la
%{_libdir}/%{name}/*.la
%{_libdir}/pkgconfig/%{name}.pc
