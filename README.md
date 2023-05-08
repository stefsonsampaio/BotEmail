# BotEmail
Projeto : Criando um bot para responder emails automaticamente

This program read the inbox emails with imap lib and create answer with smtp lib. It's up to you how you gonna use it. In my case, i wanted to keep my e-mail answer In-Reply-To, so it attachs my answer with the last one I received. 

There's the option to create conditions to the answers. I used decode and decod to make possible to read and send messages with accent or symbols, what's indispensable for pt-br. Then, the e-mail is splitted by body and subject, what make possible to create the example conditions in line #82.

For my specif need, i add the possibility of send PDF file attachment in e-mail. So, in line #82 you can see the functions needed to make email's body multipart so it can support PDF file.

Comented lines between #25 and #29 are responsible to find log.txt file's path in case you want to use pyinstaller to turn the botapp.py into an .exe file. The pyinstaller combine all the files in same folder and change their paths, so turns out it's necessary to use sys and os libs to find log.txt's path wherever pyinstaller puts that.

it's important to have a log.txt file at same tree as botapp.py, so it can save the information of how many e-mail have been received, what make possible to run the program infinitally, checking how many emails it had, to send or not a new answer.

It's necessary to have the not trust website configuration enabled on e-mail security settings. In addition, it's necessary to enable the IMAP option also in gmail configuration.
