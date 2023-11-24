file_name = input("File name: ").lower().strip().split(".")
match file_name[-1]:
    case "gif"|"png":
        print("image/"+file_name[-1])
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "pdf"|"zip":
        print("application/"+file_name[-1])
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")