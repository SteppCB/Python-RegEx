import re
import pytest
from regex import extract_emails, validate_phone_numbers, format_phone_numbers, find_dates

# Read the story from a file
with open("story.txt", "r") as file:
    story_text = file.read()

# Part 1: Test Extract Emails
def test_extract_emails():
    expected_emails = ['effertz.viola@batz.com', 'hackett.jed@hotmail.com', 'sadie.kuhn@ward.com', 'kathryne92@gmail.com', 'fbayer@terry.biz', 'toni74@nikolaus.biz', 'senger.cale@ullrich.com', 'tom.oberbrunner@gmail.com', 'imann@gmail.com', 'asha46@blanda.com', 'retha11@yahoo.com', 'vada.pacocha@hotmail.com', 'myron85@hotmail.com', 'kbergstrom@herman.com', 'vicky.carter@gmail.com', 'bernier.darrell@hammes.com', 'sigmund.moen@yahoo.com', 'vivian.hartmann@yahoo.com', 'velva.boyle@gmail.com', 'veronica.adams@grady.com', 'smohr@rowe.com', 'jalyn13@gmail.com']
    assert extract_emails(story_text) == expected_emails

# Part 2: Test Validate Phone Numbers
def test_validate_phone_numbers():
    phone_numbers = [
        "(123) 456-7890",
        "555-555-5555",
        "987-654-3210",
        "(555) 123-4567",
        "555-987-6543",
        "555 876 5432",
        "(555)999-0000",
        "5550001111",
        "not a number",
    ]
    expected_valid_numbers = [
        "(123) 456-7890",
        "555-555-5555",
        "987-654-3210",
        "(555) 123-4567",
        "555-987-6543",
        "555 876 5432",
        "(555)999-0000",
        "5550001111",
    ]
    assert validate_phone_numbers(phone_numbers) == expected_valid_numbers

# Part 3: Test Find Dates
def test_find_dates():
    expected_dates = ['08/15/2022', '03/20/2023', '10/05/2022', '06/12/2023', '02/19/2022', '09/30/2022', '07/28/2022', '11/14/2022', '01/10/2023', '04/03/2023', '03/04/2022', '08/09/2022', '05/16/2022', '07/07/2022', '11/30/2022', '09/05/2022', '10/24/2022', '02/27/2023', '04/18/2022', '06/30/2023']
    assert [match.group() for match in find_dates(story_text)] == expected_dates

# Part 4: Test Format Phone Numbers
def test_format_phone_numbers():
    expected_text = """
Once upon a time, in a small town, there was a quirky character named Alice who was known for her love of numbers and email addresses. She had an unusual fascination with phone numbers, and her favorite phone number was (123) 456-7890. She had it memorized as if it were a treasured secret.
One day, Alice received a mysterious email at her address, (555) 555-5555. The email was from an anonymous sender with the subject "(987) 654-3210," dated 08/15/2022. Alice was both puzzled and intrigued, wondering what this email could be about.
Her curiosity got the best of her, so she opened the email. Inside, she found a message from someone using the name (555) 123-4567, but the message was filled with seemingly random numbers like (555) 987-6543 and phrases like "not a number." It was a coded message that she couldn't decipher. The message was sent on 03/20/2023.
Determined to solve the mystery, Alice decided to consult her friend Bob, whose phone number was (888) 555-1234. Bob was known for his expertise in solving puzzles and riddles. Alice explained the strange email to him, and he agreed to help.
Together, they decoded the message to reveal a series of new phone numbers: (555) 333-7777, (555) 876-5432, and (555) 999-0000. The message was dated 10/05/2022. It also contained an email address, effertz.viola@batz.com, and a list of more emails, including hackett.jed@hotmail.com (sent on 06/12/2023), sadie.kuhn@ward.com (dated 02/19/2022), and @invalid-missingusername.com (received on 09/30/2022).
They realized that the numbers and emails were part of a treasure hunt. They followed the clues and found a hidden chest filled with various items. Among them were a collection of emails with unique addresses, such as kathryne92@gmail.com (sent on 07/28/2022), fbayer@terry.biz (dated 11/14/2022), toni74@nikolaus.biz (received on 01/10/2023), and senger.cale@ullrich.com (sent on 04/03/2023).
Alice and Bob's adventure continued, leading them to more discoveries, including the emails tom.oberbrunner@gmail.com (dated 03/04/2022), invalid.email@invalid, and imann@gmail.com (received on 08/09/2022). They even encountered an email address with spaces in the domain, user@spaces in domain.com, and another with an incomplete domain, user@.incomplete.
As they delved deeper into the treasure hunt, they encountered more challenges, like an email with an underscore in the domain, invalid@-hyphen-start.com, and an email with a trailing period, heber74.@rohan.org. Along the way, they discovered more emails, like asha46@blanda.com, retha11@yahoo.com, vada.pacocha@hotmail.com, myron85@hotmail.com, kbergstrom@herman.com, and an email with an extra "@" symbol, user@invalid@com.
Despite the obstacles, Alice and Bob's determination paid off as they uncovered more hidden gems, including emails like vicky.carter@gmail.com (dated 05/16/2022), bernier.darrell@hammes.com (received on 07/07/2022), sigmund.moen@yahoo.com (sent on 11/30/2022), vivian.hartmann@yahoo.com (dated 09/05/2022), velva.boyle@gmail.com (received on 10/24/2022), veronica.adams@grady.com (sent on 02/27/2023), smohr@rowe.com (dated 04/18/2022), and jalyn13@gmail.com.
The treasure hunt finally led them to the most intriguing discovery of all: a message containing the email "invalid.com" and "@invalid.com" (sent on 06/30/2023). This message was the key to unlocking the final treasure, which turned out to be a message of friendship and a lesson in the beauty of the unexpected.
Alice and Bob learned that sometimes, life's greatest treasures are found in the quirkiest and most unexpected places, and that the dates they encountered along the way added a touch of uniqueness to their adventure. They celebrated their journey and the diverse world of numbers and emails, realizing that there's always something new and exciting to discover.
"""
    assert format_phone_numbers(story_text).replace('\n', '') == expected_text.replace('\n', '')

# Run the tests
if __name__ == "__main__":
    pytest.main()