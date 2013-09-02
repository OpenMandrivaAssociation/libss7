%define	major 1
%define libname %mklibname ss7 _%{major}
%define develname %mklibname ss7 -d

Summary:	Provides SS7 protocol services to applications
Name:		libss7
Version:	1.0.2
Release:	4
License:	GPL
Group:		System/Libraries
URL:		http://www.asterisk.org/
Source0:	http://ftp.digium.com/pub/libss7/%{name}-%{version}.tar.gz

%description
libss7 is a userspace library that is used for providing SS7 protocol services
to applications.  It has a working MTP2, MTP3, and ISUP for ITU and ANSI style
SS7, however it was written in a manner that will easily allow support for
other various national specific variants in the future.  For a working
reference implementation, see the various link test programs, as well as the
Asterisk Open Source PBX.

%package -n	%{libname}
Summary:	Provides SS7 protocol services to applications
Group:          System/Libraries

%description -n	%{libname}
libss7 is a userspace library that is used for providing SS7 protocol services
to applications.  It has a working MTP2, MTP3, and ISUP for ITU and ANSI style
SS7, however it was written in a manner that will easily allow support for
other various national specific variants in the future.  For a working
reference implementation, see the various link test programs, as well as the
Asterisk Open Source PBX.

%package -n	%{develname}
Summary:	Development libraries and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	ss7-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
libss7 is a userspace library that is used for providing SS7 protocol services
to applications.  It has a working MTP2, MTP3, and ISUP for ITU and ANSI style
SS7, however it was written in a manner that will easily allow support for
other various national specific variants in the future.  For a working
reference implementation, see the various link test programs, as well as the
Asterisk Open Source PBX.

This package contains all of the development files that you will need in order
to compile %{name} applications.

%prep

%setup -q

# lib64 fix
find -name "Makefile" | xargs perl -pi -e 's|\$\(INSTALL_BASE\)/lib|\$\(INSTALL_BASE\)/%{_lib}|g'

%build

%make CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT"

%install
make \
    INSTALL_PREFIX="%{buildroot}" \
    install

%files -n %{libname}
%doc ChangeLog README NEWS*
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
