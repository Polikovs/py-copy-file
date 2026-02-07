def copy_file(command: str) -> None:

    temp = command.split()
    if len(temp) == 3:
        command, old_file, new_file = temp
        if old_file != new_file and command == "cp":
            try:
                with (open(old_file, "r") as file_in,
                      open(new_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("File not found")
