#ifndef INDEXSORTER_H 	 	    		
#define INDEXSORTER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C"{
#endif
 
void SortByIndices(int indices[], size_t idxlen, int order[], size_t orderlen);

#ifdef __cplusplus
}
#endif

#endif
