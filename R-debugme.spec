#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-debugme
Version  : 1.1.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/debugme_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/debugme_1.1.0.tar.gz
Summary  : Debug R Packages
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
control debugging of packages via environment variables.

%prep
%setup -q -c -n debugme

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523298985

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523298985
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library debugme
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library debugme
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library debugme
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library debugme|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/debugme/DESCRIPTION
/usr/lib64/R/library/debugme/INDEX
/usr/lib64/R/library/debugme/LICENSE
/usr/lib64/R/library/debugme/Meta/Rd.rds
/usr/lib64/R/library/debugme/Meta/features.rds
/usr/lib64/R/library/debugme/Meta/hsearch.rds
/usr/lib64/R/library/debugme/Meta/links.rds
/usr/lib64/R/library/debugme/Meta/nsInfo.rds
/usr/lib64/R/library/debugme/Meta/package.rds
/usr/lib64/R/library/debugme/NAMESPACE
/usr/lib64/R/library/debugme/NEWS.md
/usr/lib64/R/library/debugme/R/debugme
/usr/lib64/R/library/debugme/R/debugme.rdb
/usr/lib64/R/library/debugme/R/debugme.rdx
/usr/lib64/R/library/debugme/README.Rmd
/usr/lib64/R/library/debugme/README.markdown
/usr/lib64/R/library/debugme/help/AnIndex
/usr/lib64/R/library/debugme/help/aliases.rds
/usr/lib64/R/library/debugme/help/debugme.rdb
/usr/lib64/R/library/debugme/help/debugme.rdx
/usr/lib64/R/library/debugme/help/paths.rds
/usr/lib64/R/library/debugme/html/00Index.html
/usr/lib64/R/library/debugme/html/R.css
/usr/lib64/R/library/debugme/screencast.gif
