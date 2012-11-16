#Makfile for homework #6
CC = g++
CFLAGS = -Wall -g

all: generator consumer dispatcher

generator: generator.o
	 ${CC} ${CFLAGS} -o generator generator.o

generator.o: generator.cpp
	 ${CC} ${CFLAGS} -c generator.cpp

consumer: consumer.o
	 ${CC} ${CFLAGS} -o consumer consumer.o

consumer.o: consumer.cpp
	 ${CC} ${CFLAGS} -c consumer.cpp

dispatcher: dispatcher.o
	${CC} ${CFLAGS} -o dispatcher dispatcher.o

dispatcher.o: dispatcher.cpp
	${CC} ${CFLAGS} -c dispatcher.cpp

clean:
	rm -f *.o