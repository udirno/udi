#include <stdio.h> 	 	    		
#include <stdlib.h>
#include <stdbool.h>
#include "DataCollection.h"
#include "IndexSorter.h"

bool ParseOrder(const char *option, int *order);
bool LoadFile(const char *datafile);

int main(int argc, char *argv[]){
    int *Indices;
    int Order[4] = {RECORD_ELEMENT_ID, RECORD_ELEMENT_DOB, RECORD_ELEMENT_HEIGHT, RECORD_ELEMENT_WEIGHT};
    bool PrintError = false;

    PrintError = 2 > argc;
    if(3 <= argc){
        PrintError = !ParseOrder(argv[2],Order);
    }
    if(!PrintError){
        PrintError = !LoadFile(argv[1]);
    }
    if(PrintError){
        fprintf(stderr,"Syntax Error: proj1 datafile [order]\n              order - i/I ID, d/D DOB, h/H Height, w/W Weight\n");
        return EXIT_FAILURE;
    }
    Indices = malloc(sizeof(int) * RecordCount());
    for(int Index = 0; Index < RecordCount(); Index++){
        Indices[Index] = Index;
    }
    SortByIndices(Indices, RecordCount(), Order, 4);
    for(int Index = 0; Index < RecordCount(); Index++){
        printf("%d %d %d %d\n",QueryRecord(Indices[Index], RECORD_ELEMENT_ID),QueryRecord(Indices[Index], RECORD_ELEMENT_DOB),QueryRecord(Indices[Index], RECORD_ELEMENT_HEIGHT),QueryRecord(Indices[Index], RECORD_ELEMENT_WEIGHT));
    }
    return EXIT_SUCCESS;
}

bool ParseOrder(const char *option, int *order){
    int OrderInUse = 0;
    int OrderIndex;
    for(int Index = 0; Index < RECORD_ELEMENT_WEIGHT; Index++){
        if(!option[Index]){
            break;
        }
        switch(option[Index]){
            case 'i':   order[Index] = -RECORD_ELEMENT_ID;
                        if(OrderInUse & (1<<RECORD_ELEMENT_ID)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_ID;
                        break;
            case 'I':   order[Index] = RECORD_ELEMENT_ID;
                        if(OrderInUse & (1<<RECORD_ELEMENT_ID)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_ID;
                        break;
            case 'd':   order[Index] = -RECORD_ELEMENT_DOB;
                        if(OrderInUse & (1<<RECORD_ELEMENT_DOB)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_DOB;
                        break;
            case 'D':   order[Index] = RECORD_ELEMENT_DOB;
                        if(OrderInUse & (1<<RECORD_ELEMENT_DOB)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_DOB;
                        break;
            case 'h':   order[Index] = -RECORD_ELEMENT_HEIGHT;
                        if(OrderInUse & (1<<RECORD_ELEMENT_HEIGHT)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_HEIGHT;
                        break;
            case 'H':   order[Index] = RECORD_ELEMENT_HEIGHT;
                        if(OrderInUse & (1<<RECORD_ELEMENT_HEIGHT)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_HEIGHT;
                        break;
            case 'w':   order[Index] = -RECORD_ELEMENT_WEIGHT;
                        if(OrderInUse & (1<<RECORD_ELEMENT_WEIGHT)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_WEIGHT;
                        break;
            case 'W':   order[Index] = RECORD_ELEMENT_WEIGHT;
                        if(OrderInUse & (1<<RECORD_ELEMENT_WEIGHT)){
                            return false;
                        }
                        OrderInUse |= 1<<RECORD_ELEMENT_WEIGHT;
                        break;
            default:    return false;
                        break;
        }
    }
    OrderIndex = 3;
    for(int Index = RECORD_ELEMENT_WEIGHT; Index; Index--){
        if(OrderInUse & (1<<Index)){
            continue;
        }
        order[OrderIndex] = Index;
        OrderIndex--;
    }
    return true;
}

bool LoadFile(const char *datafile){
    FILE *InFile = fopen(datafile,"r");
    if(NULL == InFile){
        return false;
    }
    while(!feof(InFile)){
        int ID, DOB, Height, Width;
        if(4 == fscanf(InFile,"%d%d%d%d",&ID, &DOB, &Height, &Width)){
            InsertRecord(ID, DOB, Height, Width);
        }
    }
    fclose(InFile);
    return true;
}