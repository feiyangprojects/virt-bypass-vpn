#
# spec file for package virt-bypass-vpn
#
# Copyright (c) 2024 Fei Yang <io@feiyang.eu.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           virt-bypass-vpn
Version:        1.0.1
Release:        0
Summary:        Bypass default libvirt network from VPN
License:        GPL-3.0-only
Source0:        package.tar.gz
Requires:       iproute2
Requires:       libvirt-client
BuildArch:      noarch

%description
Bypass default libvirt network from VPN

%prep
%setup -q -n %{name}

%install
%make_install

%files
%{_sbindir}/%{name}
%license LICENSE

