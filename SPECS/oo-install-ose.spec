Name:		oo-install-ose
Version:	2.0.1931
Release:	1%{?dist}
Summary:	OpenShift Enterprise Installer

Group:		System Environment/Daemons
License:	GPL
Source0:	%{name}.zip
Source1:	oo-install-ose.sh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch

Requires:	unzip, ruby, openssh-clients
Provides:	oo-install-ose

# disable debug packages and the stripping of the binaries
%global _enable_debug_package 0
%global debug_package %{nil}

%description
System deployer

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/oo-install-ose
install -m 755 oo-install-ose %{buildroot}/opt/oo-install-ose/oo-install-ose
install -m 644 oo-install-ose-20140326-1931.zip %{buildroot}/opt/oo-install-ose/oo-install-ose-20140326-1931.zip
install -m 644 oo_install_launcher.README.txt %{buildroot}/opt/oo-install-ose/oo_install_launcher.README.txt

mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -m 755 %{SOURCE1} %{buildroot}/%{_sbindir}/oo-install-ose

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /opt/oo-install-ose/oo-install-ose
%attr(0644,root,root) /opt/oo-install-ose/oo-install-ose-20140326-1931.zip
%attr(0644,root,root) /opt/oo-install-ose/oo_install_launcher.README.txt 
%attr(0755,root,root) %{_sbindir}/oo-install-ose

%changelog
* Mon Apr 21 2014 Miguel Perez <mperez@redhat.com> 2.0.1931-1
- Initial RPM 

