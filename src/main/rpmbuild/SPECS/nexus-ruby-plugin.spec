Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        Nexus Ruby Plugin
License:        None
BuildArch:      %{_arch}
Source0:        %{name}-%{version}-bundle.zip

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%description

%prep
%setup -q -c -T -b 0

%install
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%changelog
* Thu Jan 1 1970 Firstname Lastname <author@example.com> - 0.1-1
- Initial release
