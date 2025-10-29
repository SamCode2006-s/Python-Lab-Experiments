def demonstrate_syntax():
    print("---Section 1: Basic Syntax---")
    my_variable=100
    print(f"The value of 'my_variable' is: {my_variable}")
    my_variable="Hello, Python!"
    print(f"The new value of 'my_variable' is: '{my_variable}'")
    if my_variable=="Hello, Python!":
        print("This message is inside the 'if' block")
        print("Indentation is crucial")
    else:
        print("This message is inside the 'else' block")
    print("This line is outside the 'if-else' block")

def demonstrate_data_types():
    print("\n---Section 2: Data Types---")
    print("\n1: Numeric Data Types:")
    integer_number=42
    float_number=3.14159
    complex_number=2+5j
    print(f"Integer: {integer_number} (Type: {type(integer_number)})")
    print(f"Float: {float_number} (Type: {type(float_number)})")
    print(f"Complex: {complex_number} (Type: {type(complex_number)})")
    print("\n2: String Data Types:")
    my_str="Python is powerful."
    print(f"String: '{my_str}' (Type: {type(my_str)})")
    print(f"First Character: '{my_str[0]}'")
    print(f"Characters from index 7 to end: '{my_str[7:]}'")
    print("\n3: Boolean Data Types:")
    is_true=True
    is_false=False
    print(f"Boolean value 'True': {is_true} (Type: {type(is_true)})")
    print(f"Boolean value 'False': {is_false} (Type: {type(is_false)})")
    print(f"Result of 10>5: {10>5}")
    print("\n4: Collection Data Types:")
    my_list=[10,20,"Hello",4.5]
    print(f"List: {my_list} (Type: {type(my_list)})")
    my_list.append(50)
    print(f"List after adding new item: {my_list}")
    my_tuple=(100,200,"World")
    print(f"Tuple: {my_tuple} (Type: {type(my_tuple)})")
    my_dict={"name":"Alice","age":25}
    print(f"Dictionary: {my_dict} (Type: {type(my_dict)})")
    print(f"Value of key 'name': {my_dict['name']}")
    my_set={1,2,3,2,1}
    print(f"Set (Duplicates removed): {my_set} (Type: {type(my_set)})")
if __name__=="__main__":
    print("Executing program")
    demonstrate_syntax()
    demonstrate_data_types()
    print("Program successful")
