from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print(get_files_info("./calculator", directory="."))
    print(get_files_info("./calculator", directory="pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))