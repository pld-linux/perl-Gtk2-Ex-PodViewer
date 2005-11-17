#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	Ex-PodViewer
Summary:	A Gtk2 widget for displaying Plain old Documentation (POD)
Summary(pl):	Widget Gtk2 do wy¶wietlania plików POD (Plain old Documentation)
Name:		perl-%{pdir}-%{pnam}
Version:	0.13
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5a381c24368883899ab8c41cdf1ed2b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Gtk2 widget for displaying Plain old Documentation (POD).

%description -l pl
Widget Gtk2 do wy¶wietlania plików POD (Plain old Documentation).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/podviewer
%{perl_vendorlib}/Gtk2/Ex/PodViewer.pm
%dir %{perl_vendorlib}/Gtk2/Ex/PodViewer
%{perl_vendorlib}/Gtk2/Ex/PodViewer/Parser.pm
%{_mandir}/man[13]/*
