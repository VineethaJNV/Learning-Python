color = input("Enter traffic color light")

match color:
    case "Green":
        print("go!")
    case "Red":
        print("Stop!")
    case "Yellow":
        print("look")
    case_:
        print("Wrong color")