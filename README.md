# Padding Oracle Attack

This project demonstrates AES encryption in CBC mode. The goal is to showcase how CBC mode works, including encryption, decryption, padding, and how this can be exploited.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python**: Version 3.6 or higher.
- **pip**: Python's package installer.

## Setting Up the Project

To ensure an isolated environment for this project, it's recommended to use a Python virtual environment. This will keep dependencies separate from your global Python installation.

### Step 1: Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/Roemerdt/padding-oracle.git
cd padding-oracle
```

### Step 2: Create a Virtual Environment

Once inside the project folder, create a virtual environment. This will allow you to manage dependencies for the project separately from your global Python environment.

Run the following command to create a virtual environment:

```bash
python3 -m venv .venv
```

This will create a folder called `.venv` that contains the virtual environment files.

### Step 3: Activate the Virtual Environment

After creating the virtual environment, activate it:

- On **macOS/Linux**, run:

   ```bash
   source .venv/bin/activate
   ```

- On **Windows**, run:

   ```bash
   .venv\Scripts\activate
   ```

After activation, your terminal prompt will indicate that you are working inside the virtual environment (usually by showing `(.venv)` at the beginning of the line).

### Step 4: Install Project Dependencies

With the virtual environment activated, install the necessary Python libraries for the project using `pip`:

```bash
pip install pycryptodome
```

This will install the `pycryptodome` library, which is used for cryptographic operations in this project.

### Step 5: Running the Project

Now that your environment is set up and dependencies are installed, you can run the project. Ensure your virtual environment is activated and then run:

```bash
python main.py
```

This will execute the Python script, which demonstrates AES encryption and decryption in CBC mode.

## Deactivating the Virtual Environment

When you are done working on the project, you can deactivate the virtual environment by running the following command:

```bash
deactivate
```

This will exit the virtual environment and return you to your global Python environment.