# Telephone Directory Management System

A Python-based application for managing telephone directory records. This project includes functionalities to add, update, delete, and search records in a MySQL database.

## Features

- **Add New Records**: Insert new entries into the telephone directory with ID, name, address, primary, and secondary phone numbers.
- **Update Records**: Modify existing records by updating fields like name, address, or phone numbers.
- **Delete Records**: Remove entries from the directory.
- **Search Records**: Retrieve records based on ID, name, address, or phone numbers.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` library (for connecting Python to MySQL)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telephone-directory.git
   cd telephone-directory
   ```

2. Install dependencies:
   ```bash
   pip install mysql-connector-python
   ```

3. Set up the database:
   - Modify the database connection details in `set-up.py` and `Telephone Directory V2.1.py` to match your MySQL server credentials.
   - Run `set-up.py` to create the necessary table:
     ```bash
     python set-up.py
     ```

4. Run the main program:
   ```bash
   python Telephone Directory V2.1.py
   ```

## Usage

1. On running `Telephone Directory V2.1.py`, a menu will appear with options:
   - `1`: Insert new record
   - `2`: Update existing record
   - `3`: Delete a record
   - `4`: Search records
   - `5`: Exit the program

2. Follow the prompts to interact with the telephone directory system.

## Database Schema

The project uses a table named `Directory` (or `Directory_1` as per `set-up.py`) with the following structure:
- `ID` (int, Primary Key): Unique identifier for each record.
- `Name` (varchar): Name of the person.
- `Address` (varchar): Address of the person.
- `PriPhone` (long): Primary phone number.
- `SecPhone` (long): Secondary phone number (optional).

## Notes

- Ensure the MySQL server is running and the specified database exists before executing the scripts.
- Validate your MySQL credentials in both Python scripts before use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
