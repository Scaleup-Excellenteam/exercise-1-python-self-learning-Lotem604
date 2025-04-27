import os

def thats_the_way(root: str, pattern: str = "deep") -> list:
    """
    Searches for files in the specified directory whose names start with a specific pattern.

    Args:
        root (str): Path to the directory to search.
        pattern (str): Pattern that matching file names should start with (default is 'deep').

    Returns:
        list: A list of matching file names.
    
    Raises:
        FileNotFoundError: If the provided directory path does not exist.
    """
    if not os.path.isdir(root):
        raise FileNotFoundError(f"The directory '{root}' does not exist.")

    return [fileName for fileName in os.listdir(root) if fileName.startswith(pattern)]

def main() -> None:
    pattern = 'deep'
    path = '../exelentim/exercise-1-python-self-learning-Lotem604/content/week05/images'
    try:
        files = thats_the_way(path, pattern)
        for i, file in enumerate(files, 1):
            print(f'file {i} is: {file}')
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
