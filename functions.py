FILEPATH= "todo.txt"
def get_todos(filepath=FILEPATH):
    """read the text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local= file_local.readlines()
        return todos_local


def write_todos(todos_arg,filepath="todo.txt"):
    """write the to-do items list in the text files"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(__name__)

if __name__=="__main__":
    print("HELLO")
    print(get_todos())