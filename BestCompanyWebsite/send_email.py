import smtplib, ssl

def sendEmail(sentFrom, msg):
  host = "smtp.gmail.com"
  port = 465

  username = "jhornjr@gmail.com"
  password = "GMAILPASSWORD" # Enviroment Variable

  receiver = "jhornjr@gmail.com"
  context = ssl.create_default_context()

  result = ""

  try:

    with smtplib.SMTP_SSL(host, port, context=context) as server:
      server.login(username, password)
      server.sendmail(sentFrom, receiver, msg)
      result = "Message sent. Thank you."
      return result

  except:
    result = "Error: Message could not be sent. Try again."
    return result
