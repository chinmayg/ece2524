#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

int main(){
  int mypipe[2];
  int genStatus;
  int conStatus;
  //Create the pipe
  if(pipe(mypipe) == -1){
    cerr << "Pipe didnt open" << endl;
    return 1;
  }
  int genPID = fork();
  //Child Process for Generator
  if(genPID == 0){
    close(mypipe[0]); //close unused read end
    dup2(mypipe[1],1);
    close(mypipe[1]);
    execve("./generator",NULL,NULL);
    exit(0);
  }
  int conPID = fork();
  //Child Process for Consumer
  if(conPID == 0){
    close(mypipe[1]); //close unused write end
    dup2(mypipe[0],0);
    close(mypipe[0]);
    execve("./consumer",NULL,NULL);
    exit(0);
  }
  sleep(1);
  kill(genPID, SIGTERM);
  pid_t pid = waitpid(genPID,&genStatus,0);
  if(pid > 0)
    cerr << "child[" << genPID << "] exited with status " << genStatus << endl;
  pid = waitpid(conPID,&conStatus,0);
  if(pid > 0)
    cerr << "child[" << conPID << "] exited with status " << conStatus << endl;

  return 0;
}
