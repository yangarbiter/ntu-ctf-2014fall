#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]) {
	if (argc != 3) {
		exit (1);
	}

	unsigned short pid = (unsigned short) atoi (argv[1]);
	int i;
	char *s = argv[2];

	for (i = 0 ; i < strlen (s) ; i++) {
		pid = (unsigned short) ((pid << 1) | (pid >> 15));
		s[i] = (s[i] + 32 + pid) % 95;
		if (s[i] <= 31) {
			s[i] += 95;
		}
	}

	s[32] = '\0';
	printf ("%32s\n", s);
	return 0;
}
