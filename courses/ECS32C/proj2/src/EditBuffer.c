#include "EditBuffer.h" 	 	    		
#include <stdlib.h> 
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#define GAP_INCREMENT 16384  // amount the gap grows each time

/*
A gap buffer is one large buffer that holds a gap in the middle and all the text
on the two ends of the array. The gap begins at the cursor and moves with the
cursor. The gap shrinks when text is inserted and expands when text is
deleted. The gap buffer data structure keeps track of the gap in the middle and
the two spans at the two ends.
*/

struct STRUCT_EDIT_BUFFER_TAG {
    char *buffer_start; // address of first location in character buffer
    char *buffer_end;  // address of first location after the buffer ends 
    char *gap_start;    // address of first location in gap
    char *gap_end;     // address of first location after the gap ends
    char *cursor;
};

/* Helper functions */
static void ClearEditBuffer(SEditBufferRef ebuf){
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    ebuf->gap_start = ebuf->buffer_start;
    ebuf->gap_end = ebuf->buffer_end;
    ebuf->cursor = ebuf->gap_start;
}

static bool CopyBytes(
    SEditBufferRef ebuf,
    char *source,    
    char *destination,
    unsigned int count)
{
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    bool result = true;
    if ((destination == source) || (count == 0) ) {
        return result;
    }
    // if we're moving the character toward the front of the buffer
    if (source > destination) {
        // check to make sure that we don't go beyond the buffer
        if ((source + count) > ebuf->buffer_end) {
            result = false;
        } else {
            for (; count > 0; count--) {
                *(destination++) = *(source++);
            }
        }
    } else {
        // To prevent overwriting characters we still
        // need to move, go to the back and copy forward.
        source += count;
        destination += count;
        for (; count > 0; count--) {
            // decrement first 'cause we start one byte beyond where we want
            *(--destination) = *(--source); 
        }
    }
    return result;
}
static int SizeOfGap(SEditBufferRef ebuf) {
    return ebuf->gap_end - ebuf->gap_start;
}
static int SizeOfBuffer(SEditBufferRef ebuf) {
    return ebuf->buffer_end - ebuf->buffer_start;
}
static int CursorOffset(SEditBufferRef ebuf) {
    int offset = ebuf->cursor - ebuf->buffer_start;
    if (ebuf->cursor > ebuf->gap_end){ //
        offset -= SizeOfGap(ebuf); 
    }
    return offset;
}

static void ExpandBuffer(SEditBufferRef ebuf, int size) {
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    char *old_buffer = ebuf->buffer_start;
    ebuf->buffer_start = realloc(ebuf->buffer_start, size * sizeof(char)); 
    if (!ebuf->buffer_start) {
        fprintf(stderr, "ERROR: realloc failed");
    } else {
        int displacement = ebuf->buffer_start - old_buffer;
        ebuf->buffer_end += displacement;
        ebuf->gap_start += displacement;
        ebuf->gap_end += displacement;
        ebuf->cursor += displacement;        
    } 
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
}
/* insert a gap twice the size of the previous gap at the cursor. */
static void ExpandGap(SEditBufferRef ebuf, int size) {
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    size += GAP_INCREMENT;
    ExpandBuffer(ebuf, size);
    CopyBytes(ebuf, ebuf->gap_end, ebuf->gap_end+size,
              ebuf->buffer_end-ebuf->gap_end);
    if (ebuf->cursor > ebuf->gap_end) { 
        ebuf->cursor += size;
    }
    ebuf->gap_end += size;
    ebuf->buffer_end += size;    
}

static void MoveGapToCursor(SEditBufferRef ebuf) {
    if (ebuf->cursor == ebuf->gap_start) {
        return;
    }

    if (ebuf->cursor == ebuf->gap_end) {
        ebuf->cursor = ebuf->gap_start;
        return;
    }
    if (ebuf->cursor < ebuf->gap_start) {
        // Cursor on the left of the gap. Move the gap towards left by moving
        // the bytes between the cursor and the gap start to the right of tha
        // gap. Moves gap towards the left.
        int gap_size = SizeOfGap(ebuf);
        int bytes_count = ebuf->gap_start-ebuf->cursor;
        //Moves the cursor over by gap_size
        CopyBytes(ebuf, ebuf->cursor, ebuf->cursor+gap_size, bytes_count);
        ebuf->gap_end -= bytes_count;
        ebuf->gap_start = ebuf->cursor;
    } else {
        // Cursor on the right of the gap. Move the gap towards right by moving
        // the bytes between the cursor and the gap end to the left of the gap. 
        // Since cursor is after the gap, find the distance
        // between gap_end and cursor and that's how
        // much we move from gap_end to gap_start.
        int bytes_count = ebuf->cursor-ebuf->gap_end;
        CopyBytes(ebuf, ebuf->gap_end, ebuf->gap_start, bytes_count);
        ebuf->gap_start += bytes_count;
        ebuf->gap_end = ebuf->cursor;
        ebuf->cursor = ebuf->gap_start;
    }   
}

