from .clib import core
from ctypes import c_int, c_uint, c_ulong, c_double, c_void_p

# ------------------------------------------------------------------------ #
#             P Y T H O N   W R A P E R   O F   l i b B b M m
#
# - generated with bin/c-to-py.py
# - c-header : bbmm.h
# 
#        /!\ ANY MODIFICATION IN THIS FILE WILL BE ERASED /!\
# ------------------------------------------------------------------------ #


# BmCode* newBmCode( uint size );
newBmCode= core.newBmCode
newBmCode.restype= c_void_p
newBmCode.argtypes= [c_uint]

# BmCode* newBmCode_numbers( uint size, uint* numbers );
newBmCode_numbers= core.newBmCode_numbers
newBmCode_numbers.restype= c_void_p
newBmCode_numbers.argtypes= [c_uint, c_void_p]

# BmCode* newBmCode_all( uint size, uint defaultValue );
newBmCode_all= core.newBmCode_all
newBmCode_all.restype= c_void_p
newBmCode_all.argtypes= [c_uint, c_uint]

# BmCode* newBmCodeAs( BmCode* model );
newBmCodeAs= core.newBmCodeAs
newBmCodeAs.restype= c_void_p
newBmCodeAs.argtypes= [c_void_p]

# BmCode* BmCode_create( BmCode* self, uint size );
BmCode_create= core.BmCode_create
BmCode_create.restype= c_void_p
BmCode_create.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_create_numbers( BmCode* self, uint size, uint* numbers );
BmCode_create_numbers= core.BmCode_create_numbers
BmCode_create_numbers.restype= c_void_p
BmCode_create_numbers.argtypes= [c_void_p, c_uint, c_void_p]

# BmCode* BmCode_create_all( BmCode* self, uint size, uint defaultValue );
BmCode_create_all= core.BmCode_create_all
BmCode_create_all.restype= c_void_p
BmCode_create_all.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_createAs( BmCode* self, BmCode* model );
BmCode_createAs= core.BmCode_createAs
BmCode_createAs.restype= c_void_p
BmCode_createAs.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_createMerge( BmCode* self, uint numberOfCodes, BmCode ** codes );
BmCode_createMerge= core.BmCode_createMerge
BmCode_createMerge.restype= c_void_p
BmCode_createMerge.argtypes= [c_void_p, c_uint, c_void_p]

# void deleteBmCode( BmCode* instance );
deleteBmCode= core.deleteBmCode
deleteBmCode.restype= c_void_p
deleteBmCode.argtypes= [c_void_p]

# BmCode* BmCode_destroy( BmCode* self );
BmCode_destroy= core.BmCode_destroy
BmCode_destroy.restype= c_void_p
BmCode_destroy.argtypes= [c_void_p]

# uint BmCode_dimention( BmCode* self );
BmCode_dimention= core.BmCode_dimention
BmCode_dimention.restype= c_uint
BmCode_dimention.argtypes= [c_void_p]

# uint* BmCode_numbers( BmCode* self );
BmCode_numbers= core.BmCode_numbers
BmCode_numbers.restype= c_void_p
BmCode_numbers.argtypes= [c_void_p]

# uint BmCode_at( BmCode* self, uint index );
BmCode_at= core.BmCode_at
BmCode_at.restype= c_uint
BmCode_at.argtypes= [c_void_p, c_uint]

# uint BmCode_count( BmCode* self, uint value );
BmCode_count= core.BmCode_count
BmCode_count.restype= c_uint
BmCode_count.argtypes= [c_void_p, c_uint]

# ulong BmCode_sum( BmCode* self );
BmCode_sum= core.BmCode_sum
BmCode_sum.restype= c_ulong
BmCode_sum.argtypes= [c_void_p]

# ulong BmCode_product( BmCode* self );
BmCode_product= core.BmCode_product
BmCode_product.restype= c_ulong
BmCode_product.argtypes= [c_void_p]

# BmCode* BmCode_reinit( BmCode* self, uint newSize );
BmCode_reinit= core.BmCode_reinit
BmCode_reinit.restype= c_void_p
BmCode_reinit.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_copy( BmCode* self, BmCode* model );
BmCode_copy= core.BmCode_copy
BmCode_copy.restype= c_void_p
BmCode_copy.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_copyNumbers( BmCode* self, BmCode* model );
BmCode_copyNumbers= core.BmCode_copyNumbers
BmCode_copyNumbers.restype= c_void_p
BmCode_copyNumbers.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_redimention( BmCode* self, uint newSize );
BmCode_redimention= core.BmCode_redimention
BmCode_redimention.restype= c_void_p
BmCode_redimention.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_setAll( BmCode* self, uint value );
BmCode_setAll= core.BmCode_setAll
BmCode_setAll.restype= c_void_p
BmCode_setAll.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_at_set( BmCode* self, uint index, uint value );
BmCode_at_set= core.BmCode_at_set
BmCode_at_set.restype= c_void_p
BmCode_at_set.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_at_increment( BmCode* self, uint index, uint value );
BmCode_at_increment= core.BmCode_at_increment
BmCode_at_increment.restype= c_void_p
BmCode_at_increment.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_at_decrement( BmCode* self, uint index, uint value );
BmCode_at_decrement= core.BmCode_at_decrement
BmCode_at_decrement.restype= c_void_p
BmCode_at_decrement.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_setNumbers( BmCode* self, uint* numbers );
BmCode_setNumbers= core.BmCode_setNumbers
BmCode_setNumbers.restype= c_void_p
BmCode_setNumbers.argtypes= [c_void_p, c_void_p]

# void BmCode_sort( BmCode* self );
BmCode_sort= core.BmCode_sort
BmCode_sort.restype= c_void_p
BmCode_sort.argtypes= [c_void_p]

