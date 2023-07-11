import os


# path = os.path.join('/home/users', 'Desktop', 'course', 'file.txt')
# folder, file = os.path.split(path)
# path_name, extension_file = os.path.splitext(file)

path = os.path.join('/home', 'fernando', 'Downloads')

for folder in os.listdir(path):
    completed_path = os.path.join(path, folder)
    if not os.path.isdir(completed_path):
        continue

    for file in os.listdir(completed_path):
        print(file)
