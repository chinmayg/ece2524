#include "Process.h"

#define	PARENT_READ     readpipe[0]
#define	CHILD_WRITE	readpipe[1]
#define CHILD_READ      writepipe[0]
#define PARENT_WRITE	writepipe[1]

Process::Process(const std::vector<std::string> &args)
{
	//Checks the number of arguments
	if(args.size() == 0){
		perror("Not Enough Arguments");
		throw "Not Enough Arguments";
	}
	//Checks if the parent pipe write end is ok
	if(pipe(writepipe) == -1){
		perror("Pipe write issue");
		throw "Pipe write issue";
	}
	//Checks if the parent pipe read end is ok
	if(pipe(readpipe) == -1){
		perror("Pipe read issue");
		throw "Pipe read issue";	
	}

	//Forks a Child Process
	m_pid = fork();

	if(m_pid < 0){
		perror("Process fork issue");
		throw "Process Fork Issue";
	}
	else if(m_pid == 0){
	//if child Process
		close(PARENT_WRITE);
		close(PARENT_READ);
		dup2(CHILD_WRITE,1);
		if (dup2(CHILD_WRITE, 1) < 0){
			perror("dup2 CHILD_WRITE");
			throw std::string("dup2 CHILD_WRITE");
		}
		close(CHILD_WRITE);
		dup2(CHILD_READ,0);
		if (dup2(CHILD_READ, 0) < 0){
			perror("dup2 CHILD_READ");
			throw std::string("dup2 CHILD_READ");
		} 
		close(CHILD_READ);
		std::vector<const char*> cargs;
		std::transform(args.begin(),args.end(), std::back_inserter(cargs), 
		[](std::string s) {
				return s.c_str();
			} );
		cargs.push_back( NULL );
		int erroCheck = execv(cargs[0], const_cast<char**>(&cargs[0]));
       		//int erroCheck = execv(args[0].c_str(), NULL);
    		if(erroCheck < 0){
     			perror("Error: Running Generator");
      			exit(1);
		}
	}
	else{
	//if parent Process
		std::cerr << "Process[" << pid()-1 <<"] Process constructor " << std::endl;
		close(CHILD_READ);
		close(CHILD_WRITE);
		close(PARENT_WRITE);
		m_pread = fdopen(PARENT_READ, "r");

	}
}

Process::~Process()
{
	int status;
	pid_t pid = waitpid(m_pid, &status, 0);
	if(pid < 0){
        	perror("Error: ~Process waitpid");
        	throw "Error: ~Process waitpid";
    	}

	fclose(m_pread);

	// Kill the child process
	kill(m_pid, SIGTERM);	
}

void Process::write(const std::string& str)
{
	int error = ::write(PARENT_WRITE, str.c_str(), str.length());
	if(error < 0){
		perror("Error: ~Write");
		throw "Error: ~Write";
	}
}

std::string Process::readline()
{
	std::string readLine;
	char* buffer = NULL;
	size_t buffer_size;

	getline(&buffer, &buffer_size, m_pread);
	readLine = buffer;
	std::cout << buffer << std::endl;
	return readLine;
}
