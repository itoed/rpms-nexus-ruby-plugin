Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:
License:        None
BuildArch:      %{_arch}

%description

%install
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%changelog
* Thu Jan 1 1970 Firstname Lastname <author@example.com> - 0.1-1
- Initial release