# void BmCode_switch( BmCode* self, BmCode* anotherCode );
BmCode_switch= core.BmCode_switch
BmCode_switch.restype= c_void_p
BmCode_switch.argtypes= [c_void_p, c_void_p]

# uint BmCode_search( BmCode* self, uint value );
BmCode_search= core.BmCode_search
BmCode_search.restype= c_uint
BmCode_search.argtypes= [c_void_p, c_uint]

# bool BmCode_isEqualTo( BmCode* self, BmCode* another );
BmCode_isEqualTo= core.BmCode_isEqualTo
BmCode_isEqualTo.restype= c_int
BmCode_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmCode_isGreaterThan( BmCode* self, BmCode* another );
BmCode_isGreaterThan= core.BmCode_isGreaterThan
BmCode_isGreaterThan.restype= c_int
BmCode_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmCode_isSmallerThan( BmCode* self, BmCode* another );
BmCode_isSmallerThan= core.BmCode_isSmallerThan
BmCode_isSmallerThan.restype= c_int
BmCode_isSmallerThan.argtypes= [c_void_p, c_void_p]

# ulong BmCode_keyOf( BmCode* self, BmCode* code );
BmCode_keyOf= core.BmCode_keyOf
BmCode_keyOf.restype= c_ulong
BmCode_keyOf.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCode_onKey( BmCode* self, BmCode* configuration, ulong key );
BmCode_setCode_onKey= core.BmCode_setCode_onKey
BmCode_setCode_onKey.restype= c_void_p
BmCode_setCode_onKey.argtypes= [c_void_p, c_void_p, c_ulong]

# BmCode* BmCode_setCodeFirst( BmCode* self, BmCode* configuration );
BmCode_setCodeFirst= core.BmCode_setCodeFirst
BmCode_setCodeFirst.restype= c_void_p
BmCode_setCodeFirst.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCodeLast( BmCode* self, BmCode* configuration );
BmCode_setCodeLast= core.BmCode_setCodeLast
BmCode_setCodeLast.restype= c_void_p
BmCode_setCodeLast.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeOnKey( BmCode* self, ulong key );
BmCode_newBmCodeOnKey= core.BmCode_newBmCodeOnKey
BmCode_newBmCodeOnKey.restype= c_void_p
BmCode_newBmCodeOnKey.argtypes= [c_void_p, c_ulong]

# BmCode* BmCode_newBmCodeFirst( BmCode* self );
BmCode_newBmCodeFirst= core.BmCode_newBmCodeFirst
BmCode_newBmCodeFirst.restype= c_void_p
BmCode_newBmCodeFirst.argtypes= [c_void_p]

# BmCode* BmCode_newBmCodeLast( BmCode* self );
BmCode_newBmCodeLast= core.BmCode_newBmCodeLast
BmCode_newBmCodeLast.restype= c_void_p
BmCode_newBmCodeLast.argtypes= [c_void_p]

# BmCode* BmCode_nextCode( BmCode* self, BmCode* configuration );
BmCode_nextCode= core.BmCode_nextCode
BmCode_nextCode.restype= c_void_p
BmCode_nextCode.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_previousCode( BmCode* self, BmCode* configuration );
BmCode_previousCode= core.BmCode_previousCode
BmCode_previousCode.restype= c_void_p
BmCode_previousCode.argtypes= [c_void_p, c_void_p]

# bool BmCode_isIncluding( BmCode* self, BmCode* configuration );
BmCode_isIncluding= core.BmCode_isIncluding
BmCode_isIncluding.restype= c_int
BmCode_isIncluding.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeMask( BmCode* self, BmCode* mask );
BmCode_newBmCodeMask= core.BmCode_newBmCodeMask
BmCode_newBmCodeMask.restype= c_void_p
BmCode_newBmCodeMask.argtypes= [c_void_p, c_void_p]

# char* BmCode_print( BmCode* self, char* buffer );
BmCode_print= core.BmCode_print
BmCode_print.restype= c_void_p
BmCode_print.argtypes= [c_void_p, c_void_p]

# BmVector* newBmVector( uint size );
newBmVector= core.newBmVector
newBmVector.restype= c_void_p
newBmVector.argtypes= [c_uint]

# BmVector* newBmVector_values( uint size, double* values );
newBmVector_values= core.newBmVector_values
newBmVector_values.restype= c_void_p
newBmVector_values.argtypes= [c_uint, c_void_p]

# BmVector* newBmVector_all( uint size, double value );
newBmVector_all= core.newBmVector_all
newBmVector_all.restype= c_void_p
newBmVector_all.argtypes= [c_uint, c_double]

# BmVector* BmVector_create( BmVector* self, uint size );
BmVector_create= core.BmVector_create
BmVector_create.restype= c_void_p
BmVector_create.argtypes= [c_void_p, c_uint]

# BmVector* BmVector_create_values( BmVector* self, uint size, double* values );
BmVector_create_values= core.BmVector_create_values
BmVector_create_values.restype= c_void_p
BmVector_create_values.argtypes= [c_void_p, c_uint, c_void_p]

# BmVector* BmVector_create_all( BmVector* self, uint size, double value );
BmVector_create_all= core.BmVector_create_all
BmVector_create_all.restype= c_void_p
BmVector_create_all.argtypes= [c_void_p, c_uint, c_double]

# BmVector* BmVector_destroy( BmVector* self );
BmVector_destroy= core.BmVector_destroy
BmVector_destroy.restype= c_void_p
BmVector_destroy.argtypes= [c_void_p]

# void deleteBmVector( BmVector* self );
deleteBmVector= core.deleteBmVector
deleteBmVector.restype= c_void_p
deleteBmVector.argtypes= [c_void_p]

# BmVector* BmVector_reinit( BmVector* self, uint newSize );
BmVector_reinit= core.BmVector_reinit
BmVector_reinit.restype= c_void_p
BmVector_reinit.argtypes= [c_void_p, c_uint]

