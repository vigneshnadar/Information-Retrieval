import os


def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating directory' + directory)
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data.encode('utf-8'))
    f.flush()
    f.close()


def create_data_files(path, base_url, data, count):
    create_project_directory(path)
    # file_name = path + '/' + str(base_url) + ' ' + str(count) + '.txt'
    file_name = path + '/' + str(base_url) + '.txt'
    if not os.path.isfile(file_name):
        write_file(file_name, data)