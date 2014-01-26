#I like ctypes a lot, swig always tended to give me problems. Also ctypes has the advantage that you don't need to satisfy any 
#compile time dependency on python, and your binding will work on any python that has ctypes, not just the one it was compiled against.
#
#Suppose you have a simple C++ example class you want to talk to in a file called foo.cpp:
#
##include <iostream>
#
#class Foo{
#    public:
#        void bar(){
#            std::cout << "Hello" << std::endl;
#        }
#};
#Since ctypes can only talk to C functions, you need to provide those declaring them as extern "C"
#
#extern "C" {
#    Foo* Foo_new(){ return new Foo(); }
#    void Foo_bar(Foo* foo){ foo->bar(); }
#}
#Next you have to compile this to a shared library
#
#g++ -c -fPIC foo.cpp -o foo.o
#g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o
#And finally you have to write your python wrapper (e.g. in fooWrapper.py)
#
#from ctypes import cdll
#lib = cdll.LoadLibrary('./libfoo.so')
#
#class Foo(object):
#    def __init__(self):
#        self.obj = lib.Foo_new()
#
#    def bar(self):
#        lib.Foo_bar(self.obj)
#Once you have that you can call it like
#
#f = Foo()
#f.bar() #and you will see "Hello" on the screen

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

f = Foo()
f.bar() #and you will see "Hello" on the screen
