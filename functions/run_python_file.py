import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        is_file = os.path.isfile(target_file)
        
        if not valid_target_dir:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not is_file:
            raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        
        if len(file_path) < 3 or file_path[-3:] != ".py":
            raise Exception(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", target_file]
        
        if args is not None:
            command.extend(args)
            
        # Run the command
        res = subprocess.run(command, capture_output=True, text=True, cwd=working_dir_abs, timeout=30)
        
        str_output = ""
        
        if res.returncode == 0:
            if res.stdout:
                str_output += f"STDOUT: {res.stdout}"
            if res.stderr:
                str_output += f"STDERR: {res.stderr}"
        else:
            str_output += f"Process exited with code {res.returncode}"
            
        if str_output.strip() == "":
            str_output += "No output captured"
            
        return str_output
        
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"