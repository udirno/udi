#include <gtest/gtest.h> 	 	    		
#include "IndexSorter.h"
#include "DataCollection.h"

TEST(DataCollectionTest, EmptyTests){
    ClearRecords();
    EXPECT_EQ(RecordCount(), 0);
    EXPECT_TRUE(0 > QueryRecord(0,RECORD_ELEMENT_ID));
    EXPECT_TRUE(0 > QueryRecord(0,RECORD_ELEMENT_DOB));
    EXPECT_TRUE(0 > QueryRecord(0,RECORD_ELEMENT_HEIGHT));
    EXPECT_TRUE(0 > QueryRecord(0,RECORD_ELEMENT_WEIGHT));
}

TEST(DataCollectionTest, InsertTests){
    ClearRecords();
    EXPECT_EQ(InsertRecord(1001,20100317,122,27216),0);
    EXPECT_EQ(QueryRecord(0,RECORD_ELEMENT_ID), 1001);
    EXPECT_EQ(QueryRecord(0,RECORD_ELEMENT_DOB), 20100317);
    EXPECT_EQ(QueryRecord(0,RECORD_ELEMENT_HEIGHT), 122);
    EXPECT_EQ(QueryRecord(0,RECORD_ELEMENT_WEIGHT), 27216);
}

int TestData[6][4] =   {{1001, 19691001, 179, 75422},
                        {1002, 19701128, 187, 82552},
                        {1003, 19720724, 193, 94929},
                        {1004, 19870628, 160, 47002},
                        {1005, 19810121, 176, 72248},
                        {1006, 19600903, 176, 67506}};

TEST(IndexSorterTest, SortDOBTests){
    int Indices[6];
    int Order[4] = {RECORD_ELEMENT_DOB, RECORD_ELEMENT_HEIGHT, RECORD_ELEMENT_WEIGHT, RECORD_ELEMENT_ID};
    
    ClearRecords();
    for(int Index = 0; Index < 6; Index++){
        EXPECT_EQ(InsertRecord(TestData[Index][0],TestData[Index][1],TestData[Index][2],TestData[Index][3]),Index);
        Indices[Index] = Index;
    }
    SortByIndices(Indices, 6, Order, 4);
    for(int Index = 0; Index < 5; Index++){
        EXPECT_TRUE(QueryRecord(Indices[Index],RECORD_ELEMENT_DOB) <= QueryRecord(Indices[Index+1],RECORD_ELEMENT_DOB));
    }
}

TEST(IndexSorterTest, SortHeightTests){
    int Indices[6];
    int Order[4] = {RECORD_ELEMENT_HEIGHT, RECORD_ELEMENT_WEIGHT, RECORD_ELEMENT_DOB, RECORD_ELEMENT_ID};
    
    ClearRecords();
    for(int Index = 0; Index < 6; Index++){
        EXPECT_EQ(InsertRecord(TestData[Index][0],TestData[Index][1],TestData[Index][2],TestData[Index][3]),Index);
        Indices[Index] = Index;
    }
    SortByIndices(Indices, 6, Order, 4);
    for(int Index = 0; Index < 5; Index++){
        EXPECT_TRUE(QueryRecord(Indices[Index],RECORD_ELEMENT_HEIGHT) <= QueryRecord(Indices[Index+1],RECORD_ELEMENT_HEIGHT));
    }
}

TEST(IndexSorterTest, SortWeightTests){
    int Indices[6];
    int Order[4] = {RECORD_ELEMENT_WEIGHT, RECORD_ELEMENT_DOB, RECORD_ELEMENT_HEIGHT, RECORD_ELEMENT_ID};
    
    ClearRecords();
    for(int Index = 0; Index < 6; Index++){
        EXPECT_EQ(InsertRecord(TestData[Index][0],TestData[Index][1],TestData[Index][2],TestData[Index][3]),Index);
        Indices[Index] = Index;
    }
    SortByIndices(Indices, 6, Order, 4);
    for(int Index = 0; Index < 5; Index++){
        EXPECT_TRUE(QueryRecord(Indices[Index],RECORD_ELEMENT_WEIGHT) <= QueryRecord(Indices[Index+1],RECORD_ELEMENT_WEIGHT));
    }
}

TEST(IndexSorterTest, SortReverseIDTests){
    int Indices[6];
    int Order[4] = {-RECORD_ELEMENT_ID, RECORD_ELEMENT_WEIGHT, RECORD_ELEMENT_DOB, RECORD_ELEMENT_HEIGHT};
    
    ClearRecords();
    for(int Index = 0; Index < 6; Index++){
        EXPECT_EQ(InsertRecord(TestData[Index][0],TestData[Index][1],TestData[Index][2],TestData[Index][3]),Index);
        Indices[Index] = Index;
    }
    SortByIndices(Indices, 6, Order, 4);
    for(int Index = 0; Index < 5; Index++){
        EXPECT_TRUE(QueryRecord(Indices[Index],RECORD_ELEMENT_ID) >= QueryRecord(Indices[Index+1],RECORD_ELEMENT_ID));
    }
}
