## How to Create .debian Package

make directory packagename_v1.0
make a `DEBIAN` dir
inside it 
create a `control` file

**control file should content:**
```
Package: Name of Package
Version: 1.0
Architecture: all
Maintainerr: Anonymous
Essential: no
Priority: optional
Description: LONG DESCRIPTION OF PACKAGE
```

increase version according your package update or patch,
you can use your name in Maintainer field

back `cd ..` move up
in package-name dir

in termux 
make directory according to filesystem.
```
mkdir -p data/data/com.termux/files/usr/bin/
```

write a your script in bin directory.
if you want to create library files just change `/bin`
to `/lib` 

in other linux filesystem

use direct directory

you you want to stored script in bin then create `/bin`
lateral to `DEBIAN` directory.

**give DEBIAN directory 755 or 775permission**
```
chmod 0755 /pkg-namev_1.0/DEBIAN
```


**to build .deb pkg**

come to package name dir outside of dir

```
dpkg-deb -b name_of_package_v1.0

# -b:  --build 
```

debian archive will be created.

then install by
```
apt install ./nameofpkg.deb

# OR

dpkg -i name.deb
```

after installed

change script permission of script inside `/bin`
directory.

