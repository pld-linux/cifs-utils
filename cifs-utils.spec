Summary:	Utilities for mounting and managing CIFS mounts
Summary(pl.UTF-8):	Narzędzia do montowania i zarządzania montowaniami CIFS
Name:		cifs-utils
Version:	5.9
Release:	1
License:	GPL v3+
Group:		Daemons
Source0:	ftp://ftp.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	7164ad6f7963a31fcbffbe4f14a7cfc6
Patch0:		%{name}-heimdal.patch
URL:		http://linux-cifs.samba.org/cifs-utils/
BuildRequires:	heimdal-devel >= 1.5.1-3
BuildRequires:	keyutils-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtalloc-devel
Requires:	keyutils
Obsoletes:	mount-cifs
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

%prep
%setup -q
%patch0 -p1

%build
%configure \
	WBCLIENT_CFLAGS=" " \
	WBCLIENT_LIBS="-lwbclient" \
	--with-libcap-ng=yes \
	--enable-cifsupcall \
	--enable-cifsidmap \
	--enable-cifsacl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) /sbin/mount.cifs
%attr(755,root,root) %{_bindir}/cifscreds
%attr(755,root,root) %{_bindir}/getcifsacl
%attr(755,root,root) %{_bindir}/setcifsacl
%attr(755,root,root) %{_sbindir}/cifs.upcall
%attr(755,root,root) %{_sbindir}/cifs.idmap
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/idmapwb.so
%{_mandir}/man1/cifscreds.1*
%{_mandir}/man1/getcifsacl.1*
%{_mandir}/man1/setcifsacl.1*
%{_mandir}/man8/cifs.upcall.8*
%{_mandir}/man8/cifs.idmap.8*
%{_mandir}/man8/idmapwb.8*
%{_mandir}/man8/mount.cifs.8*
