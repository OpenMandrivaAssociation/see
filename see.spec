%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: 	 	see
Summary: 	JavaScript interpreter and runtime library
Version: 	3.1.1424
Release: 	5
Source0:	%{name}-%{version}.tar.gz
Patch0:		see-3.1.1424-underlink.patch
# Build the library with -fPIC (needed by tkhtml3) - AdamW 2008/12
Patch1:		see-3.1.1424-fpic.patch
# During 'temporary' move: http://125.168.50.158/~d/software/see/
URL:		http://www.adaptive-enterprises.com.au/~d/software/see/
License:	BSD
Group:		Development/Other
BuildRequires:	pkgconfig(bdw-gc)

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
export CFLAGS="%optflags -DPIC -fPIC"
%configure2_5x
%make
										
%install
%makeinstall_std

%files
%doc AUTHORS COPYING README NEWS TODO doc/*.html
%{_bindir}/see-shell

%files -n %{libname}
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
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 3.1.1424-4mdv2011.0
+ Revision: 640460
- rebuild to obsolete old packages

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.1.1424-3
+ Revision: 634760
- really enable fPIC

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.1.1424-2
+ Revision: 634731
- rebuild

* Sat Jan 16 2010 Jérôme Brenier <incubusss@mandriva.org> 3.1.1424-1mdv2011.0
+ Revision: 492454
- new version 3.1.1424
- redo Patch0 and Patch1 not to have to autoreconf
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 3.0.1376-6mdv2009.1
+ Revision: 310349
- build the lib with -fPIC (or else tkhtml3 can't build)

* Mon Dec 01 2008 Adam Williamson <awilliamson@mandriva.org> 3.0.1376-5mdv2009.1
+ Revision: 308734
- add underlink.patch (fix underlinking)
- correct upstream URLs etc
- new release 3.0.1376
- clean spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri May 04 2007 Austin Acton <austin@mandriva.org> 2.1.1206-1mdv2008.0
+ Revision: 22172
- Import see

