#include <time.h>

struct DataObject {
	char ip[16];
	//char time[21];
	struct tm time;
	char url[100];
};
