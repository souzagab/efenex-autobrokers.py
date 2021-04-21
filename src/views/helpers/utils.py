def logo_text(text="", font="slant"):
    from pyfiglet import Figlet
    f = Figlet(font=font)
    return f.renderText(text)