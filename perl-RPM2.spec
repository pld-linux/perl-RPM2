#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	RPM2 - Perl bindings for the RPM Package Manager API
Summary(pl):	RPM2 - dowi±zania do API zarz±dcy pakietów RPM
Name:		perl-RPM2
Version:	0.66
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/CHIPT/RPM2-%{version}.tar.gz
# Source0-md5:	3e53f141c7160f1b82087e93c6295240
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPM2 module provides an object-oriented interface to querying both
the installed RPM database as well as files on the filesystem.

%description -l pl
Modu³ RPM2 dostarcza obiektowo zorientowany interfejs do zapytañ
dotycz±cych zarówno bazy zainstalowanych pakietów RPM, jak i plików
obecnych w systemie.

%prep
%setup -q -n RPM2-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/RPM2.pm
%dir %{perl_vendorarch}/auto/RPM2
%{perl_vendorarch}/auto/RPM2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RPM2/*.so
%{_mandir}/man3/*
