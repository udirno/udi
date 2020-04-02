#include "DataCollection.h" 	 	    		
#include <stdlib.h>
#include <string.h>

#define RECORD_ELEMENTS 4

int *Records = NULL;
int MaximumRecords = 0;
int TotalRecordCount = 0;

void ClearRecords(){
    TotalRecordCount = MaximumRecords= 0;
    if(Records){
        free(Records);
        Records = NULL;
    }
}

int RecordCount(){
    return TotalRecordCount;
}

int InsertRecord(int id, int dob, int height, int weight){
    int Index = TotalRecordCount * RECORD_ELEMENTS;

    if((0 >= id) || (0 >= dob) || (0 >= height) || (0 >= weight)){
        return -1;
    }
    if(TotalRecordCount >= MaximumRecords){
        int *NewRecords;

        MaximumRecords = MaximumRecords ? MaximumRecords * 2 : 128;
        NewRecords = malloc(MaximumRecords * RECORD_ELEMENTS * sizeof(int));
        if(TotalRecordCount){
            memcpy(NewRecords, Records, TotalRecordCount * RECORD_ELEMENTS * sizeof(int));
            free(Records);
        }
        Records = NewRecords;
    }
    Records[Index++] = id;
    Records[Index++] = dob;
    Records[Index++] = height;
    Records[Index++] = weight;
    return TotalRecordCount++;
}

int QueryRecord(int index, int element){
    if((0 > index)||(index >= TotalRecordCount)||(0 >= element)||(element > RECORD_ELEMENTS)){
        return -1;
    }
    return Records[index * RECORD_ELEMENTS + element - 1];
}