# BmVector* BmVector_copy( BmVector* self, BmVector* model );
BmVector_copy= core.BmVector_copy
BmVector_copy.restype= c_void_p
BmVector_copy.argtypes= [c_void_p, c_void_p]

# uint BmVector_dimention( BmVector* self );
BmVector_dimention= core.BmVector_dimention
BmVector_dimention.restype= c_uint
BmVector_dimention.argtypes= [c_void_p]

# double BmVector_at( BmVector* self, uint i );
BmVector_at= core.BmVector_at
BmVector_at.restype= c_double
BmVector_at.argtypes= [c_void_p, c_uint]

# double* BmVector_values( BmVector* self );
BmVector_values= core.BmVector_values
BmVector_values.restype= c_void_p
BmVector_values.argtypes= [c_void_p]

# BmVector* BmVector_redimention( BmVector* self, uint size );
BmVector_redimention= core.BmVector_redimention
BmVector_redimention.restype= c_void_p
BmVector_redimention.argtypes= [c_void_p, c_uint]

# double BmVector_at_set( BmVector* self, uint i, double value );
BmVector_at_set= core.BmVector_at_set
BmVector_at_set.restype= c_double
BmVector_at_set.argtypes= [c_void_p, c_uint, c_double]

# BmVector* BmVector_setValues( BmVector* self, double* values );
BmVector_setValues= core.BmVector_setValues
BmVector_setValues.restype= c_void_p
BmVector_setValues.argtypes= [c_void_p, c_void_p]

# double BmVector_sum( BmVector* self );
BmVector_sum= core.BmVector_sum
BmVector_sum.restype= c_double
BmVector_sum.argtypes= [c_void_p]

# double BmVector_product( BmVector* self );
BmVector_product= core.BmVector_product
BmVector_product.restype= c_double
BmVector_product.argtypes= [c_void_p]

# bool BmVector_isEqualTo( BmVector* self, BmVector* another );
BmVector_isEqualTo= core.BmVector_isEqualTo
BmVector_isEqualTo.restype= c_int
BmVector_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmVector_isGreaterThan( BmVector* self, BmVector* another );
BmVector_isGreaterThan= core.BmVector_isGreaterThan
BmVector_isGreaterThan.restype= c_int
BmVector_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmVector_isSmallerThan( BmVector* self, BmVector* another );
BmVector_isSmallerThan= core.BmVector_isSmallerThan
BmVector_isSmallerThan.restype= c_int
BmVector_isSmallerThan.argtypes= [c_void_p, c_void_p]

# char* BmVector_print( BmVector* self, char* output );
BmVector_print= core.BmVector_print
BmVector_print.restype= c_void_p
BmVector_print.argtypes= [c_void_p, c_void_p]

# char* BmVector_format_print( BmVector* self, char* format, char* buffer );
BmVector_format_print= core.BmVector_format_print
BmVector_format_print.restype= c_void_p
BmVector_format_print.argtypes= [c_void_p, c_void_p, c_void_p]

# BmBench* newBmBench( uint capacity );
newBmBench= core.newBmBench
newBmBench.restype= c_void_p
newBmBench.argtypes= [c_uint]

# BmBench* newBmBenchWith( uint capacity, BmCode* newFirstItems, double value );
newBmBenchWith= core.newBmBenchWith
newBmBenchWith.restype= c_void_p
newBmBenchWith.argtypes= [c_uint, c_void_p, c_double]

# BmBench* newBmBenchAs( BmBench* model );
newBmBenchAs= core.newBmBenchAs
newBmBenchAs.restype= c_void_p
newBmBenchAs.argtypes= [c_void_p]

# BmBench* BmBench_create( BmBench* self, uint capacity );
BmBench_create= core.BmBench_create
BmBench_create.restype= c_void_p
BmBench_create.argtypes= [c_void_p, c_uint]

# BmBench* BmBench_createWith( BmBench* self, uint capacity, BmCode* newFirstItems, double value );
BmBench_createWith= core.BmBench_createWith
BmBench_createWith.restype= c_void_p
BmBench_createWith.argtypes= [c_void_p, c_uint, c_void_p, c_double]

# BmBench* BmBench_createAs( BmBench* self, BmBench* model );
BmBench_createAs= core.BmBench_createAs
BmBench_createAs.restype= c_void_p
BmBench_createAs.argtypes= [c_void_p, c_void_p]

# BmBench* BmBench_destroy( BmBench* self );
BmBench_destroy= core.BmBench_destroy
BmBench_destroy.restype= c_void_p
BmBench_destroy.argtypes= [c_void_p]

# void deleteBmBench( BmBench* self );
deleteBmBench= core.deleteBmBench
deleteBmBench.restype= c_void_p
deleteBmBench.argtypes= [c_void_p]

# BmBench* BmBench_reinit( BmBench* self, uint capacity );
BmBench_reinit= core.BmBench_reinit
BmBench_reinit.restype= c_void_p
BmBench_reinit.argtypes= [c_void_p, c_uint]

# uint BmBench_size( BmBench* self );
BmBench_size= core.BmBench_size
BmBench_size.restype= c_uint
BmBench_size.argtypes= [c_void_p]

# uint BmBench_capacity( BmBench* self );
BmBench_capacity= core.BmBench_capacity
BmBench_capacity.restype= c_uint
BmBench_capacity.argtypes= [c_void_p]

# BmCode* BmBench_at( BmBench* self, uint i );
BmBench_at= core.BmBench_at
BmBench_at.restype= c_void_p
BmBench_at.argtypes= [c_void_p, c_uint]

# double BmBench_valueAt( BmBench* self, uint i );
BmBench_valueAt= core.BmBench_valueAt
BmBench_valueAt.restype= c_double
BmBench_valueAt.argtypes= [c_void_p, c_uint]

