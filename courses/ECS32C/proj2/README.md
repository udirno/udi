# Project 2: Writing an Interface to a Data Stucture

##References:
**https://www.drdobbs.com/architecture-and-design/text-editors-algorithms-and-architecture/184408975?pgno=2**

**https://github.com/lazyhacker/gapbuffer/blob/master/gap_buffer.cpp**

I used these references to help create the gap buffer data structure for my code.

##Objective 
We will implement a sequence using a data structure called ```EditBuffer```. It represents an ordered set of characters that allows characters to be inserted or deleted from arbitrary positions. The interface is in file ```include/EditBuffer.h``` and the implementation is in ```src/EditBuffer.c```.

The EditBuffer data structure is used by program ```proj2``` which takes two text files as parameters: the first file ```orig.txt``` is the original file, and the second file ```edit.txt```. The program prints the result of the edit which is redirected to file ```result.txt``` file:

```
proj2 orig.txt edit.txt > result.txt
```

The ```edit.txt``` file will edit the ```orig.txt``` by presenting the first half of the ```result.txt``` file in descending order and the second half in ascendnding order. We want the edit time to take the least amount of time possible as the .txt files get larger.

We will be using Test Driven Development to pass a series of given GoogleTest tests as efficiently as possible. The efficiency of our program will be determined by the type of data structure we use.

## Sample Session
Start by providing two text files,

```make bin/proj2``` 

```pali_orig.txt``` :

```
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
```
```pali_sml_edit.txt``` :

```
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 130 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 260 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 390 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 520 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 650 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 780 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 910 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1040 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1170 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1300 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1430 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1560 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1690 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1820 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 1950 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
+ 2080 65 "0123456789\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n"
+ 0 65 "zyxwvutsrqponmlkjihgfedcba\nZYXWVUTSRQPONMLKJIHGFEDCBA\n9876543210\n"
```
Once the program is run using the command above: 

```result.txt``` :

```
zyxwvutsrqponmlkjihgfedcba
ZYXWVUTSRQPONMLKJIHGFEDCBA
9876543210
zyxwvutsrqponmlkjihgfedcba
ZYXWVUTSRQPONMLKJIHGFEDCBA
9876543210
zyxwvutsrqponmlkjihgfedcba
ZYXWVUTSRQPONMLKJIHGFEDCBA
9876543210
zyxwvutsrqponmlkjihgfedcba
ZYXWVUTSRQPONMLKJIHGFEDCBA
9876543210
zyxwvutsrqponmlkjihgfedcba
ZYXWVUTSRQPONMLKJIHGFEDCBA
9876543210
...
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
```
Observable differences in ```result.txt```:

