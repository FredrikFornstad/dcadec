Name:           dcadec
Version:        0.2.0
Release:        1%{?dist}
License:        LGPLv2.1
Summary:        DTS Coherent Acoustics decoder with support for HD extensions
Url:            https://github.com/foo86/dcadec/
Group:          System Environment/Libraries
Source:         https://github.com/foo86/dcadec/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.

Supported features:
    Decoding of standard DTS core streams with up to 5.1 channels
    Decoding of DTS-ES streams with discrete back channel
    Decoding of High Resolution streams with up to 7.1 channels and extended bitrate
    Decoding of 96/24 core streams
    Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
    Downmixing to stereo and 5.1 using embedded coefficients

Features not implemented:
    Decoding of DTS Express streams
    Applying dynamic range compression and dialog normalization

%package libs
Summary:	DTS Coherent Acoustics decoder with support for HD extensions
Group:		Development/Libraries

%description libs
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.


%package devel
Summary:	Development files for dcadec
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development files for dcadec.
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.

%prep
%setup -q

%build
make %{?_smp_mflags} CONFIG_SHARED=1 LDFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX="/usr" LIBDIR="%{_libdir}" BINDIR="%{_bindir}" INCLUDEDIR="%{_includedir}" CONFIG_SHARED=1
chmod 0755 %{buildroot}%{_libdir}/lib*so*

%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README.md COPYING.LGPLv2.1
%{_bindir}/%{name}

%files libs
%defattr(-,root,root,-)
%{_libdir}/libdcadec.so.*

%files devel
%defattr(-,root,root,-)
%doc README.md COPYING.LGPLv2.1
%{_libdir}/libdcadec.so
%{_includedir}/lib%{name}/*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Jan 26 2016 Fredrik Fornstad <fredrik.fornstad@gmail.com> 0.2.0-1
- Initial release for ClearOS
