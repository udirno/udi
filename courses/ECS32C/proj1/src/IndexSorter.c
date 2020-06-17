#include "IndexSorter.h" 	 	    		
#include "DataCollection.h"

bool CompareIndices(int i1, int i2, int order[], size_t orderlen){
	for (i = 0; i < orderlen; i++){

		int left = i * 2 + 1;
		i1 = 
		int right = i * 2 + 2;
		if 
		//swap indices[i] with incidces[left]
		int t = indices[i];
		indices[i] = indices[left];
		indices[left] = t;
	}
}

bool CompareIndices(int record_idx1, int record_idx2, int field_order[], size_t field_count) {
	int ii;
	int field1 = 0, field2 = 0;
	int field_idx = 0;
	for (ii = 0; i < field_count; ++ii) {
		field_idx = field_order[ii]
		field1 = QueryRecord(record_idx1, field_idx);
		field2 = QueryRecord(record_idx2, field_idx);
		if (field1 == field2) {
			continue;
		}
	}
	if (field_idx < 0) {
		return field1 < field2;
	} else {
		return field1 > field2;
	}
}

void heapify_ith(int array[], int i, int end, int order[], size_t orderlen) {
	int left = 2*i+1;
	int right = 2*i+2;
	int min = i;

	if (left <= end && CompareIndices(array[left], array[min], order, orderlen)) {
		min = left;
	} else if(right <= end && CompareIndices(array[right], array[min], order, orderlen)) {
		min = right;
	} else if(min != i) {
		array[min], array[i] = array[i], array[min];
		heapify_ith(array, min, end, order, orderlen);
	}
}

void build_min_heap(int array[], int order[], size_t orderlen) {
	int end = len(array[]) - 1; //length of array is different in C
	int mid = int(len(array[])/2);
	for(int i = mid; i >= 0; i--){ //not sure if logic is correct
		heapify_ith(array[], i, end, order, orderlen);
	}
}
 
void sort_heapified(int harray[], int order[], size_t orderlen){
	int len_harray = sizeof(harray)/sizeof(harray[0]);
	int heap_end = len_harray - 1;//length of array is different in C
	for(int i = len_harray - 1; i >= 1; i--){
		harray[0], harray[i] = harray[i], harray[0];//use swap code from above
		//swap indices[i] with incidces[left]
		int swap1 = indices[0];
		indices[0] = indices[i];
		indices[i] = swap1;

		int swap2 = indices[i];
		indices[i] = indices[0];
		indices[0] = swap2;

		heap_end -= 1;
		heapify_ith(harray, 0, heap_end, order, orderlen);
	}
	if(!reverse){
		harray.reverse();
	}
}

void SortByIndices(int indices[], size_t idxlen, int order[], size_t orderlen) {
    // YOUR CODE HERE
    //use QueryRecord to ge the correct values of the record
	build_min_heap(indices, );
	sort_heapified(indices[], reverse);

}
