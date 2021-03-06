SUFFIXES = .c .mod .def .o .obj .lo .a .m .mxm

SHELL=/bin/bash


prefix= @prefix@
datarootdir= @datarootdir@
srcdir= @srcdir@
mandir= @mandir@
exec_prefix=@exec_prefix@
bindir= @bindir@
INSTALL_PROGRAM = install

DISTFILES = Makefile.in configure.ac configure \
            README version.c COPYING examples src \
            INSTALL

GM2=/opt/bin/gm2
G++=/opt/bin/g++
CC=/opt/bin/gcc

TARGET_SUBDIR=/opt/gm2/lib64

ACLOCAL_AMFLAGS=-I m4


help:  force
	@echo "knows about:  all, clean, ball"

SOURCES = \
          macroObjects.mod Points.mod Fractions.mod PolyMatrix3D.mod Transform3D.mod \
          delay.mod GC.mod popWorld.mod twoDsim.mod NetworkOrder.mod \
          roots.mod coord.mod polar.mod history.mod stairs.mod rpc.mod \
          snooker.mod wall.mod npn.mod wallv.mod slope.mod para.mod testpy.mod \
          deviceIf.mod ramps.mod ramps2.mod boxes.mod wallh.mod bounce.mod line.mod bounce2.mod \
          bounce3.mod bounce4.mod bounce5.mod bagatelle.mod elc.mod rboxes.mod circle.mod

noinst_LTLIBRARIES = libpgeif.la
libpgeif_la_SOURCES = macroObjects.mod Points.mod Fractions.mod PolyMatrix3D.mod \
                      Transform3D.mod delay.mod GC.mod popWorld.mod \
                      twoDsim.mod roots.mod coord.mod polar.mod history.mod \
                      deviceIf.mod rpc.mod deviceBuffer.mod pgeif.mod NetworkOrder.mod \
                      buffers.c

MY_DEPS = macroObjects.lo Points.lo Fractions.lo PolyMatrix3D.lo	\
                      Transform3D.lo delay.lo GC.lo popWorld.lo		\
                      twoDsim.lo roots.lo coord.lo polar.lo		\
                      history.lo deviceIf.lo rpc.lo			\
                      deviceBuffer.lo pgeif.lo NetworkOrder.lo	\
                      buffers.lo

BUILT_SOURCES = circles.m rotating-line.m rotating-circles.m

# PYTHON_VERSION=$(shell python --version 2>&1 | cut -f2 -d' ')
PYTHON_VERSION=2.7

GM2_LIB_DIR=/opt/gm2/lib/gcc/x86_64-linux-gnu/4.7.4/m2

SRC_PATH_PIM=$(srcdir):$(GM2_LIB_DIR)/libgm2/pim:$(GM2_LIB_DIR)/iso

OBJECTS = $(SOURCES:%.mod=%.o)
PROFILE =
CHECK = -fsoft-check-all

GM2FLAGS = $(PROFILE) $(CHECK) -g -fiso -fextended-opaque -I$(srcdir)/src -g
GM2LIBDIR = /opt/gm2

EXAMPLES = elc

LIBTOOL_DEPS = @LIBTOOL_DEPS@
libtool: $(LIBTOOL_DEPS)
	$(SHELL) ./config.status libtool

ball: ball.raw
	@echo please ignore the error message about eof
	make playback

ball.raw: libpgeif.la
	PYTHONPATH=.:$(srcdir)/src python $(srcdir)/examples/ball.py

triangle.raw: libpgeif.la
	PYTHONPATH=.:$(srcdir)/src python $(srcdir)/examples/triangle.py

circles.m: $(srcdir)/src/circles.mxm
	python $(srcdir)/src/max2code.py -o $@ $<

rotating-circles.m: $(srcdir)/src/rotating-circles.mxm
	python $(srcdir)/src/max2code.py -o $@ $<

rotating-line.m: $(srcdir)/src/rotating-line.mxm
	python $(srcdir)/src/max2code.py -o $@ $<

