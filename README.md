# Python Concurrency Getting Started

Code for Python Concurrency Getting Started Course on Pluralsight.

# GIL Workarounds

GIL_less Python interpreters

+ Jython
+ IronPython

Python Multiprocessing

## Process vss Threads

+ Sidesteps GIL
+ Less need for synchronization
+ Can be paused and terminate
+ More resilient
+ Higher memory footprint
+ Expensive context switches

## Pickling

is the process whereby a Python object hierarchy is converted into a byte stream, 'unpacking' is the inverse operation

## Picklable Objects

+ None, True, False
+ integers, floats, complex numbers
+ Normal and Unicode strings
+ Collections containing only picklable objects
+ Top level functions
+ Classes with picklable attributes

## Daemon process

is a child process that does not prevent its parent process from exiting

## Terminating Process

+ is_alive()
+ terminate()


## Process.terminate() gotchas

+ Shared resources may be put in an inconsistent state
+ Finally clauses and exit handlers will not be run

'''
class multiprocessing.Pool([num_processes # default is num of cpu cors
[,initializer
[,initargs # picklable not required
[maxtasksperchild]]] ])
''''

'''
map(func, iterable[,chunksize])
'''


## Inter-process communication

+ Pipe
+ Queue


## Multiprocess Queue Methods

| threading.Queue | multiprocessing.Queue | multiprocessing.JoinableQueue | 
|-----------------|-----------------------|-------------------------------|
| qsize()         | qsize                 | qsize                         |
| put()           | put()                 | put()                         |
| get()           | get()                 | get()                         |
| empty()         | empty()               | empty()                       |
| full()          | full()                | full()                        |
| task_done()     | -- task_done() --     | task_done()                   |
| join()          | join()                | join()                        |




## Shared State

+ Shared Memory
  + multiprocessing.Value
+ Manager Process
  + multiprocessing.Array

'''python
multiprocessing.Value(typecode_or_type, *args[, lock])
'''

## ctypes

| ctypes type | Ctype                     | Python type               | Type-code |
|-------------|---------------------------|---------------------------|-----------|
| c_bool      | _Bool                     | bool(1)                   |           |
| c_char      | char                      | 1-character bytes object  | 'c'       |
| c_wchar     | wchar_t                   | 1-character string object | 'u'       |
| c_int       | int                       | int                       | 'i'       |
| c_long      | long                      | int                       | 'l'       |
| c_float     | float                     | float                     | 'f'       |
| c_char_p    | char *(NUL terminated     | bytes object or None      |           |
| c_wchar_p   | wchar_t * (NUL terminated | string object or None     |           |
| c_void_p    | void *                    | int or None               | -         |

## Manager

| Value      | Array     | 
|------------|-----------|
| Dictionary | List      |
| Lock       | Semaphore |

## Manager Shared Objects

| Data Structures | Synchronization Mechanisms | 
|-----------------|----------------------------|
| Value           | Lock                       |
| Array           | RLock                      |
| List            | BoundedSemaphore           |
| Dict            | Event                      |
| Namespace       | Condition                  |
| Queue           | Barrier                    |

## Cooperative Multitasking

+ Tasks suspend themselves to allow others run
+ Event loop resumes the task when the IO operation completes
+ Tasks => Coroutines

## Coroutine

+ Coroutine Function
+ Coroutine Object


> pip install aiohttp