# uint BmBench_dimention( BmBench* self );
BmBench_dimention= core.BmBench_dimention
BmBench_dimention.restype= c_uint
BmBench_dimention.argtypes= [c_void_p]

# void BmBench_resizeCapacity( BmBench* self, uint newCapacity );
BmBench_resizeCapacity= core.BmBench_resizeCapacity
BmBench_resizeCapacity.restype= c_void_p
BmBench_resizeCapacity.argtypes= [c_void_p, c_uint]

# uint BmBench_attach( BmBench* self, BmCode* newItem );
BmBench_attach= core.BmBench_attach
BmBench_attach.restype= c_uint
BmBench_attach.argtypes= [c_void_p, c_void_p]

# uint BmBench_attachLast( BmBench* self, BmCode* newItem, double value );
BmBench_attachLast= core.BmBench_attachLast
BmBench_attachLast.restype= c_uint
BmBench_attachLast.argtypes= [c_void_p, c_void_p, c_double]

# BmCode* BmBench_detachLast( BmBench* self );
BmBench_detachLast= core.BmBench_detachLast
BmBench_detachLast.restype= c_void_p
BmBench_detachLast.argtypes= [c_void_p]

# uint BmBench_attachFirst( BmBench* self, BmCode* newItem, double value );
BmBench_attachFirst= core.BmBench_attachFirst
BmBench_attachFirst.restype= c_uint
BmBench_attachFirst.argtypes= [c_void_p, c_void_p, c_double]

# BmCode* BmBench_detachFirst( BmBench* self );
BmBench_detachFirst= core.BmBench_detachFirst
BmBench_detachFirst.restype= c_void_p
BmBench_detachFirst.argtypes= [c_void_p]

# BmCode* BmBench_at_setValue( BmBench* self, uint i, double value );
BmBench_at_setValue= core.BmBench_at_setValue
BmBench_at_setValue.restype= c_void_p
BmBench_at_setValue.argtypes= [c_void_p, c_uint, c_double]

# void BmBench_switch( BmBench* self, BmBench* doppleganger );
BmBench_switch= core.BmBench_switch
BmBench_switch.restype= c_void_p
BmBench_switch.argtypes= [c_void_p, c_void_p]

# void BmBench_add_reducted( BmBench* self, BmBench* another, BmCode* mask );
BmBench_add_reducted= core.BmBench_add_reducted
BmBench_add_reducted.restype= c_void_p
BmBench_add_reducted.argtypes= [c_void_p, c_void_p, c_void_p]

# uint BmBench_sort( BmBench* self, fctptr_BmBench_compare compare );
BmBench_sort= core.BmBench_sort
BmBench_sort.restype= c_uint
BmBench_sort.argtypes= [c_void_p, c_void_p]

# uint BmBench_switchCodes( BmBench* self, uint id1, uint id2 );
BmBench_switchCodes= core.BmBench_switchCodes
BmBench_switchCodes.restype= c_uint
BmBench_switchCodes.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isGreater( BmBench* self, uint i1, uint i2 );
BmBench_isGreater= core.BmBench_isGreater
BmBench_isGreater.restype= c_int
BmBench_isGreater.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isSmaller( BmBench* self, uint i1, uint i2 );
BmBench_isSmaller= core.BmBench_isSmaller
BmBench_isSmaller.restype= c_int
BmBench_isSmaller.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isGreaterValue( BmBench* self, uint i1, uint i2 );
BmBench_isGreaterValue= core.BmBench_isGreaterValue
BmBench_isGreaterValue.restype= c_int
BmBench_isGreaterValue.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isSmallerValue( BmBench* self, uint i1, uint i2 );
BmBench_isSmallerValue= core.BmBench_isSmallerValue
BmBench_isSmallerValue.restype= c_int
BmBench_isSmallerValue.argtypes= [c_void_p, c_uint, c_uint]

# char* BmBench_print( BmBench* self, char* output );
BmBench_print= core.BmBench_print
BmBench_print.restype= c_void_p
BmBench_print.argtypes= [c_void_p, c_void_p]

# char* BmBench_printCodes( BmBench* self, char* output );
BmBench_printCodes= core.BmBench_printCodes
BmBench_printCodes.restype= c_void_p
BmBench_printCodes.argtypes= [c_void_p, c_void_p]

# char* BmBench_printNetwork( BmBench* self, char* output );
BmBench_printNetwork= core.BmBench_printNetwork
BmBench_printNetwork.restype= c_void_p
BmBench_printNetwork.argtypes= [c_void_p, c_void_p]

# BmTree* newBmTree( uint binarySpaceSize, uint optionSize );
newBmTree= core.newBmTree
newBmTree.restype= c_void_p
newBmTree.argtypes= [c_uint, c_uint]

# BmTree* newBmTreeWith( BmCode* newSpace, uint optionSize );
newBmTreeWith= core.newBmTreeWith
newBmTreeWith.restype= c_void_p
newBmTreeWith.argtypes= [c_void_p, c_uint]

# BmTree* BmTree_createWhith( BmTree* self, BmCode* input, uint optionSize );
BmTree_createWhith= core.BmTree_createWhith
BmTree_createWhith.restype= c_void_p
BmTree_createWhith.argtypes= [c_void_p, c_void_p, c_uint]

# BmTree* BmTree_destroy( BmTree* self );
BmTree_destroy= core.BmTree_destroy
BmTree_destroy.restype= c_void_p
BmTree_destroy.argtypes= [c_void_p]

# void deleteBmTree( BmTree* self );
deleteBmTree= core.deleteBmTree
deleteBmTree.restype= c_void_p
deleteBmTree.argtypes= [c_void_p]

# BmTree* BmTree_reinitWith( BmTree* self, BmCode* newSpace, uint optionSize );
BmTree_reinitWith= core.BmTree_reinitWith
BmTree_reinitWith.restype= c_void_p
BmTree_reinitWith.argtypes= [c_void_p, c_void_p, c_uint]

