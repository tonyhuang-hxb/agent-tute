import os

def write_file(working_directory, file_path, content):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        is_dir = os.path.isdir(target_file)
        
        if not valid_target_dir:
            raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if is_dir:
            raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
        
        # Create all parent directories of the target file if they do not exist
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)
        
        with open(target_file, "w") as f:
            res = f.write(content)
            
        if res == len(content):
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            return f'Warning: Mismatch in number of characters written to "{file_path}", wrote {res} instead of {len(content)}'
        
    except Exception as e:
        return f"Error: {str(e)}"