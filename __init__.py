# Codex By KangEhem
# Udah Tinggal pake aja, gak usah di recode:v
import re
import sys
import os
import marshal
import zlib
import base64
import types
import time
import struct
import io
from opcode import *
if sys.version_info >= (3,4):
        from importlib.util import MAGIC_NUMBER
else:
    import imp
    MAGIC_NUMBER = imp.get_magic()
kapten=base64.b64decode(b'PFRoaXMgQ29kZSBHZW5lcmF0ZWQgQnkgRGlzMz4=').decode()

def _pack_uint32(val):
    return struct.pack("<I", val)

def code_to_bytecode(code, mtime=0, source_size=0):
    data = bytearray(MAGIC_NUMBER)
    if sys.version_info >= (3,7):
        data.extend(_pack_uint32(0))
    data.extend(_pack_uint32(int(mtime)))
    if sys.version_info >= (3,2):
        data.extend(_pack_uint32(source_size))
    data.extend(marshal.dumps(code))
    return data

def dump_to_pyc(byte_code, file):
    pyc_code = code_to_bytecode(byte_code, time.time())
    with open(file, mode="wb") as f:
        f.write(pyc_code)

class Asm:
    def __init__(self, file, ki=False):
        self.file=file
        self.ki=ki
        self.mm=lambda x:bytes(bytearray(x))

    def kawai(self, my_code, key_name, master_key):
        arg1 = my_code.co_code
        arg2 = my_code.co_consts
        if master_key in [1]:
            arg1 = key_name
        if master_key in [2]:
            arg2 = key_name
        data=[my_code.co_argcount,my_code.co_nlocals,my_code.co_stacksize,my_code.co_flags,arg1,arg2,my_code.co_names,my_code.co_varnames,my_code.co_filename,my_code.co_name,my_code.co_firstlineno,my_code.co_lnotab,my_code.co_freevars,my_code.co_cellvars]
        try:
            data[1:1] = [my_code.co_posonlyargcount,my_code.co_kwonlyargcount]
        except:
            data.insert(1, my_code.co_kwonlyargcount)
        return types.CodeType(*data)

    def get_byte_code(self, source):
        yah_kok_knok = re.findall("\((.*)\)", source)[0].split(",")
        sorry2_lag_cok = "".join([chr(int(yeah)) for yeah in yah_kok_knok])
        return marshal.loads(zlib.decompress(base64.b64decode(sorry2_lag_cok)))

    def regex(self, rip_grep, offset=''):
        this_fucker = None
        if offset in [1]:
            this_fucker = "sparator"
        if offset in [2]:
            this_fucker = 'have_code'
        result_point = []
        rg_split = rip_grep.splitlines()
        arg_repr = 0
        offset_width = len(rg_split)
        while arg_repr < offset_width:
            key_name = rg_split
            if key_name[arg_repr][:len(this_fucker)] in [this_fucker]:
               arg_repr = arg_repr + 1
               continue
            awokawok = key_name[arg_repr].split()
            sparator = len(awokawok)
            for wibu in range(sparator):
                if awokawok[wibu] in opmap.keys():
                    result_point.append(opmap[awokawok[wibu]])
                    result_point.append(int(awokawok[wibu+1]))
                    break
            arg_repr = arg_repr + 1
        return result_point

    def main_asm(self, arg=0, arg1=1, arg2=2):
        read = open(self.file).read().split(kapten)
        my_py_ini = self.get_byte_code(read[arg])
        master_key = list(my_py_ini.co_consts)
        offset_width = len(read) - arg1
        arg_repr = arg
        while arg_repr < offset_width:
            arg_value = read[arg_repr]
            arg_split = arg_value.splitlines()
            if "sparator" and "<code object" in str(arg_split):
                get_num_tuple = re.findall("\((\d+)\)", arg_split[arg1])
                this_is_point = len(get_num_tuple)
                if this_is_point in [arg1]:
                    my_axist = int(get_num_tuple[arg])
                    kode_keras = master_key[my_axist]
                    int_bytecode = self.regex(arg_value, arg1)
                    xl_prioritas = self.mm(int_bytecode)
                    master_key[my_axist] = self.kawai(kode_keras, xl_prioritas, arg1)
                if this_is_point in [arg2] or this_is_point > arg2:
                    arg_func = int(get_num_tuple[arg])
                    bokep_indo = int(get_num_tuple[arg1])
                    sparator = master_key[arg_func]
                    story_wa = list(sparator.co_consts)
                    broken_heart = story_wa[bokep_indo]
                    get_code_info = self.regex(arg_value, arg1)
                    in_bytecode = self.mm(get_code_info)
                    story_wa[bokep_indo] = self.kawai(broken_heart, in_bytecode, arg1)
                    master_key[arg_func] = self.kawai(sparator, tuple(story_wa), arg2)
            arg_repr = arg_repr + arg1
        my_self = self.regex(read[arg1], arg2)
        this_bytecode = self.mm(my_self)
        my_telkomsel = self.kawai(my_py_ini, this_bytecode, arg1)
        return self.kawai(my_telkomsel, tuple(master_key), arg2)

    def main(self):
        byte_code = self.main_asm()
        if self.ki:
            return byte_code
        pyc_file = ".".join([os.path.splitext(self.file)[0], "pyc"])
        dump_to_pyc(byte_code, pyc_file)
        print("sukses write to %s" % pyc_file)

