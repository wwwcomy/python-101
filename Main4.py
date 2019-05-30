import pickle
'''
use pickle to dump(save) data and load(read) data
'''
try:
    with open("2.txt",'wb') as f:
        pickle.dump([1,2,'three'],f)
    with open("3.txt",'rb') as f:
        a_list = pickle.load(f)
except IOError as err:
    print(str(err))
print(a_list)