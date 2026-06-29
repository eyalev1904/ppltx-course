
class clinic:

    def __init__(self):
# Q2 when to use which brackets?
        self.dogs = []

    def add_dog(self,name, breed, age, is_vacc, chip_id, days_in_clinic = 1):
        dog ={
            "name":name,
            "breed":breed,
            "age":age,
            "is_vacc":is_vacc,
            "chip_id":chip_id,
            "days_in_clinic":days_in_clinic
        }
        self.dogs.append(dog)
        return dog

# Q4 - When to use just print and when to user for?
    def show_dogs(self):
        # print(self.dogs)
        for dog in self.dogs:
            print(dog)

    def remove_dog(self, chip_id):
        chip_id = int(chip_id)

        for dog in self.dogs:
            if dog["chip_id"] == chip_id:
                self.dogs.remove(dog)
                return f"Dog with chip {chip_id} removed."

        return "Chip ID not found."

    def vaccinate(self,chip_id):
            target_id = int(chip_id)
            for dog in self.dogs:
                if dog["chip_id"] == target_id:
                    if dog["is_vacc"] == True:
                        return "already_vaccinated"
                    else:
                        dog["is_vacc"] = True
                        return "just_vaccinated"
            return "not_found"

    def days(self,chip_id):
        target_id = int(chip_id)
        for dog in self.dogs:
            if dog["chip_id"] == target_id:
                dog["days_in_clinic"] += 1
                return f"Days in clicnic {dog["days_in_clinic"]}."
            # else:
            #     print("chip_id not in the list")
            #     break
        return None

def project():
    mapping = clinic()
    
    mapping.add_dog("Buddy", "Golden Retriever", 1, True, 5, 123)
    mapping.add_dog("Luna", "Border Collie", 7, True, 2, 345)
    

    while True:
        print("\n1. display dogs")
        print("2. add dog")
        print("3. checkout dog")
        print("4. vaccinate dog")
        print("5. check days")
        print("6: exit")

        choice = input("Choose option (1-6): ")

        if choice == '1':
            mapping.show_dogs()
        elif choice == '2':
            print(mapping.add_dog(
                input("Name: "),
                input("breed:"),
                int(input("age:")),
                input("is_vaccinated:").lower() in ["true", "yes", "y"],
                int(input("chip_id:"))
            ))
        elif choice == '3':
            # mapping.checkout_dog(input("chip_id: "))
            i = input("chip_id: ")
            print(mapping.remove_dog(i))
        # didn't work - fix below
        # elif choice == '4':
        #     i = input("chip_id: ")
        #     print(f"is he vaccinated? {mapping.vaccinate(i)}")
        elif choice == '4':
            i = input("Enter chip_id to vaccinate: ")
            result = mapping.vaccinate(i)

            if result == "already_vaccinated":
                print("The dog is already vaccinated.")
            elif result == "just_vaccinated":
                print("Now the dog is vaccinated.")
            else:
                print("Error: Chip ID not found.")
        elif choice == '5':
            print(mapping.days(input("chip_id: ")))
            # print(mapping.get_dog(i))
            # print(i)
        elif choice == '6':
            break
        else:
            print("Invalid choice!")


def main():
    """Main function to run all chapter demonstrations"""
    project()

if __name__ == "__main__":
    main()