class Dis:
    def __init__(self,code):
        self.kodek=code

    def dis_py3(self, this_code):
        aray = this_code.co_code
        argval = list(aray)
        arg_repr = 0
        length = len(argval) - 1
        while arg_repr < length:
            oparg = argval[arg_repr]
            op = opname[oparg]
            arg2_int = argval[arg_repr + 1]
            this_key = " ".join(["", repr(arg_repr), op, repr(arg2_int)])
            if oparg in hasname:
                print("%s (%s)"%(this_key, this_code.co_names[arg2_int]))
            elif oparg in haslocal:
                print("%s (%s)"%(this_key, this_code.co_varnames[arg2_int]))
            elif oparg in hasconst:
                print("%s (%s)"%(this_key, repr(this_code.co_consts[arg2_int])))
            elif oparg in hascompare:
                print("%s (%s)"%(this_key, cmp_op[arg2_int]))
            else:print(this_key)
            arg_repr = arg_repr + 2
        print(kapten)

    def puki(self, this_text, this_code):
        print(this_text)
        self.dis_py3(this_code)
        return list(this_code.co_consts)

    def main(self):
        print("# This Script Written By KangEhem")
        print("# Dont Forget To Follow My Github Profile !")
        ag=list(base64.b64encode(zlib.compress(marshal.dumps(self.kodek))))
        list_byte = '(%s)'%','.join([str(i) for i in ag])
        aray=self.puki('%s\n%s\nhave_code %s '%(list_byte,kapten, str(self.kodek)), self.kodek)
        length = len(aray)
        for aargh in range(length):
            argval = aray[aargh]
            if type(argval) is types.CodeType:
                array=self.puki("sparator (%s) %s"%(str(aargh), str(argval)), argval)
                for aargh2 in range(len(array)):
                    argval2 = array[aargh2]
                    if type(argval2) is types.CodeType:
                        self.puki("sparator (%s)(%s) %s" % (str(aargh), str(aargh2), str(argval2)), argval2)


def load_module(Sparator):
    y = None
    try:
        x = open(Sparator).read()
        y = compile(x, Sparator, "exec")
    except Exception as i:
        try:
            x = open(Sparator, "rb")
            x.seek(16)
            y = marshal.loads(x.read())
        except Exception as i:
            exit("Sepertinya ada kesalahan di file %s"%Sparator)
    return y

def cekfile(f):
    if not os.path.exists(f):
        exit("File %s Tidak Ditemukan"%f)

def menu(sys):
    asm = False
    if len(sys) <= 2:
        exit("usage: dis3 (dis|asm) file.py")
    file = sys[2]
    if sys[1] == "asm":
        asm = True
    cekfile(file)
    if asm:
        Asm(file).main()
    else:
        x = load_module(file)
        Dis(x).main()

def main():
    try:menu(sys.argv)
    except (KeyboardInterrupt, EOFError):exit()
# Mau Nyari Apaan Sih Cuk?
