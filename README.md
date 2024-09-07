# Code Runner

This is a simple Python script that allows users to run code in either **Python 3.10.0** or **Dart 2.19.6** using the [Piston API](https://emkc.org/api/v2/piston/execute). The script provides a user-friendly interface to input code and see the results, with the option to select the language and view output directly in the console.

## Features

- **Language Selection**: Users can choose between Python and Dart to run their code.
- **Colored Console Output**: Uses color coding in the console for better readability.
  - **Cyan** for instructions and prompts.
  - **Green** for successful output.
  - **Yellow** for warnings like no output.
  - **Red** for errors.
- **Easy Input Method**: Input your code line by line and press **Enter twice** to run the code.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/prakhardoneria/code-runner-api.git
   ```

2. **Install dependencies**:
   Make sure to have Python installed. Then, install the required package:
   ```bash
   pip install requests colorama
   ```

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Select the language**:
   When prompted, choose:
   - **1** for Python 3.10.0
   - **2** for Dart 2.19.6

3. **Enter your code**:
   Type or paste your code, line by line. After finishing your code, press **Enter twice** to execute.

4. **See the output**:
   The script will display the output of your code in the console.

### Example

```
Choose a language to run your code:
1. Python 3.10.0
2. Dart 2.19.6
Enter 1 for Python or 2 for Dart: 1

You chose Python version 3.10.0.
Enter your code (press Enter twice to run):

print("Hello, World!")

Output:
Hello, World!
```

## List of Available Runtimes

You can find the full list of supported runtimes and their versions at:

[https://emkc.org/api/v2/piston/runtimes](https://emkc.org/api/v2/piston/runtimes)

## API Used

The script uses the **Piston API** to execute code. The API is a great tool to run code in various languages. You can check out more details about the API and its runtimes:

- **API Endpoint**: [https://emkc.org/api/v2/piston/execute](https://emkc.org/api/v2/piston/execute)
- **List of runtimes**: [https://emkc.org/api/v2/piston/runtimes](https://emkc.org/api/v2/piston/runtimes)
