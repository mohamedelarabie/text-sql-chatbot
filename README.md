## 🪟 Windows Virtual Environment Setup (Single Script)

Run these commands in **PowerShell** inside your project folder:

```powershell
- python -m venv venv
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
- venv\Scripts\Activate.ps1
- pip install -r requirements.txt