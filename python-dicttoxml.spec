# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# NOTES:
# - 'module' should match the Python import path (first component?)
# - 'egg_name' should equal to Python egg name
# - 'pypi_name' must match the Python Package Index name
%define		module		dicttoxml
%define		egg_name	dicttoxml
%define		pypi_name	dicttoxml
Summary:	Converts a Python dictionary or other native data type into a valid XML string
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	1.7.4
Release:	5
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://pypi.debian.net/dicttoxml/%{module}-%{version}.tar.gz
# Source0-md5:	ec5643a048cf32dad3c28db236b923e4
URL:		https://github.com/quandyfactory/dicttoxml
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
#BuildRequires:	python-
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a Python dictionary or other native data type into a valid
XML string.

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Converts a Python dictionary or other native data type into a valid
XML string.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.markdown
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.markdown
%{py3_sitescriptdir}/%{module}.py*
%{py3_sitescriptdir}/__pycache__/dicttoxml*
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
