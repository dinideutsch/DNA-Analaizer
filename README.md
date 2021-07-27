## DNA PROJECT
#### Description
This project stands for creating and manipulating DNA sequences,
using special command lines.
#### Usage
run the main function in the main file
and then use one or more of the following commands:
* Create a DNA sequence ATC named first (if no @name will be sent, a default name will be generated):
```python
new ATC @first
```
* Duplicate a sequence with id number 1:
```python
dup #1
```
* Load sequence from some_file.rawdna and name it third:
```python
load some_file.rawdna @third
```
* 1. Count the amount of times that subsequence A appears in the sequence named third
  2. Count the amount of times that subsequence named first appears in the sequence named third
 
```python
1. count @third A
2. count @second @first
```
* Find the first index of:
  1. Explicit subsequence in an existing sequence
  2. Existing sequence  in an existing sequence (using @name or #id)
 ```python
1. find @third A 
    find #3 A
2. find @second @first
```
* Find all indexes of explicit subsequence in an existing sequence
 ```python
 findall @third A 
 findall #3 A
```  
* Return the length of a sequence by @name or by #id:
 ```python
len @third 
len #3
``` 
* Delete a sequence by @name or by #id:
 ```python
del @third 
del #3
```
* Save a sequence by @name or by #id to a file with .rawdna suffix with a given filename or a default one:
 ```python
#this will create a file named newfile.rawdna:
save @second newfile.rawdna
#this will create a file named second.rawdna (default name):
save #2 
```
* Replace the letter in the (0-based) index of @seq_name/#seq_id by <new_letter>.
  if the command ends with : @@ or : @new_name the replaced sequence will get default / new_name name
 ```python
#this will create a sequence named new_name:
replace @first 0 T : @new_name
#this will create a sequence named first_r1 (default name):
replace @first 0 T : @@
#this will change the @name sequence itself:
replace @first 0 T
```
* Create sequence @seq_name/#seq_id with its pair sequence, 
that is, each T is replaced by an A (and vice versa), and each 
C is replaced by a G (and vice versa). if the command ends 
with : @@ or : @new_name the replaced sequence will get default / new_name name
 ```python
#this will create a sequence named new_name:
pair @first : @new_name
#this will create a sequence named first_r1 (default name):
pair @first : @@
#this will change the @name sequence itself:
pair @first
```
* Get into batch mode - every command that is entered in batch mode wil be saved in the batch and will run by running the batch:
 ```python
batch batch_name
```
* Finish batch mode:
 ```python
end
```
* Get the list of existing batches:
 ```python
batchlist
```
* Get the content of batch_name batch:
 ```python
batchshow @batch_name
```
* Save batch_name batch in file_name.dnabatch:
 ```python
batchsave @batch_name file_name.dnabatch
```
* Load file_name.dnabatch into batch_name batch if given,
  otherwise batch name will be file_name:
 ```python
#this will create a batch called batch_name
batchload file_name.dnabatch : @batch_name
#this will create a batch called file_name
batchload file_name.dnabatch
```
* Run batch_name batch:
```python
run @batchname
```
