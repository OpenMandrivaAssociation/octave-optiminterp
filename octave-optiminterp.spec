%define octpkg optiminterp

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	An optimal interpolation toolbox for Octave
Name:		octave-%{octpkg}
Version:	0.3.4
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.9

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package provides functions to perform a n-dimensional optimal
interpolations of arbitrarily distributed data points with Octave.

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

