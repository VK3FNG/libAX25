Name:           libax25
Version:        0.0.12rc4
Release:        1
Summary:        AX.25 library for hamradio applications

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.linux-ax25.org/
Source0:        http://www.linux-ax25.org/pub/%{name}/%{name}-0.0.12-rc4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-0.0.12-rc4-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel

%description
libax25 is a library for ham radio applications that use the AX.25, NETROM
or ROSE protocols.  Included are routines to do ax25 address parsing, common
ax25 application config file parsing, etc. 

%package        devel

Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%setup -q -n %{name}-0.0.12-rc4

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*
%{_mandir}/man?/*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sat Jun 27 2009 Ralf Baechle <ralf@linux-mips.org>
- Initial version
