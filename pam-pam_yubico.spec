%define	module	pam_yubico
Summary:	A Pluggable Authentication Module for Yubikeys
Summary(pl.UTF-8):	Moduł PAM dla urządzeń Yubikey
Name:		pam-%{module}
Version:	2.26
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubico-pam/Releases/%{module}-%{version}.tar.gz
# Source0-md5:	727d5937dcc864bfe6201f90f35728a5
URL:		https://developers.yubico.com/yubico-pam
BuildRequires:	asciidoc
BuildRequires:	libyubikey-devel >= 1.5
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	ykclient-devel >= 2.15
BuildRequires:	ykpers-devel >= 1.8.0
Requires:	libyubikey >= 1.5
Requires:	pam
Requires:	ykclient >= 2.15
Requires:	ykpers >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is pam_yubico, a pluggable authentication module that can be used
with Linux-PAM and Yubikeys. This module supports Yubikey OTP
checking.

%description -l pl.UTF-8
Ten pakiet zawiera pam_yubico - ładowalny moduł uwierzytelniający,
który może być używany ze szkieletem Linux-PAM oraz urządzeniami
Yubikey. Ten moduł obsługuje sprawdzanie haseł jednorazowych (OTP)
Yubikey.

%prep
%setup -q -n %{module}-%{version}

%build
%configure \
	--disable-silent-rules \
	--with-pam-dir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/security/%{module}.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/*.adoc
%attr(755,root,root) /%{_lib}/security/pam_yubico.so
%attr(755,root,root) %{_bindir}/ykpamcfg
%{_mandir}/man1/ykpamcfg.1*
%{_mandir}/man8/pam_yubico.8*
