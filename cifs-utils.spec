Summary:	Utilities for mounting and managing CIFS mounts
Name:		cifs-utils
Version:	5.2
Release:	1
License:	GPL v3
Group:		Daemons
URL:		http://linux-cifs.samba.org/cifs-utils/
Source0:	ftp://ftp.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	2ca839553cccd0c3042f7dd8737cc9de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	heimdal-devel >= 1.5.1-3
BuildRequires:	keyutils-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libtalloc-devel
BuildRequires:	samba-devel
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

%prep
%setup -q

%build
%configure \
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
%attr(755,root,root) /sbin/mount.cifs
%attr(755,root,root) %{_bindir}/getcifsacl
%attr(755,root,root) %{_bindir}/setcifsacl
%attr(755,root,root) %{_sbindir}/cifs.upcall
%attr(755,root,root) %{_sbindir}/cifs.idmap
%{_mandir}/man1/getcifsacl.1*
%{_mandir}/man1/setcifsacl.1*
%{_mandir}/man8/cifs.upcall.8*
%{_mandir}/man8/cifs.idmap.8*
%{_mandir}/man8/mount.cifs.8*
