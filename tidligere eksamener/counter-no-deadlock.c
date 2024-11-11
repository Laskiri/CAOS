#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "common.h"
#include "common_threads.h"

#ifdef linux
#include <semaphore.h>
#elif __APPLE__
#include "zemaphore.h"
#endif

sem_t a, b, c, d;
volatile int counter = 0;

void *t3task(void *arg) {
    Sem_wait(&a);
    Sem_wait(&c);
    Sem_wait(&d);
    counter++;
    Sem_post(&d);
    Sem_post(&c);
    Sem_post(&a);
    return NULL;
}

void *t2task(void *arg) {
    Sem_wait(&b);
    Sem_wait(&c);
    Sem_wait(&d);
    counter++;
    Sem_post(&d);
    Sem_post(&c);
    Sem_post(&b);
    return NULL;
}

void *t1task(void *arg) {
	Sem_wait(&a);
	Sem_wait(&b);
	Sem_wait(&c);
	counter++;
	Sem_post(&c);
	Sem_post(&b);
	Sem_post(&a);
    return NULL;
}

int main(int argc, char *argv[]) {
    Sem_init(&a, 1);
    Sem_init(&b, 1);
    Sem_init(&c, 1);
    Sem_init(&d, 1);

    pthread_t t1, t2, t3;
    Pthread_create(&t1, NULL, t1task, NULL);
    Pthread_create(&t2, NULL, t2task, NULL);
    Pthread_create(&t3, NULL, t3task, NULL);
    Pthread_join(t1, NULL);
    Pthread_join(t2, NULL);
    Pthread_join(t3, NULL);
    printf("result: %d (should be 3)\n", counter);
    return 0;
}
    
