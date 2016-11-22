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


def create_data_files(path, base_url, html, count):
    create_project_directory(path)
    file_name = path + '/File ' + str(count) + '.txt'
    data = base_url + '\n' + str(html).decode('utf-8')
    crawled = path + '/crawled.txt'
    if not os.path.isfile(file_name):
        write_file(file_name, data)