```pali_sml_edit.txt``` editted the first half of  ```pali_orig.txt``` so that each of the 3 lines are now ordered in descending order. Additionally, the line orders also swapped, so what was originally line 3 in the ```pali_orig.txt``` became line 1 in ```result.txt```. NOTE this only applies for the first half or ```result.txt```. The second half is simply ```pali_orig.txt``` printed repeatedly the same number of times as the first half. (not sure how the # of repetitions is calculated)

# Structure

**typedef struct STRUCT_ EDIT_ BUFFER_TAG SEditBuffer;** is the data set which holds the data values for the Edit Buffer (Gap Buffer):

```
char *buffer_start;
char *buffer_end;  
char *gap_start;    
char *gap_end;     
char *cursor;
```

### Helper Functions
**ClearEditBuffer(SEditBufferRef ebuf)** is called by the ```EditBufferLoad``` function. Load needs this function because it clears the edit buffer before calling ```EditBufferInsert```.

**CopyBytes()** copies the characters from one location of the buffer to another.It is called by ```ExpandGap``` and ```MoveGapToCursor```.

**SizeOfGap(SEditBufferRef ebuf)** returns the size of the gap.

**SizeOfBuffer(SEditBufferRef ebuf)** returns the size of the buffer.

**CursorOffset(SEditBufferRef ebuf)** calculates the offset from the beginning of the Edit Buffer is returned. Is used to return the offset in ```EditBufferMoveCursor```.

**ExpandBuffer(SEditBufferRef ebuf, int size)** checks to see if the size of the Buffer needs to be increased. Expands the size of the buffer on the tail. However, this means that everything on the right side of the gap must be shifter to the new tail end. This then leaves a block of empty space between the gap and the tail which is reserved for the gap once ```ExpandGap``` is called. **This function uses realloc to resize the previously allocated memory (by ```malloc``` without losing old data.**

**ExpandGap(SEditBufferRef ebuf, int size)** expands the size of the gap. It calls ```CopyBytes```... If the gap size needed is more than what is needed nothing changes. If it is less, both the gap and buffer are increased by ```size```. We must expand the buffer by calling ```ExpandBuffer``` first before we can expand the gap using ```CopyBytes```. This increases the size of the gap by just extending it because the contents of the buffer that were previously to the right of the gap have already been shifted over by ```ExpandBuffer```. The cursor is moved by the same ```displacement```.

**MoveGapToCursor(SEditBufferRef ebuf)** moves the gap to the current position of the cursor. The cursor should end in the same location as gap_start. The purpose of this function is because in a gap buffer when insertion is needed, the ```gap_start``` must match the cursor position.

### Main Functions

**SEditBufferRef EditBufferCreate(int size);** creates the Gap Buffer by allocating ```GAP_INCREMENT``` amount of memory and initializing each of the five data values.

**void EditBufferDestroy(SEditBufferRef ebuf);** simply frees the memory allocated for the ebuf gap buffer.

**size_t EditBufferSize(SEditBufferRef ebuf);** returns the number of characters currently in the Edit Buffer by subtracting ```SizeOfGap``` from ```SizeOfBuffer```.

**size_t EditBufferMoveCursor(SEditBufferRef ebuf, int offset, int
origin);** returns the offset of the cursor relative to the beginning of the buffer. The function takes an ```offset``` and an ```origin```. The ```origin``` is what the ```offset``` is with respect too. The switch cases give the ```origin``` three options: ```EDIT_BUFFER_ORIGIN_BEGINNING, EDIT_BUFFER_ORIGIN_CURRENT, or EDIT_BUFFER_ORIGIN_END``` which each use the offset to calculate the new position of the cursor. **The offset is the number of characters the cursor wants to move (can be negative or positive)**

**size_t EditBufferLoad(SEditBufferRef ebuf, const char * buf);** first clears the edit buffer by calling ```ClearEditBuffer``` and then calls ```EditBufferInsert``` to insert the string ```buf``` holds, and moves the cursor back to the beginning of the buffer.

**size_t EditBufferRead(SEditBufferRef ebuf, char * buf, size_t
count);** reads ```count``` number of characters from Edit Buffer into the buffer pointed to by ```buf```. The cursor starts at ```cursor offset``` and moves as characters are read. It also has to take into account the cursor falling within the gap or outside the buffer.

**size_t EditBufferInsert(SEditBufferRef ebuf, const char * buf,
size_t count);** inserts ```count``` characters at the cursor location. ```buf``` points to the specific characters that are to be inserted. The cursor moves by the number of characters inserted. In a gap buffer, you want the cursor to be at the position of the start of the gap. By calling ```MoveGapToCursor``` we move ```gap_start``` to the cursor so that characters can be inserted. **if the number of characters to be inserted is larger than the gap, then the gap must be expanded by calling ```ExpandGap```.**

**size_t EditBufferDelete(SEditBufferRef ebuf, size_t count);** deletes ```count``` characters that are following the cursor location. The cursor is not moved. If fewer characters exist after the cursor in the Edit Buffer, all of the remaining characters are removed following the cursor. The number of characters that were deleted will be returned. IMPORTANT: only need to move the gap when editing, otherwise you can move cursor and not the gap everytime. When the user edits i.e. inserts or deletes, only then will the gap move so that the cursor is alligned with the start of the gap.


