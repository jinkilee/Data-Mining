//*/
#define _XOPEN_SOURCE
#include "dataobj.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int n = 100;
	struct DataObject* data = (struct DataObject*)malloc(sizeof(struct DataObject)*n);
	int i;
	struct tm time;

	for(i = 0; i < n; i++) {
		// 116 9 14 9 1476404273
		strptime("14/Oct/2016:09:17:53", "%d/%b/%Y:%H:%M:%S", &time);
		printf("%d %d %d %d %ld\n", time.tm_year+1900, time.tm_mon+1, time.tm_mday, time.tm_hour, mktime(&time));
	}

	free(data);

	return 0;
}
