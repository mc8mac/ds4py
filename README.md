# DS4PY

This script automatically generates basic docstrings for all functions in a Python file. It parses function definitions, lists each argument, and provides a placeholder for the return type.

Here’s a step-by-step guide for installing and using the `docstring_helper.py` script.

---

## Usage

1. **Clone this repository or save the `docstring_helper.py` script to your local machine**.

2. **Open a Terminal or Command Prompt**:
   - Navigate to the folder where `docstring_helper.py` is saved.

3. **Prepare Your Target File**:
   - Ensure you have a Python file with function definitions you want to document (e.g., `my_script.py`). Place it in the same directory as `docstring_helper.py` or provide the full path when running the script.

4. **Run the Script**:
   - Execute the following command, replacing `<filename>` with your target Python file’s name:

     ```bash
     python docstring_helper.py <filename>
     ```

   - **Example**:

     ```bash
     python docstring_helper.py my_script.py
     ```

## Troubleshooting

If you encounter issues running the script in your terminal, follow these steps:

1. **Clone this repository or save the `docstring_helper.py` script to the same folder as the target file**.

2. **Change the `FILE_PATH` to the name of your target file, including the `.py` extension (line 8)**:

    ```python
    FILE_PATH = "your_file.py"
    ```

3. **Run the script from your IDE**.

### Before Running the Script

```python
def multiply(x, y):
    return x * y
```

### Running the Script

```bash
python docstring_helper.py my_script.py
```

### After Running the Script

The function will be modified as follows:

```python
def multiply(x, y):
    """
    Edit Description

    x: type
    y: type

    ret: type
    """
    return x * y
```

## Additional Information

- **Error Handling**: If the specified file does not exist or if no filename is provided, the script will output an error message.
- **Customization**: After running the script, customize each docstring as needed to provide clear and accurate documentation for each function.

You are now ready to use `docstring_helper.py` to automate docstring creation in your Python files!

## Notes

- **Required Argument**: A filename argument is required. For example:
  
  ```bash
  python docstring_helper.py my_script.py
  ```
  
- **File Not Found**: If the specified file does not exist, the script will exit with an error message.
- **File Location**: Ensure the target file is in the same directory as this script if specifying only the filename, or provide the full path.

## Requirements

- Python 3.x
- `os` and `re` libraries (standard libraries)
