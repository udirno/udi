# Sort Records Based on Fields

We want to sort a file containing an array of records, one record per line. Each record has 4 fields: ID, Date of Birth (DoB), height, and weight. The program takes a `datafile` parameter and an optional `order` parameter 
```
proj1 datafile [order]
order - i/I ID, d/D DOB, h/H Height, w/W Weight
```
and sorts the records based on the field specified in the `order` paramter. For lowercase `order`, i.e. `i`, `d`, `h`, and `w` it sorts in descending order, and for uppercase `order`, i.e. `I`, `D`, `D`, and `W` it sorts in ascending order.

We want to use a sorting algorithm that sorts in O(n lg n) time using O(1) additional space. This rules out quicksort which takes O(n^2) time, and
mergesort which takes O(n) additional space.

## Sample Session
Syntax Error:

```
uchaudhu@ad3.ucdavis.edu@pc8:/home/cjnitta/ecs89l$ proj1
Syntax Error: proj1 datafile [order]
              order - i/I ID, d/D DOB, h/H Height, w/W Weight
``` 
Sort by ID (I = ascending, i = descending)

```
uchaudhu@ad3.ucdavis.edu@pc8:/home/cjnitta/ecs89l$ proj1 proj1data/data_sml.txt  I
1001 19691001 179 75422
1002 19701128 187 82552
1003 19720724 193 94929
1004 19870628 160 47002
1005 19810121 176 72248
1006 19600903 176 67506
1007 19710929 170 68081
1008 19860913 169 61624
1009 19800523 175 73118
1010 19980928 186 84979
1011 19941015 170 71088
1012 19750908 175 76004
1013 19751107 168 72241
1014 19630227 182 83465
1015 19961119 155 46218
1016 19960601 184 80087 
```
Sort by DOB

```
uchaudhu@ad3.ucdavis.edu@pc8:/home/cjnitta/ecs89l$ proj1 proj1data/data_sml.txt  d
1010 19980928 186 84979
1015 19961119 155 46218
1016 19960601 184 80087
1011 19941015 170 71088
1004 19870628 160 47002
1008 19860913 169 61624
1005 19810121 176 72248
1009 19800523 175 73118
1013 19751107 168 72241
1012 19750908 175 76004
1003 19720724 193 94929
1007 19710929 170 68081
1002 19701128 187 82552
1001 19691001 179 75422
1014 19630227 182 83465
1006 19600903 176 67506
```


# Structure

**Records** is the array that stores all the data of each record. So for example if there are 3 total records, then Record[0] will be the ID of the 1st record, Record[1] will be the DOB of the 1st record, Record[2] will be the height of the 1st record, Record [3] will be the weight of the 1st record, Record[4] will be the ID of the 2nd record..... etc. and Record[11] will be the weight of the 3rd record:
```[ID, DOB, Height, Weight]```

### **DataCollection.c** 
This class has 4 functions implemented to help us perform the task of sorting the records: 

**ClearRecords()** clears all the records. 

**InsertRecord()** allows you to insert a new record and returns the index. 

**RecordCount()** returns the total number of records inserted. So from the previous example RecordCount() would return 3. 

**QueryRecord** is a function that returns the value of a field from a number of records where each record contains a number of fields. It takes 2 parameters: `index` denotes the index of a record, and `element` denotes the index of the field within the record:

```
int QueryRecord(int index, int element);
``` 

Ex:
If you called QueryRecord with index of 2, and element of 3 (height):

```QueryRecord(2, RECORD_ELEMENT_HEIGHT)```

So this function will take in an index of a record (from previous example this number will be between 0,1,2) and the element will be an integer that will specify which element of that record you are looking for (so values will be between 0,1,2,3). So if you want to know the DOB of the 1st record, the parameters will be (0,1). If you want to know the weight of the 2nd record the parameters will be (1,3) and if you want to know the ID of the 3rd record the parameters will be (2,0), etc. 

If the first element in the order array is negative, i.e order[0] has a negative value, then you have to sort it in descending order. Otherwise you sort in ascending order

### **IndexSorter.c**

**SortByIndices** has 4 parameters: The **indices array**, **indices length**, **order** and **orderlength**.

```
void SortByIndices(int indices[], size_t idxlen, int order[], size_t orderlen);
```

**indices[]** stores the indices of the records. So from our previous example if we were to call SortByIndices, our indices array would simply be {0,1,2}. It does not contain the values of the elements of the records. 

**indxlen** specifies the length of the indices array, i.e. how many indices there are.

**order[]** is an array of integers which specifies the order in which the fields withing the record are compared. For example if the order given is "id" and the order array is ```{1, 3, 4, 2}``` then the Record is sorted by first comparing fields 1 (ID). If the IDs of the two records are the same, then they are compared by field 3 (Height), 4 (Weight), and 2 (DoB) respectively as we encounter additional ties. Then by field 3 (),  by ID (1). However, if there are two of the same ID's, the Record will then look at Height (3) as the next way to sort the Record. A negative number in the order[] means that that order should be sorted in descending order. 

**orderlen** specifies the length of the order array.

To get the values of the elements of the records you would have to use QueryRecord. Since the 1st parameter of the QueryRecord asks you for the index of the record, you can use the indices array, along with the order array to get the value of the element you're looking for.

