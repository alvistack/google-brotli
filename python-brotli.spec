# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-brotli
Epoch: 100
Version: 1.1.0
Release: 1%{?dist}
Summary: Brotli compression format
License: MIT
URL: https://github.com/google/brotli/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-static
BuildRequires: libtool
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-brotli
Summary: Brotli compression format
Requires: python3
Provides: python3-brotli = %{epoch}:%{version}-%{release}
Provides: python3dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotli) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-brotli
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

%files -n python%{python3_version_nodots}-brotli
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-brotli
Summary: Brotli compression format
Requires: python3
Provides: python3-brotli = %{epoch}:%{version}-%{release}
Provides: python3dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotli) = %{epoch}:%{version}-%{release}

%description -n python3-brotli
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

%files -n python3-brotli
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-brotli
Summary: Brotli compression format
Requires: python3
Provides: python3-brotli = %{epoch}:%{version}-%{release}
Provides: python3dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotli) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotli = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotli) = %{epoch}:%{version}-%{release}

%description -n python3-brotli
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

%files -n python3-brotli
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
