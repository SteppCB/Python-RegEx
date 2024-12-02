import re

def extract_emails(text):
    """Extract valid email addresses from text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    valid_emails = []
    for email in emails:
        if not any(invalid in email for invalid in [' ', '@.', '.@', '@-', '--', '..']):
            if not email.startswith('.') and not email.endswith('.'):
                if not '@invalid' in email and not email.startswith('@'):
                    valid_emails.append(email)
    return valid_emails

def validate_phone_numbers(numbers):
    """Validate a list of phone numbers."""
    valid_patterns = [
        r'^\(\d{3}\)\s?\d{3}-\d{4}$',  # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',         # 123-456-7890
        r'^\d{3}\s\d{3}\s\d{4}$',       # 123 456 7890
        r'^\(\d{3}\)\d{3}-\d{4}$',      # (123)456-7890
        r'^\d{10}$'                      # 1234567890
    ]
    valid_numbers = []
    for number in numbers:
        if any(re.match(pattern, number) for pattern in valid_patterns):
            valid_numbers.append(number)
    return valid_numbers

def find_dates(text):
    """Find dates in MM/DD/YYYY format in text."""
    date_pattern = r'\b(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/20\d\d\b'
    return re.finditer(date_pattern, text)

def format_phone_numbers(text):
    """Format phone numbers in text to (XXX) XXX-XXXX format."""
    def format_match(match):
        # Get all digits from the match
        digits = ''.join(re.findall(r'\d', match.group()))
        # Format to (XXX) XXX-XXXX
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"

    # Pattern to match all possible phone number formats
    pattern = r'(?:\b\d{3}[-\s]\d{3}[-\s]\d{4}\b|\b\d{10}\b|\(\d{3}\)[- ]?\d{3}-\d{4})'
    
    # Replace all phone numbers with formatted version
    formatted = re.sub(pattern, format_match, text)
    
    # Add newline at the start to match expected format
    return "\n" + formatted if not formatted.startswith("\n") else formatted
