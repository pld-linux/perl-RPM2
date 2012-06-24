%include	/usr/lib/rpm/macros.perl
Summary:	Perl bindings for the RPM Package Manager API
Summary(pl):	Dowi�zania do API zarz�dcy pakiet�w RPM
Name:		perl-RPM2
Version:	0.63
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/CHIPT/RPM2-%{version}.tar.gz
# Source0-md5:	3a84c4e501f36f17a952ed2d0bc9da7b
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPM2 module provides an object-oriented interface to querying both
the installed RPM database as well as files on the filesystem.

%prep
%setup -q -n RPM2-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/RPM2.pm
%{perl_vendorarch}/auto/RPM2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RPM2/*.so
%{_mandir}/man3/*
