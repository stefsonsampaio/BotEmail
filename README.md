# Email Autoresponder and PDF Sender

This Python script serves as an email autoresponder and PDF sender, designed to be executed indefinitely. It continuously monitors the inbox, detects new email messages, and sends personalized replies based on specific conditions. Moreover, it can automatically attach a PDF file if the subject of the received email contains the keyword "pdfpath."

## Prerequisites

Before running the script, ensure you have the following:

1. Python installed on your system.
2. The required Python libraries: `os`, `sys`, `time`, `smtplib`, `imaplib`, `email`, `base64`, and others. Install them using `pip` if needed.

## Setup

1. Replace the placeholders 'youremail@example.com' and 'yourpassword' with your actual Gmail credentials in two places within the code.
2. If you want to include PDF attachments, save the PDF file with the name 'pdfpath.pdf' in the same directory as this script.

## How It Works

1. The script constantly monitors the inbox using IMAP over SSL to connect to the Gmail server.
2. It reads the `log.txt` file to determine the last email count that was processed.
3. If new messages are found since the last check, the script processes the latest email.
4. It extracts the sender's email address, the subject, and the body of the email.
5. Depending on the subject's content, the script composes a reply, either with a PDF attachment or a regular response.
6. The reply is then sent back to the sender's email address.
7. The script updates the `log.txt` file with the latest email count to keep track of processed emails.

## Usage

1. Execute the script using Python.
2. The program will run indefinitely, checking for new emails every 5 seconds.
3. When a new email arrives, the script will automatically respond according to the conditions specified in the code.
4. If the subject contains 'pdfpath', the script will attach the PDF named 'pdfpath.pdf' to the reply.

**Please Note:** For security reasons, avoid using actual email addresses and passwords directly in the code. Instead, consider using environment variables or configuration files to store sensitive information.

Feel free to explore and customize the script to suit your specific needs! Happy coding!
