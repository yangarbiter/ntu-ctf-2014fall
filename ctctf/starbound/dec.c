#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]) {
	if (argc != 3) {
		exit (1);
	}

	unsigned short pid = (unsigned short) atoi (argv[1]);
	int i, t;
	char *s = argv[2];

	for (i = 0 ; i < strlen (s) ; i++) {
		pid = (unsigned short) ((pid << 1) | (pid >> 15));

		t = (s[i] - pid - 32) % 95;
		if (t < 0) {
			t += 95;
		}
		if (t <= 31) {
			t += 95;
		}
		putchar (t);
	}
	puts ("");

	return 0;
}
