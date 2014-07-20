Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        Nexus Ruby Plugin
License:        None
BuildArch:      %{_arch}
Requires:       nexus
Source:         %{name}-%{version}-bundle.zip
AutoReqProv:    no

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%define         plugindir /usr/local/sonatype-work/nexus/plugin-repository

%description
Plugin to enhance Nexus with Ruby support

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
