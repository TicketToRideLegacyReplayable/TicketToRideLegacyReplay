# TicketToRideLegacyReplayable

A program to allow you to replay Ticket To Ride Legacy Edition.

## Prerequisites

- **CMake**: Version 3.14 or higher.
- **Python**: Ensure Python 3 is installed on your system.

## Installation

To build and install the application, follow these steps:

1. **Configure the build**:

    ```sh
    cmake -S . -B build -DCMAKE_INSTALL_PREFIX=<path/to/install/directory>
    ```

    This command will create a virtual environment and prepare the project for building.

2. **Build the project**:

    ```sh
    cmake --build build --config Release
    ```

    This command compiles the project and packages it using PyInstaller.

3. **Install the application**:

    ```sh
    cmake --install build --config Release --prefix <path/to/install/directory>
    ```

    Replace `<path/to/install/directory>` with the directory where you want to install the application.

## Creating an Installer

To package the application as an installer for distribution:

1. **Configure the build**:

    ```sh
    cmake -S . -B build
    ```

    This command will create a virtual environment and prepare the project for building.

2. **Build the project** (if not already done):

    ```sh
    cmake --build build --config Release
    ```

3. **Generate the installer**:

    ```sh
    cpack --config build/CPackConfig.cmake
    ```

    This will create an installer appropriate for your platform (e.g., NSIS on Windows, DEB/RPM on Linux, DragNDrop on macOS).

## Running the Application

After installation, you can run the application directly from the installation directory. On Windows, you will find an `.exe` file, while on macOS and Linux, you'll have a binary named `TicketToRideLegacyReplayable`.
