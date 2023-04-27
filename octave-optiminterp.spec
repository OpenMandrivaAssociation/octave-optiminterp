%global octpkg optiminterp

Summary:	An optimal interpolation toolbox for Octave
Name:		octave-optiminterp
Version:	0.3.7
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/optiminterp/
Source0:	https://downloads.sourceforge.net/octave/optiminterp-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
An optimal interpolation toolbox providing functions to perform a
n-dimensional optimal interpolations of arbitrarily distributed data
points.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
export CC=gcc
export CXX=g++
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

