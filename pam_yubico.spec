Summary:	A Pluggable Authentication Module for yubikeys
Name:		pam_yubico
Version:	2.24
Release:	1
License:	BSD
Group:		Applications/System
URL:		http://opensource.yubico.com/yubico-pam/
Source0:	http://opensource.yubico.com/yubico-pam/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3420a1538031aee90af1c4e83988994d
BuildRequires:	libyubikey-devel >= 1.5
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	ykclient-devel >= 2.15
BuildRequires:	ykpers-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is pam_yubico, a pluggable authentication module that can be used
with Linux-PAM and yubikeys. This module supports yubikey OTP
checking.

%prep
%setup -q

%build
%configure \
	--libdir=/%{_lib} \
	--with-pam-dir=/%{_lib}/security/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_lib}/security/pam_yubico.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog
%attr(755,root,root) /%{_lib}/security/pam_yubico.so
%attr(755,root,root) %{_bindir}/ykpamcfg
%{_mandir}/man1/ykpamcfg.1*
%{_mandir}/man8/pam_yubico.8*