# BmTree* BmTree_clearWhith_on( BmTree* self, uint index, uint defaultOption );
BmTree_clearWhith_on= core.BmTree_clearWhith_on
BmTree_clearWhith_on.restype= c_void_p
BmTree_clearWhith_on.argtypes= [c_void_p, c_uint, c_uint]

# BmTree* BmTree_clearOn( BmTree* self, uint defaultOption );
BmTree_clearOn= core.BmTree_clearOn
BmTree_clearOn.restype= c_void_p
BmTree_clearOn.argtypes= [c_void_p, c_uint]

# uint BmTree_size( BmTree* self );
BmTree_size= core.BmTree_size
BmTree_size.restype= c_uint
BmTree_size.argtypes= [c_void_p]

# BmCode* BmTree_inputSpace( BmTree* self );
BmTree_inputSpace= core.BmTree_inputSpace
BmTree_inputSpace.restype= c_void_p
BmTree_inputSpace.argtypes= [c_void_p]

# uint BmTree_outputSize( BmTree* self );
BmTree_outputSize= core.BmTree_outputSize
BmTree_outputSize.restype= c_uint
BmTree_outputSize.argtypes= [c_void_p]

# uint BmTree_at( BmTree* self, BmCode* code );
BmTree_at= core.BmTree_at
BmTree_at.restype= c_uint
BmTree_at.argtypes= [c_void_p, c_void_p]

# double BmTree_at_value( BmTree* self, BmCode* code );
BmTree_at_value= core.BmTree_at_value
BmTree_at_value.restype= c_double
BmTree_at_value.argtypes= [c_void_p, c_void_p]

# void BmTree_reziseCapacity( BmTree* self, uint newCapacity );
BmTree_reziseCapacity= core.BmTree_reziseCapacity
BmTree_reziseCapacity.restype= c_void_p
BmTree_reziseCapacity.argtypes= [c_void_p, c_uint]

# void BmTree_reziseCompleteCapacity( BmTree* self );
BmTree_reziseCompleteCapacity= core.BmTree_reziseCompleteCapacity
BmTree_reziseCompleteCapacity.restype= c_void_p
BmTree_reziseCompleteCapacity.argtypes= [c_void_p]

# void BmTree_option_setValue( BmTree* self, uint iOption, double value );
BmTree_option_setValue= core.BmTree_option_setValue
BmTree_option_setValue.restype= c_void_p
BmTree_option_setValue.argtypes= [c_void_p, c_uint, c_double]

# uint BmTree_at_set( BmTree* self, BmCode* code, uint output );
BmTree_at_set= core.BmTree_at_set
BmTree_at_set.restype= c_uint
BmTree_at_set.argtypes= [c_void_p, c_void_p, c_uint]

# uint BmTree_at_readOrder_set( BmTree* self, BmCode* code, BmCode* codeOrder, uint output );
BmTree_at_readOrder_set= core.BmTree_at_readOrder_set
BmTree_at_readOrder_set.restype= c_uint
BmTree_at_readOrder_set.argtypes= [c_void_p, c_void_p, c_void_p, c_uint]

# uint BmTree_branchSize( BmTree* self, uint iBranch );
BmTree_branchSize= core.BmTree_branchSize
BmTree_branchSize.restype= c_uint
BmTree_branchSize.argtypes= [c_void_p, c_uint]

# uint BmTree_branch_state( BmTree* self, uint iBranch, uint state );
BmTree_branch_state= core.BmTree_branch_state
BmTree_branch_state.restype= c_uint
BmTree_branch_state.argtypes= [c_void_p, c_uint, c_uint]

# uint BmTree_branchVariable( BmTree* self, uint iBranch );
BmTree_branchVariable= core.BmTree_branchVariable
BmTree_branchVariable.restype= c_uint
BmTree_branchVariable.argtypes= [c_void_p, c_uint]

# uint BmTree_branchNumberOfOutputs( BmTree* self, uint branch );
BmTree_branchNumberOfOutputs= core.BmTree_branchNumberOfOutputs
BmTree_branchNumberOfOutputs.restype= c_uint
BmTree_branchNumberOfOutputs.argtypes= [c_void_p, c_uint]

# uint BmTree_deepOf( BmTree* self, BmCode* code );
BmTree_deepOf= core.BmTree_deepOf
BmTree_deepOf.restype= c_uint
BmTree_deepOf.argtypes= [c_void_p, c_void_p]

# uint BmTree_newBranch( BmTree* self, uint iVariable, uint defaultOption );
BmTree_newBranch= core.BmTree_newBranch
BmTree_newBranch.restype= c_uint
BmTree_newBranch.argtypes= [c_void_p, c_uint, c_uint]

# void BmTree_branch_state_connect( BmTree* self, uint branchA, uint stateA, uint branchB );
BmTree_branch_state_connect= core.BmTree_branch_state_connect
BmTree_branch_state_connect.restype= c_void_p
BmTree_branch_state_connect.argtypes= [c_void_p, c_uint, c_uint, c_uint]

# void BmTree_branch_state_set( BmTree* self, uint branchA, uint iState, uint outbut );
BmTree_branch_state_set= core.BmTree_branch_state_set
BmTree_branch_state_set.restype= c_void_p
BmTree_branch_state_set.argtypes= [c_void_p, c_uint, c_uint, c_uint]

# uint BmTree_cleanDeadBranches( BmTree* self );
BmTree_cleanDeadBranches= core.BmTree_cleanDeadBranches
BmTree_cleanDeadBranches.restype= c_uint
BmTree_cleanDeadBranches.argtypes= [c_void_p]

# uint BmTree_removeBranch( BmTree* self, uint iBranch );
BmTree_removeBranch= core.BmTree_removeBranch
BmTree_removeBranch.restype= c_uint
BmTree_removeBranch.argtypes= [c_void_p, c_uint]

