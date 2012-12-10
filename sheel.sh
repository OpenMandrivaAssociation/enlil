svn co http://svn.enlightenment.org/svn/e/trunk/enlil enlil; \
	cd enlil; \
	SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
	v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
	v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
	v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
	PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
	cd ..; \
	tar -Jcf enlil-$PKG_VERSION.tar.xz enlil/ --exclude .svn --exclude .*ignore

