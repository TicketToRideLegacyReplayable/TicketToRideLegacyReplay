cmake_minimum_required(VERSION 3.14)
project(TicketToRideLegacyReplayable)

# Name of the program
set(PROGRAM_NAME "TicketToRideLegacyReplayable")

# Specify Python version required
find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_target(
    CreateVenv ALL
    COMMAND ${Python3_EXECUTABLE} -m venv ${CMAKE_CURRENT_BINARY_DIR}/venv
)

if(WIN32)
    # For Windows
    set(Python3_EXECUTABLE "${CMAKE_CURRENT_BINARY_DIR}/venv/Scripts/python.exe")
elseif(UNIX)
    # Mac and Linux
    set(Python3_EXECUTABLE "${CMAKE_CURRENT_BINARY_DIR}/venv/bin/python")
else()
    message(FATAL_ERROR "Unknown OS")
endif()

# Install Python dependencies (if needed)
if (EXISTS "${CMAKE_SOURCE_DIR}/requirements.txt")
    add_custom_target(
        InstallDependencies ALL
        COMMAND ${Python3_EXECUTABLE} -m pip install -r ${CMAKE_SOURCE_DIR}/requirements.txt
        DEPENDS CreateVenv
    )
else()
    add_custom_target(
        InstallDependencies ALL
        DEPENDS CreateVenv
    )
endif()

# Set the project source files
file(GLOB_RECURSE PROJECT_SOURCES
    "${CMAKE_SOURCE_DIR}/*.py"
)

# Define the main entry point of the application
set(MAIN_SCRIPT "${CMAKE_SOURCE_DIR}/main.py")

add_custom_target(
    PackageApp ALL
    COMMAND ${Python3_EXECUTABLE} -m pip install pyinstaller
    COMMAND ${Python3_EXECUTABLE} -m PyInstaller --onefile --name ${PROGRAM_NAME} ${MAIN_SCRIPT}
    DEPENDS InstallDependencies
)
message(STATUS "CMAKE_INSTALL_PREFIX is set to: ${CMAKE_INSTALL_PREFIX}")

# Installation settings for all OSes
install(FILES ${PROJECT_SOURCES} DESTINATION ${CMAKE_INSTALL_PREFIX}/src)
install(PROGRAMS ${MAIN_SCRIPT} DESTINATION ${CMAKE_INSTALL_PREFIX})

# TODO: Understand why this isn't run
# OS-specific install configurations
if (WIN32)
    install(PROGRAMS "${CMAKE_CURRENT_BINARY_DIR}/dist/${PROGRAM_NAME}.exe" DESTINATION ${CMAKE_INSTALL_PREFIX})
elseif(UNIX)
    # Mac and Linux installation steps
    install(PROGRAMS "${CMAKE_CURRENT_BINARY_DIR}/dist/${PROGRAM_NAME}" DESTINATION ${CMAKE_INSTALL_PREFIX})
else()
    message(FATAL_ERROR "Unknown OS")
endif()

# Cross-platform package
include(CPack)

# CPack configuration
set(CPACK_PACKAGE_NAME "${PROGRAM_NAME}")
set(CPACK_PACKAGE_VENDOR "TicketToRideLegacyReplayable")
set(CPACK_PACKAGE_VERSION "0.1.1")
configure_file(
    "${CMAKE_SOURCE_DIR}/version.txt.in"
    "${CMAKE_BINARY_DIR}/version.txt"
    @ONLY
)
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Ticket To Ride Legacy Replayable Application")
set(CPACK_PACKAGE_EXECUTABLES "${PROGRAM_NAME}" "${PROGRAM_NAME}")
set(CPACK_RESOURCE_FILE_SECURITY "${CMAKE_SOURCE_DIR}/SECURITY.md")
set(CPACK_RESOURCE_FILE_README "${CMAKE_SOURCE_DIR}/README.md")

# Different generators for different OSes
if(WIN32)
    set(CPACK_GENERATOR "NSIS")
elseif(APPLE)
    set(CPACK_GENERATOR "DragNDrop")
elseif(UNIX)
    set(CPACK_GENERATOR "DEB;RPM")
else()
    message(FATAL_ERROR "Unknown OS")
endif()
