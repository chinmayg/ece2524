#Makfile for homework #6
CC = g++
CFLAGS = -Wall -g

all: generator consumer

generator: generator.o
	 ${CC} ${CFLAGS} -o generator generator.o

generator.o: generator.cpp
	 ${CC} ${CFLAGS} -c generator.cpp

consumer: consumer.o
	 ${CC} ${CFLAGS} -o consumer generator.o

consumer.o: consumer.cpp
	 ${CC} ${CFLAGS} -c consumer.cpp

clean:
	rm -f *.o