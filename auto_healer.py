import subprocess

def check_sql_service():
    result = subprocess.run("sc query MSSQLSERVER", capture_output=True, text=True)
    
    if "RUNNING" in result.stdout:
        print("SQL Server is running fine.")
    else:
        print("SQL Server is stopped. Restarting now...")
        subprocess.run("net start MSSQLSERVER")
        print("Service restarted successfully.")

check_sql_service()