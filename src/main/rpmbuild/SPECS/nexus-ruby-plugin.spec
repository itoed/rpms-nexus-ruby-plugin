Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        Nexus Ruby Plugin
License:        None
BuildArch:      %{_arch}
Source:         %{name}-%{version}-bundle.zip

%define         plugindir /usr/local/sonatype-work/nexus/plugin-repository

%description

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{plugindir}
cp -r %{name}-%{version} %{buildroot}%{plugindir}

%files
%defattr(-,nexus,nexus,-)
%{plugindir}

%changelog
* Tue Jul 15 2014 Eduardo Ito <ed@fghijk.local> - 1.4.1-1
- Initial release
