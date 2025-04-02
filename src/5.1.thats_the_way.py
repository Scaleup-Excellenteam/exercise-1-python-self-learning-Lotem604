import os

def thats_the_way(root, pattern="deep"):
    # This script searches for files in a given directory whose names start with a specific pattern.
    # It then returns each matching file as a list.
    lst = []

    for fileName in os.listdir(root):
        if fileName.startswith(pattern):
            lst.append(fileName)
    
    return lst


def main() -> None:
    pattern = 'deep'
    path = '../exelentim/exercise-1-python-self-learning-Lotem604/content/week05/images'
    files = thats_the_way(path, pattern)
    for i, file in enumerate(files, 1):
        print(f'file {i} is: {file}')


if __name__ == '__main__':
    main()
