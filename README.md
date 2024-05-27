# Python_FastApi
creating fastapi crud operation using mysql database

# Download Python:
1. Go to the official Python website: https://www.python.org/downloads/
2. Download the latest version of Python for your operating system.

# Installing Python In Intellij Idea
1. Download and install intellij Idea Community Edition https://www.jetbrains.com/idea/download/. Open IntelliJ IDEA. 
2. Install Python Plugin:
3. Go to File > Settings 
4. Navigate to Plugins. 
5. Search for "Python" in the marketplace. 
6. Install the Python plugin. 
7. Restart IntelliJ IDEA if prompted.

# Create Python Project
1. Open IntelliJ IDEA. 
2. Click on New Project. 
3. Select Python from the list of project types. 
4. Choose the location for your project. 
5. Ensure the correct Python interpreter is selected (you should see the Python version you installed earlier). 
6. Right-click on the src or main project directory in the Project Explorer. 
7. Select New > Python File. 
8. Name your file (e.g., main.py).

# Install Uvicorn for running python application
pip install fastapi uvicorn (for fastapi and uvicorn )

# Run Python application on default host and port
1. go to main folder 
2. uvicorn main:app --reload

# Run python application on custom host and port
uvicorn main:app --reload --host 127.0.0.1 --port 8082

# Swagger run
127.0.0.1:8082/docs
