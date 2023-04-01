# # append aug data

# import os
# folder = '00'
# for filename in os.listdir(folder):
#         parts = filename.split('_')[0] + '.' + filename.split('.')[-1]
#         new_filename = parts
#         old_path = os.path.join(folder, filename)
#         new_path = os.path.join(folder, new_filename)
        
#         os.rename(old_path, new_path)

# import os

# folder_A = '/data/train'
# folder_B = 'yolo_data/train'

# files_A = []
# for filename in os.listdir(folder_A):
#     if filename.endswith('.jpg'):
#         files_A.append(filename)
# files_B = []
# for filename in os.listdir(folder_B):
#     if filename.endswith('.jpg'):
#         files_B.append(filename)

# files_A = set(files_A)
# files_B = set(files_B)
# only_in_A = files_A - files_B
# print(len(only_in_A))
# only_in_B = files_B - files_A
# print(len(only_in_B))

# # for file in only_in_A:
# #     os.remove(os.path.join(folder_A, file))
