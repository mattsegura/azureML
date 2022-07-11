from azureml.core import Workspace

# Access the workspace from the config.json
print("Accessing the workspace...")
ws = Workspace.from_config(path="./config")
