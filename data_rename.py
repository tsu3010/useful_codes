import os
path = r'D:\DataScience\Image Classification\all\train_samp'
print(os.listdir(path))
str_add = '_passed'
for i, filename in enumerate(os.listdir(path)):
    print(i, filename)
    if filename.endswith('.jpg'):
        os.rename(os.path.join(path, filename), os.path.join(path, filename[:-4] + str_add + ".jpg"))
print(os.listdir(path))
