# Makefile 3
CC	= g++
CFLAGS	= -Wall -g

main.o: main.cpp iodat.h
	${CC} ${CFLAGS} -c main.cpp
iodat.o: iodat.cpp iodat.h
	${CC} ${CFLAGS} -c iodat.cpp

clean: 
	rm -f *.o 
