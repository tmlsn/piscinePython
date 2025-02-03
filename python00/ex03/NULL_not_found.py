def NULL_not_found(object: any) -> int:

    match object :
        case None :
            print(f"Nothing: None {type(object)}")
        case False :
            print(f"Fake: False {type(object)}")
        case "" :
            print(f"Empty: {type(object)}")
        case 0 :
            print(f"Zero: 0 {type(object)}")
        case float() if object != object:
            print(f"Cheese: nan {type(object)}")
        case _ :
            print("Type not found")
            return 1
    
    return 0