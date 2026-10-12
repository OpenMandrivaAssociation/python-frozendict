Name:		python-frozendict
Version:	2.4.7
Release:	2
Summary:	Immutable dictionary implementation
License:	LGPL-3.0
Group:		Development/Python
URL:		https://github.com/Marco-Sulla/python-frozendict
Source0:	https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

# Keep the pure-Python mapping so this stays noarch. There is no
# CPython 3.14 C source in 2.4.7. The env must be set in both
# %build and %install — setup.py re-decides C vs py at install time.
%build -p
export FROZENDICT_PURE_PY=1
%install -p
export FROZENDICT_PURE_PY=1

%description
An immutable mapping type for Python. Used by einx (and thus
vector-quantize-pytorch / ACE-Step).

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/frozendict
%{py_sitedir}/frozendict-*.*-info