# BmBench* BmTree_asNewBench( BmTree* self );
BmTree_asNewBench= core.BmTree_asNewBench
BmTree_asNewBench.restype= c_void_p
BmTree_asNewBench.argtypes= [c_void_p]

# void BmTree_fromBench( BmTree* self, BmBench* model );
BmTree_fromBench= core.BmTree_fromBench
BmTree_fromBench.restype= c_void_p
BmTree_fromBench.argtypes= [c_void_p, c_void_p]

# char* BmTree_printBranch( BmTree* self, uint iBranch, char* output );
BmTree_printBranch= core.BmTree_printBranch
BmTree_printBranch.restype= c_void_p
BmTree_printBranch.argtypes= [c_void_p, c_uint, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_print_sep( BmTree* self, char* output, char* separator );
BmTree_print_sep= core.BmTree_print_sep
BmTree_print_sep.restype= c_void_p
BmTree_print_sep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmTree_print_sep_options( BmTree* self, char* output, char* separator, char** optionStrs );
BmTree_print_sep_options= core.BmTree_print_sep_options
BmTree_print_sep_options.restype= c_void_p
BmTree_print_sep_options.argtypes= [c_void_p, c_void_p, c_void_p, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_printInside( BmTree* self, char* output );
BmTree_printInside= core.BmTree_printInside
BmTree_printInside.restype= c_void_p
BmTree_printInside.argtypes= [c_void_p, c_void_p]

# BmCondition* newBmConditionBasic( uint domain );
newBmConditionBasic= core.newBmConditionBasic
newBmConditionBasic.restype= c_void_p
newBmConditionBasic.argtypes= [c_uint]

# BmCondition* newBmConditionWith( uint domain, BmCode* newParentRanges, BmBench* newDefaultDistrib );
newBmConditionWith= core.newBmConditionWith
newBmConditionWith.restype= c_void_p
newBmConditionWith.argtypes= [c_uint, c_void_p, c_void_p]

# BmCondition* BmCondition_createBasic( BmCondition* self, uint domain );
BmCondition_createBasic= core.BmCondition_createBasic
BmCondition_createBasic.restype= c_void_p
BmCondition_createBasic.argtypes= [c_void_p, c_uint]

# BmCondition* BmCondition_createWith( BmCondition* self, uint domain, BmCode* newParentRanges, BmBench* newDefaultDistrib );
BmCondition_createWith= core.BmCondition_createWith
BmCondition_createWith.restype= c_void_p
BmCondition_createWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# BmCondition* BmCondition_destroy( BmCondition* self );
BmCondition_destroy= core.BmCondition_destroy
BmCondition_destroy.restype= c_void_p
BmCondition_destroy.argtypes= [c_void_p]

# void deleteBmCondition( BmCondition* instance );
deleteBmCondition= core.deleteBmCondition
deleteBmCondition.restype= c_void_p
deleteBmCondition.argtypes= [c_void_p]

# uint BmCondition_reinitWith( BmCondition* self, uint domain, BmCode* newParents, BmBench* newDistrib );
BmCondition_reinitWith= core.BmCondition_reinitWith
BmCondition_reinitWith.restype= c_uint
BmCondition_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# uint BmCondition_reinitDistributionsWith( BmCondition* self, BmBench* newDistrib );
BmCondition_reinitDistributionsWith= core.BmCondition_reinitDistributionsWith
BmCondition_reinitDistributionsWith.restype= c_uint
BmCondition_reinitDistributionsWith.argtypes= [c_void_p, c_void_p]

# uint BmCondition_domain( BmCondition* self );
BmCondition_domain= core.BmCondition_domain
BmCondition_domain.restype= c_uint
BmCondition_domain.argtypes= [c_void_p]

# BmCode* BmCondition_parents( BmCondition* self );
BmCondition_parents= core.BmCondition_parents
BmCondition_parents.restype= c_void_p
BmCondition_parents.argtypes= [c_void_p]

# BmBench* BmCondition_from( BmCondition* self, BmCode* configuration );
BmCondition_from= core.BmCondition_from
BmCondition_from.restype= c_void_p
BmCondition_from.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_fromKey( BmCondition* self, uint configKey );
BmCondition_fromKey= core.BmCondition_fromKey
BmCondition_fromKey.restype= c_void_p
BmCondition_fromKey.argtypes= [c_void_p, c_uint]

# uint BmCondition_distributionSize( BmCondition* self );
BmCondition_distributionSize= core.BmCondition_distributionSize
BmCondition_distributionSize.restype= c_uint
BmCondition_distributionSize.argtypes= [c_void_p]

# BmBench* BmCondition_distributionAt( BmCondition* self, uint iDistrib );
BmCondition_distributionAt= core.BmCondition_distributionAt
BmCondition_distributionAt.restype= c_void_p
BmCondition_distributionAt.argtypes= [c_void_p, c_uint]

# uint BmCondition_from_attach( BmCondition* self, BmCode* configuration, BmBench* distribution );
BmCondition_from_attach= core.BmCondition_from_attach
BmCondition_from_attach.restype= c_uint
BmCondition_from_attach.argtypes= [c_void_p, c_void_p, c_void_p]

# void BmCondition_switch( BmCondition* self, BmCondition* doppelganger );
BmCondition_switch= core.BmCondition_switch
BmCondition_switch.restype= c_void_p
BmCondition_switch.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_infer( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_infer= core.BmCondition_infer
BmCondition_infer.restype= c_void_p
BmCondition_infer.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_newDistributionByInfering= core.BmCondition_newDistributionByInfering
BmCondition_newDistributionByInfering.restype= c_void_p
BmCondition_newDistributionByInfering.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering_mask( BmCondition* self, BmBench* longDistrib, BmCode* parentMask );
BmCondition_newDistributionByInfering_mask= core.BmCondition_newDistributionByInfering_mask
BmCondition_newDistributionByInfering_mask.restype= c_void_p
BmCondition_newDistributionByInfering_mask.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_print( BmCondition* self, char* output );
BmCondition_print= core.BmCondition_print
BmCondition_print.restype= c_void_p
BmCondition_print.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printSep( BmCondition* self, char* output, char* separator );
BmCondition_printSep= core.BmCondition_printSep
BmCondition_printSep.restype= c_void_p
BmCondition_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printExtend( BmCondition* self, char* output );
BmCondition_printExtend= core.BmCondition_printExtend
BmCondition_printExtend.restype= c_void_p
BmCondition_printExtend.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printExtendSep( BmCondition* self, char* output, char* separator );
BmCondition_printExtendSep= core.BmCondition_printExtendSep
BmCondition_printExtendSep.restype= c_void_p
BmCondition_printExtendSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printIdentity( BmCondition* self, char* output );
BmCondition_printIdentity= core.BmCondition_printIdentity
BmCondition_printIdentity.restype= c_void_p
BmCondition_printIdentity.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInferer( BmCode* variableSpace, uint inputDimention, uint outputDimention );
newBmInferer= core.newBmInferer
newBmInferer.restype= c_void_p
newBmInferer.argtypes= [c_void_p, c_uint, c_uint]

# BmInferer* newBmInfererStateAction( BmCode* stateSpace, BmCode* actionSpace );
newBmInfererStateAction= core.newBmInfererStateAction
newBmInfererStateAction.restype= c_void_p
newBmInfererStateAction.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInfererStateActionShift( BmCode* stateSpace, BmCode* actionSpace, BmCode* shiftSpace );
newBmInfererStateActionShift= core.newBmInfererStateActionShift
newBmInfererStateActionShift.restype= c_void_p
newBmInfererStateActionShift.argtypes= [c_void_p, c_void_p, c_void_p]

# BmInferer* BmInferer_create( BmInferer* self, BmCode* varDomains, uint inputDimention, uint outputDimention );
BmInferer_create= core.BmInferer_create
BmInferer_create.restype= c_void_p
BmInferer_create.argtypes= [c_void_p, c_void_p, c_uint, c_uint]

# BmInferer* BmInferer_destroy( BmInferer* self );
BmInferer_destroy= core.BmInferer_destroy
BmInferer_destroy.restype= c_void_p
BmInferer_destroy.argtypes= [c_void_p]

# void deleteBmInferer( BmInferer* self );
deleteBmInferer= core.deleteBmInferer
deleteBmInferer.restype= c_void_p
deleteBmInferer.argtypes= [c_void_p]

# BmBench* BmInferer_distribution( BmInferer* self );
BmInferer_distribution= core.BmInferer_distribution
BmInferer_distribution.restype= c_void_p
BmInferer_distribution.argtypes= [c_void_p]

# uint BmInferer_inputDimention( BmInferer* self );
BmInferer_inputDimention= core.BmInferer_inputDimention
BmInferer_inputDimention.restype= c_uint
BmInferer_inputDimention.argtypes= [c_void_p]

# uint BmInferer_outputDimention( BmInferer* self );
BmInferer_outputDimention= core.BmInferer_outputDimention
BmInferer_outputDimention.restype= c_uint
BmInferer_outputDimention.argtypes= [c_void_p]

# uint BmInferer_shiftDimention( BmInferer* self );
BmInferer_shiftDimention= core.BmInferer_shiftDimention
BmInferer_shiftDimention.restype= c_uint
BmInferer_shiftDimention.argtypes= [c_void_p]

# uint BmInferer_overallDimention( BmInferer* self );
BmInferer_overallDimention= core.BmInferer_overallDimention
BmInferer_overallDimention.restype= c_uint
BmInferer_overallDimention.argtypes= [c_void_p]

# BmCondition* BmInferer_node( BmInferer* self, uint iNode );
BmInferer_node= core.BmInferer_node
BmInferer_node.restype= c_void_p
BmInferer_node.argtypes= [c_void_p, c_uint]

# uint BmInferer_node_size( BmInferer* self, uint iVar );
BmInferer_node_size= core.BmInferer_node_size
BmInferer_node_size.restype= c_uint
BmInferer_node_size.argtypes= [c_void_p, c_uint]

# BmCode* BmInferer_node_parents( BmInferer* self, uint iVar );
BmInferer_node_parents= core.BmInferer_node_parents
BmInferer_node_parents.restype= c_void_p
BmInferer_node_parents.argtypes= [c_void_p, c_uint]

# BmCondition* BmInferer_node_reinitIndependant( BmInferer* self, uint index );
BmInferer_node_reinitIndependant= core.BmInferer_node_reinitIndependant
BmInferer_node_reinitIndependant.restype= c_void_p
BmInferer_node_reinitIndependant.argtypes= [c_void_p, c_uint]

# BmCondition* BmInferer_node_reinitWith( BmInferer* self, uint index, BmCode* newDependenceList, BmBench* newDefaultDistrib );
BmInferer_node_reinitWith= core.BmInferer_node_reinitWith
BmInferer_node_reinitWith.restype= c_void_p
BmInferer_node_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# BmBench* BmInferer_process( BmInferer* self, BmBench* inputDistribution );
BmInferer_process= core.BmInferer_process
BmInferer_process.restype= c_void_p
BmInferer_process.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_process_newOverallDistribution( BmInferer* self, BmBench* inputDistribution );
BmInferer_process_newOverallDistribution= core.BmInferer_process_newOverallDistribution
BmInferer_process_newOverallDistribution.restype= c_void_p
BmInferer_process_newOverallDistribution.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_processState_Action( BmInferer* self, BmCode* state, BmCode* action );
BmInferer_processState_Action= core.BmInferer_processState_Action
BmInferer_processState_Action.restype= c_void_p
BmInferer_processState_Action.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmInferer_print( BmInferer* self, char* output );
BmInferer_print= core.BmInferer_print
BmInferer_print.restype= c_void_p
BmInferer_print.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printStateActionSignature( BmInferer* self, char* output );
BmInferer_printStateActionSignature= core.BmInferer_printStateActionSignature
BmInferer_printStateActionSignature.restype= c_void_p
BmInferer_printStateActionSignature.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printDependency( BmInferer* self, char* output );
BmInferer_printDependency= core.BmInferer_printDependency
BmInferer_printDependency.restype= c_void_p
BmInferer_printDependency.argtypes= [c_void_p, c_void_p]

# BmEvaluator* newBmEvaluatorBasic( uint spaceDimention, uint numberOfCriteria );
newBmEvaluatorBasic= core.newBmEvaluatorBasic
newBmEvaluatorBasic.restype= c_void_p
newBmEvaluatorBasic.argtypes= [c_uint, c_uint]

# BmEvaluator* newBmEvaluatorWith( BmCode* newSpace, uint numberOfCriteria );
newBmEvaluatorWith= core.newBmEvaluatorWith
newBmEvaluatorWith.restype= c_void_p
newBmEvaluatorWith.argtypes= [c_void_p, c_uint]

# BmEvaluator* BmEvaluator_createWith( BmEvaluator* self, BmCode* newSpace, uint numberOfCriteria );
BmEvaluator_createWith= core.BmEvaluator_createWith
BmEvaluator_createWith.restype= c_void_p
BmEvaluator_createWith.argtypes= [c_void_p, c_void_p, c_uint]

# void deleteBmEvaluator( BmEvaluator* self );
deleteBmEvaluator= core.deleteBmEvaluator
deleteBmEvaluator.restype= c_void_p
deleteBmEvaluator.argtypes= [c_void_p]

# BmEvaluator* BmEvaluator_destroy( BmEvaluator* self );
BmEvaluator_destroy= core.BmEvaluator_destroy
BmEvaluator_destroy.restype= c_void_p
BmEvaluator_destroy.argtypes= [c_void_p]

# BmCode* BmEvaluator_space( BmEvaluator* self );
BmEvaluator_space= core.BmEvaluator_space
BmEvaluator_space.restype= c_void_p
BmEvaluator_space.argtypes= [c_void_p]

# uint BmEvaluator_numberOfCriteria( BmEvaluator* self );
BmEvaluator_numberOfCriteria= core.BmEvaluator_numberOfCriteria
BmEvaluator_numberOfCriteria.restype= c_uint
BmEvaluator_numberOfCriteria.argtypes= [c_void_p]

# BmTree* BmEvaluator_crit( BmEvaluator* self, uint iCritirion );
BmEvaluator_crit= core.BmEvaluator_crit
BmEvaluator_crit.restype= c_void_p
BmEvaluator_crit.argtypes= [c_void_p, c_uint]

# BmVector* BmEvaluator_weights( BmEvaluator* self );
BmEvaluator_weights= core.BmEvaluator_weights
BmEvaluator_weights.restype= c_void_p
BmEvaluator_weights.argtypes= [c_void_p]

# double BmEvaluator_crit_weight( BmEvaluator* self, uint iCritirion );
BmEvaluator_crit_weight= core.BmEvaluator_crit_weight
BmEvaluator_crit_weight.restype= c_double
BmEvaluator_crit_weight.argtypes= [c_void_p, c_uint]

# double BmEvaluator_process( BmEvaluator* self, BmCode* input );
BmEvaluator_process= core.BmEvaluator_process
BmEvaluator_process.restype= c_double
BmEvaluator_process.argtypes= [c_void_p, c_void_p]

# double BmEvaluator_processState_action( BmEvaluator* self, BmCode* state, BmCode* action );
BmEvaluator_processState_action= core.BmEvaluator_processState_action
BmEvaluator_processState_action.restype= c_double
BmEvaluator_processState_action.argtypes= [c_void_p, c_void_p, c_void_p]

# double BmEvaluator_processState_action_state( BmEvaluator* self, BmCode* state, BmCode* action, BmCode* statePrime );
BmEvaluator_processState_action_state= core.BmEvaluator_processState_action_state
BmEvaluator_processState_action_state.restype= c_double
BmEvaluator_processState_action_state.argtypes= [c_void_p, c_void_p, c_void_p, c_void_p]

# double BmEvaluator_crit_process( BmEvaluator* self, uint iCriterion, BmCode* input );
BmEvaluator_crit_process= core.BmEvaluator_crit_process
BmEvaluator_crit_process.restype= c_double
BmEvaluator_crit_process.argtypes= [c_void_p, c_uint, c_void_p]

# BmEvaluator* BmEvaluator_reinitCriterion( BmEvaluator* self, uint numberOfCriterion );
BmEvaluator_reinitCriterion= core.BmEvaluator_reinitCriterion
BmEvaluator_reinitCriterion.restype= c_void_p
BmEvaluator_reinitCriterion.argtypes= [c_void_p, c_uint]

# BmTree* BmEvaluator_crit_reinitWith( BmEvaluator* self, uint index, BmCode* newDependenceMask, uint numberOfOptions, double defaultValue );
BmEvaluator_crit_reinitWith= core.BmEvaluator_crit_reinitWith
BmEvaluator_crit_reinitWith.restype= c_void_p
BmEvaluator_crit_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_uint, c_double]

# void BmEvaluator_crit_setWeight( BmEvaluator* self, uint iCritirion, double weight );
BmEvaluator_crit_setWeight= core.BmEvaluator_crit_setWeight
BmEvaluator_crit_setWeight.restype= c_void_p
BmEvaluator_crit_setWeight.argtypes= [c_void_p, c_uint, c_double]
