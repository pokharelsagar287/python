#taking requried inputs

def get_input():
    project_name = input("Enter the project name: ")
    work_summary = input("Enter the work summary: ")
    issue_faced = input("Enter the issue faced: ")
    no_of_workers = input("Enter the number of workers: ")
    return project_name, work_summary, issue_faced, no_of_workers


#function to format the data into a mail


def generate_mail(data):
    mail_content = f"""
    Subject: Daily Progress Report - {data[0]}
    
    Dear Team,
    
    Here is the daily progress report for the project '{data[0]}'.
    
    Work Summary:
    {data[1]}
    
    Issues Faced:
    {data[2]}
    
    Number of Workers:
    {data[3]}
    
    Best Regards,
    Project Management Team
    """
    return mail_content

def main():
   
    data = get_input()
    generate_mail(data)
    #print the generated mail
    print("\nGenerated Mail:")
    print(generate_mail(data))
    #save the generated mail to a file
    filename = f"Mail_Sample_{data[0]}.txt"
    with open(filename, 'w') as file:
        file.write(generate_mail(data))
    print(f"\nMail saved to {filename}.")
    






    #redirect to mail with that generated mail
    import webbrowser
    import os
    import urllib.parse
    confirmation = input("Do you want to open the mail in your default mail client? (y/n): ")
    if confirmation.lower() == 'y':
        subject = urllib.parse.quote(f"Daily Progress Report - {data[0]}")
        body = urllib.parse.quote(generate_mail(data))
        mailto_link = f"mailto:?subject={subject}&body={body}"
        webbrowser.open(mailto_link)

if __name__ == "__main__":  
    main()  