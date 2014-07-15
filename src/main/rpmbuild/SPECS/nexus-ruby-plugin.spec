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

%define         plugindir /usr/local/sonatype-work/nexus/plugin-repository

%description

%prep
%setup -q

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}/%{plugindir}
cp -r %{builddir}/%{name}-%{version} %{plugindir}

%files
%defattr(-,nexus,nexus,-)
%{plugindir}

%changelog
* Tue Jul 15 2014 Eduardo Ito <ed@fghijk.local> - 1.4.1-1
- Initial release