SEditBufferRef EditBufferCreate(int size){
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    SEditBufferRef ebuf;
    if ((ebuf = (SEditBufferRef)malloc(sizeof(SEditBuffer))) == NULL ) {
        return NULL;
    }
    ebuf->buffer_start = malloc(GAP_INCREMENT);
    if (!ebuf->buffer_start) {
        return NULL;
    }
    ebuf->cursor = ebuf->buffer_start;
    ebuf->gap_start = ebuf->buffer_start;
    ebuf->gap_end = ebuf->buffer_start + GAP_INCREMENT;  
    ebuf->buffer_end = ebuf->gap_end;
    return ebuf;
}

void EditBufferDestroy(SEditBufferRef ebuf){
    if (ebuf) {
        free(ebuf);
    }
}

size_t EditBufferSize(SEditBufferRef ebuf) {
    return SizeOfBuffer(ebuf) - SizeOfGap(ebuf);
}


size_t EditBufferMoveCursor(SEditBufferRef ebuf, int offset, int origin) {
    char *new_cursor = NULL; 
    switch(origin) {
        case EDIT_BUFFER_ORIGIN_BEGINNING:
            new_cursor = ebuf->buffer_start + offset;
        break;
        case EDIT_BUFFER_ORIGIN_CURRENT:
            new_cursor = ebuf->cursor + offset;
        break;
        case EDIT_BUFFER_ORIGIN_END:
            new_cursor = ebuf->buffer_end + offset;
        break;
        default:
        break;
    }
    if ((new_cursor < ebuf->buffer_end) && (new_cursor >= ebuf->buffer_start)){
        ebuf->cursor = new_cursor;
        if ((offset > 0) && (ebuf->cursor > ebuf->gap_start)){
            //the cursor cannot fall inside the gap
            //simply adding the gap length to the cursor to prevent the cursor from ever falling within the gap
            ebuf->cursor += SizeOfGap(ebuf);
        } else if ((offset < 0) && (ebuf->cursor < ebuf->gap_end)){
            //the cursor cannot fall inside the gap
            //simply subtracting the gap length to the cursor to prevent the cursor from ever falling within the gap
            ebuf->cursor -= SizeOfGap(ebuf);
        }      
    }
    return CursorOffset(ebuf);
}
//will insert the buf string at the begining of the buffer regardless of where the cursor is
//Load is the same as Insert when the buffer is empty
//the cleareditbuffer helper function will clear the edit buffer so that load can call clear and just call insert.
size_t EditBufferLoad(SEditBufferRef ebuf, const char *buf){
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    //editbuffer is empty before 
    int char_count = 0;
    ClearEditBuffer(ebuf);
    if (buf) {
        char_count = strlen(buf);
        EditBufferInsert(ebuf, buf, char_count);
        assert(char_count == EditBufferSize(ebuf));
        ebuf->cursor = ebuf->buffer_start;
    }
    return char_count; 
}

size_t EditBufferRead(SEditBufferRef ebuf, char *buf, size_t count) {
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    int read_index = 0;
    while ((read_index < count) && (ebuf->cursor < ebuf->buffer_end)){
        // if the cursor fall in the gap, jump over the gap. 
        if (ebuf->cursor == ebuf->gap_start) {
            //printf("in gap at read_index = %d\n", read_index);
            ebuf->cursor = ebuf->gap_end;
        }
        // By jumping over the gap, the cursor might have jumped out of the
        // buffer. If the cursor is still inside the buffer, keep reading
        if (ebuf->cursor < ebuf->buffer_end) {
            buf[read_index] = *ebuf->cursor;
            ebuf->cursor++;
            read_index++;
        }
    }     
    return read_index;
}

size_t EditBufferInsert(SEditBufferRef ebuf, const char *buf, size_t count) {
    //printf("%s @ line: %d\n",__FILE__,__LINE__);
    if (ebuf->cursor != ebuf->gap_start) {
        MoveGapToCursor(ebuf); 
    }  
    if (count > SizeOfGap(ebuf)) {
        ExpandGap(ebuf, count);
    }
    size_t length = strlen(buf);
    int idx;
    for(idx=0; (idx < count) && (idx < length); idx++) {
        *ebuf->gap_start = buf[idx];
        ebuf->gap_start++;
        ebuf->cursor += 1;        
    }
    return idx;
}

//only need to move the gap when editing, otherwise you can move cursor and not the gap everytime
//When the user edits i.e. inserts or deletes, only then will the gap move so that the cursor is alligned with the start of the gap
size_t EditBufferDelete(SEditBufferRef ebuf, size_t count) {
    //Cursor does not move after deleting count # of characters
    if (ebuf->cursor != ebuf->gap_start) {
        MoveGapToCursor(ebuf); 
    }
    // We shifted the gap so that gapend points to the location where we want to
    // start deleting so extend it to cover all the characters.
    char *new_gap_end = ebuf->gap_end + count;
    int delete_count = count;
    if (new_gap_end < ebuf->buffer_end) {
        ebuf->gap_end = new_gap_end;
    } else {
        delete_count = ebuf->buffer_end - ebuf->gap_end;
        ebuf->gap_end = ebuf->buffer_end;
    }
    return delete_count;
}
