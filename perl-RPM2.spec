#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	RPM2 - Perl bindings for the RPM Package Manager API
Summary(pl.UTF-8):	RPM2 - dowiązania do API zarządcy pakietów RPM
Name:		perl-RPM2
Version:	0.67
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/CHIPT/RPM2-%{version}.tar.gz
# Source0-md5:	f9888629116a9b1a5cc39d2e16d44afd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-devel >= 4.4.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPM2 module provides an object-oriented interface to querying both
the installed RPM database as well as files on the filesystem.

%description -l pl.UTF-8
Moduł RPM2 dostarcza obiektowo zorientowany interfejs do zapytań
dotyczących zarówno bazy zainstalowanych pakietów RPM, jak i plików
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
