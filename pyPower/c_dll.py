# test file
import ctypes
import time

path='C:/Users/taejin/Desktop/Code/26project-CFD/mylib/x64/Debug/mylib.dll'
c_module=ctypes.windll.LoadLibrary(path)

prime_c=c_module.prime
prime_c.argtypes=[ctypes.c_uint]
prime_c.restype=ctypes.c_bool

test=c_module.test

test()

# n=5000000

# t_s_c=time.time()
# prime_c(n)
# t_f_c=time.time()

# def prime_py(N):
#     count=0
#     for n in range(N+1):
#         D=True
#         if(n==0 or n==1):
#             continue
#         for i in range(2,int(n**0.5)+1):
#             if(n%i==0):
#                 D=False
#         if(D):
#             count+=1
#     print(count)

# print()
# t_s_py=time.time()
# prime_py(n)
# t_f_py=time.time()

# print("\n")
# print("C time      :",t_f_c-t_s_c)
# print("Python time :",t_f_py-t_s_py)

# print("C:Python ",(t_f_c-t_s_c)/(t_f_py-t_s_py),":",1)
