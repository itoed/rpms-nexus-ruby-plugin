Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        Nexus Ruby Plugin
License:        None
BuildArch:      %{_arch}
Source:         %{name}-%{version}-bundle.zip

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%description

%prep
%setup -q

%install
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%changelog
* Tue Jul 15 2014 Eduardo Ito <ed@fghijk.local> - 1.4.1-1
- Initial release
