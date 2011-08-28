Summary: A library which allows userspace access to USB devices
Name: libusb1
Version: 1.0.3
Release: 1%{?dist}
Source0: http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
License: LGPLv2+
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://libusb.wiki.sourceforge.net/Libusb1.0
ExcludeArch: s390 s390x
BuildRequires: doxygen

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package devel
Summary: Development files for libusb
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb1.

%package static
Summary: Static development files for libusb
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries to develop applications that use libusb1.

%prep
%setup -q -n libusb-%{version}

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS"
pushd doc
make docs
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc doc/html examples/*.c
%{_libdir}/pkgconfig/libusb-1.0.pc
%{_includedir}/*
%{_libdir}/*.so

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%changelog
* Mon Sep 28 2009 Jindrich Novy <jnovy@redhat.com> 1.0.3-1
- update to 1.0.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Jindrich Novy <jnovy@redhat.com> 1.0.2-1
- update to 1.0.2

* Wed May 13 2009 Jindrich Novy <jnovy@redhat.com> 1.0.1-1
- update to 1.0.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 - Bastien Nocera <bnocera@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Nov 21 2008 - Bastien Nocera <bnocera@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Tue Sep 23 2008 Jindrich Novy <jnovy@redhat.com> 0.9.3-0.1
- update to 0.9.3

* Sun Jul 06 2008 - Bastien Nocera <bnocera@redhat.com> - 0.9.1
- Update to 0.9.1

* Mon May 26 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.4
- update to official beta

* Thu May 23 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.3.gitbef33bb
- update comment on how the tarball was created
- use abbreviated git hash within package name to avoid conflicts
- add to %%description that libusb1 is incompatible with libsub-0.1

* Thu May 22 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.2.gitbef33bb
- add info on how the snapshot tarball was created

* Wed May 21 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.1.gitbef33bb
- use proper version to denote it is a git snapshot

* Thu May 15 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.1
- initial packaging
