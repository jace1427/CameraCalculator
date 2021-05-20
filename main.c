#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

char *commands[][3] = { 
    {"python3", "backend/app.py", NULL}, 
    {"/bin/bash", "frontend/run_server.sh", NULL}
};

void print_pid(int i) {
    printf("PID[%d] Running -> ", getpid());
    
    for (int j = 0; j < 3; j++) {
        printf("%s ", commands[i][j]);
    }

    printf("\n");
}

int main() {
    
    pid_t pool[2];
    for (int i = 0; i < 2; i++) {

        pool[i] = fork();
        
        if (pool[i] < 0) {
            printf("Fork error\n");
            exit(1);
        }

        if (pool[i] == 0) {
            print_pid(i);            
            execvp(commands[i][0], commands[i]);     
        }
        sleep(1);
    }
}
