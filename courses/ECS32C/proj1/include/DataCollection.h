#ifndef DATACOLLECTION_H 	 	    		
#define DATACOLLECTION_H

#include <stddef.h>

#ifdef __cplusplus
extern "C"{
#endif
 
#define RECORD_ELEMENT_ID       1
#define RECORD_ELEMENT_DOB      2
#define RECORD_ELEMENT_HEIGHT   3
#define RECORD_ELEMENT_WEIGHT   4

void ClearRecords();
int RecordCount();
int InsertRecord(int id, int dob, int height, int weight);
int QueryRecord(int index, int element);

#ifdef __cplusplus
}
#endif

#endif
