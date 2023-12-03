from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()
def process(choice_font):
    figlet.setFont(font=choice_font)
    text = input("Input: ")
    print("Output:",figlet.renderText(text))
if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[2] == "--font") and sys.argv[2] in fonts:
        choice_font = sys.argv[2]
        process(choice_font)
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 0:
    choice_font = random.choice(fonts)
    process(choice_font)
else:
    sys.exit("Invalid usage")