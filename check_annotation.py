import os

path = ['train','valid']


for folder_path in path:
    print(folder_path)
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
                annotation_file = filename.split(".")[0] + ".txt"
                if not os.path.exists(os.path.join(folder_path, annotation_file)):
                    print(f"{filename} is missing its annotation file")

        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    line_split = line.split(' ')
                    if len(line_split) != 5:
                        print(f'{filename}  Invalid Annotation')
                        break
                    for item in line_split:
                        try:
                            float(item)
                        except ValueError:
                            print(f'{filename} Invalid Annotation')
                            break
