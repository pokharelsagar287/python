import datetime


#taking requried inputs
def get_input():
    task = input("Enter the task activities: ")
    material = input("Enter the material used: ")
    no_of_workers = input("Enter the number of workers: ")
    #record input date onyl
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    return task, material, no_of_workers, date

#function to save the data
def save_data(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(f"Date: {data[3]}\n")
            file.write(f"Task Activities: {data[0]}\n")
            file.write(f"Material Used: {data[1]}\n")
            file.write(f"Number of Workers: {data[2]}\n")
            file.write("-" * 40 + "\n")
        #print confirmation message
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    #filename should be in format of progress_report_YYYY-MM-DD.txt
    filename = f"progress_report_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
    while True:
        print("\nDaily Progress Log")
        print("1. Add Daily Progress")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = get_input()
            save_data(filename, data)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
