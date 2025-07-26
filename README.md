# Setup the workspace (CMD)
- $`conda deactivate`
- $`pip install uv`
- $`uv init [Workspace Name (Option)]`
- $`.venv/Scripts/activate`
- $`uv python list` _to list python versions_
- $`uv python install [specific python version]` _to install specific python version_
- $`uv venv env --python [specific python version]` _to create virtual env with specific python version_
- $`uv add -r requirements.txt` or `uv pip install -r requirements.txt`
- $`uv pip list` _to list the installed packages_
- $`doskey/history` _to see the previos commands you written_

# Your Environment Variables
- See the _.env.example_ file

# Run the Langgraph Studio for the basics of langgraph folder
$`langgraph dev`


# Run the App
$`uvicorn main:app --reload --port 8000`
<br> **You can reach the api page from http://localhost:8000/ and play with the api doc from _docs_ endpont**