.mod.lo:
	$(LIBTOOL) --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile gm2 -fcpp -g -fiso -fextended-opaque -I. -I$(srcdir) -c $< -o $@

.c.lo:
	$(LIBTOOL) --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile gcc -c $(CFLAGS_FOR_TARGET) $(LIBCFLAGS) $(libgm2_la_M2FLAGS) $< -o $@

libpgeif.la:  $(MY_DEPS)
	swig -outdir . -o pgeif_wrap.cxx -c++ -python $(srcdir)/pgeif.i
	$(LIBTOOL) --tag=CC --mode=compile g++ -g -c pgeif_wrap.cxx -I/usr/include/python$(PYTHON_VERSION) -o pgeif_wrap.lo
	gm2 -c -g -I$(SRC_PATH_PIM) -fcpp -fmakelist $(srcdir)/pgeif.mod
	gm2 -c -g -I$(SRC_PATH_PIM) -fcpp -fmakeinit -fshared $(srcdir)/pgeif.mod
	$(LIBTOOL) --tag=CC --mode=compile g++ -g -c _m2_pgeif.cpp -o _m2_pgeif.lo
	$(LIBTOOL) --tag=CC --mode=link gcc -g _m2_pgeif.lo $(MY_DEPS) \
            pgeif_wrap.lo \
           -L$(GM2LIBDIR)/lib64 \
           -rpath `pwd` -lgm2 -liso -lgcc -lstdc++ -lpth -lc -lm -o libpgeif.la
	cp .libs/libpgeif.so _pgeif.so

output.raw: libpgeif.la
	PYTHONPATH=.:$(srcdir)/src python $(srcdir)/examples/exampleBoxes.py

playback: force
	PYTHONPATH=.:$(srcdir)/src python $(srcdir)/src/pgeplayback.py

boxes.raw:  libpgeif.la
	PYTHONPATH=.:$(srcdir)/src python $(srcdir)/examples/boxes.py

foo: circles.m $(OBJECTS)
	gm2 $(GM2FLAGS) -fonlylink $(srcdir)/foo.mod

bounce: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bounce.mod

bounce2: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bounce2.mod

bounce3: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bounce3.mod

bounce4: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bounce4.mod

bounce5: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bounce5.mod

bagatelle: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/bagatelle.mod

elc: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/elc.mod

elc2: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/elc2.mod

line: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/line.mod

wallh: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/wallh.mod

rboxes: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/rboxes.mod

circle: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/circle.mod

boxes: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/boxes.mod

ramps: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/ramps.mod

ramps2: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/ramps2.mod

slope: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/slope.mod

stairs: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/stairs.mod

py: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -pg -g -fiso -fextended-opaque -fonlylink testpy.mod

para: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink para.mod && ./a.out
	./produce-avi

wallv: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 $(GM2FLAGS) -fonlylink wallv.mod

wall: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 $(GM2FLAGS) -fonlylink wall.mod

snooker: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/snooker.mod

npn: $(OBJECTS)
	$(RM) *.ms *.png
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/npn.mod && ./a.out

test: $(OBJECTS)
	gm2 -fcpp -I. $(GM2FLAGS) -fonlylink $(srcdir)/test.mod && ./a.out

transforms: rotating-circles.asc rotating-line.asc

release: force
	pwd
	echo pge-`sed -e '/version_string/!d' \
          -e 's/[^0-9.]*\([0-9.]*\).*/\1/' -e q $(srcdir)/version.c` > .fname
	-rm -rf `cat .fname`
	mkdir `cat .fname`
	dst=`cat .fname`; for f in $(DISTFILES); do \
           cp -rp $(srcdir)/$$f $$dst/$$f ; \
        done
	tar --gzip -chf `cat .fname`.tar.gz `cat .fname`
	-rm -rf `cat .fname` .fname

clean: force
	$(RM) *.o *.m *.cpp *~ $(EXAMPLES) *.so *.lo *.la
	$(RM) -rf .libs *_m2.cpp

clear: force
	$(RM) *.png *.ms *.cpp

force:
