Summary:	Utilities for mounting and managing CIFS mounts
Summary(pl.UTF-8):	Narzędzia do montowania i zarządzania montowaniami CIFS
Name:		cifs-utils
Version:	7.3
Release:	1
License:	GPL v3+
Group:		Daemons
Source0:	https://ftp.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	ed26a90c367cf2e958ff956bd8e8fc99
Patch0:		%{name}-heimdal.patch
Patch1:		python3.patch
URL:		https://wiki.samba.org/index.php/LinuxCIFS_utils
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docutils
BuildRequires:	heimdal-devel >= 1.5.1-3
BuildRequires:	keyutils-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libsmbclient-devel >= 1:4
BuildRequires:	libtalloc-devel
BuildRequires:	pam-devel
Requires:	keyutils
Obsoletes:	mount-cifs < 0.2
Conflicts:	samba-client < 1:3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SMB/CIFS protocol is a standard file sharing protocol widely
deployed on Microsoft Windows machines. This package contains tools
for mounting shares on Linux using the SMB/CIFS protocol. The tools in
this package work in conjunction with support in the kernel to allow
one to mount a SMB/CIFS share onto a client and use it as if it were a
standard Linux file system.

%description -l pl.UTF-8
Protokół SMB/CIFS to standardowy protokół współdzielenia plików
szeroko wykorzystywany na komputerach z systemem Microsoft Windows.
Ten pakiet zawiera narzędzia do montowania pod Linuksem udziałów
udostępnionych poprzez protokół SMB/CIFS. Narzędzia z tego pakietu
współpracując z obsługą w jądrze pozwalają na montowanie udziałów
SMB/CIFS na systemie klienckim tak, jakby był to standardowy
linuksowy system plików.

%package devel
Summary:	Header file for cifs-utils ID Mapping Plugin interface
Summary(pl.UTF-8):	Plik nagłówkowy interfejsu wtyczek ID Mapping cifs-utils
Group:		Development/Libraries
# doesn't require base

%description devel
Header file for cifs-utils ID Mapping Plugin interface.

%description devel -l pl.UTF-8
Plik nagłówkowy interfejsu wtyczek ID Mapping cifs-utils.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' \
	-e '1s,/usr/bin/env python3,%{__python3},' \
	smb2-quota \
	smb2-secdesc \
	checkopts \
	smbinfo

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-libcap-ng \
	--enable-cifsacl \
	--enable-cifsidmap \
	--enable-cifsupcall

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pamdir=/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) /sbin/mount.cifs
%attr(755,root,root) /sbin/mount.smb3
%attr(755,root,root) %{_bindir}/cifscreds
%attr(755,root,root) %{_bindir}/getcifsacl
%attr(755,root,root) %{_bindir}/setcifsacl
%attr(755,root,root) %{_bindir}/smb2-quota
%attr(755,root,root) %{_bindir}/smbinfo
%attr(755,root,root) %{_sbindir}/cifs.upcall
%attr(755,root,root) %{_sbindir}/cifs.idmap
%attr(755,root,root) /%{_lib}/security/pam_cifscreds.so
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/idmapwb.so
%{_mandir}/man1/cifscreds.1*
%{_mandir}/man1/getcifsacl.1*
%{_mandir}/man1/setcifsacl.1*
%{_mandir}/man1/smb2-quota.1*
%{_mandir}/man1/smbinfo.1*
%{_mandir}/man8/cifs.upcall.8*
%{_mandir}/man8/cifs.idmap.8*
%{_mandir}/man8/idmapwb.8*
%{_mandir}/man8/mount.cifs.8*
%{_mandir}/man8/mount.smb3.8*
%{_mandir}/man8/pam_cifscreds.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/cifsidmap.h
