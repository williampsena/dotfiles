class AppSettingsLockScreen:
    command = ""
    timeout = 10
    font = ""
    font_size = 17
    joke_providers = "reddit"
    joke_foreground_color = "#fff"
    joke_text_color = "#000"
    icanhazdad_joke_url = ""
    reddit_joke_url = "https://www.reddit.com/r/ProgrammerDadJokes.json"
    blurtype = "0x5"
    blank_color = "#00000000"
    clear_color = "#ffffff22"
    default_color = "#9db4c0"
    key_color = "#8a8ea800"
    text_color = "#4BC1CC"
    wrong_color = "#D50000"
    verifying_color = "#41445800"

    def __init__(self, **kwargs):
        self.command = kwargs.get("command", self.command)
        self.timeout = kwargs.get("timeout", str(self.timeout))
        self.font = kwargs.get("font", self.font)
        self.font_size = int(kwargs.get("font_size", str(self.font_size)))
        self.joke_providers = kwargs.get("joke_providers", self.joke_providers).split(
            ","
        )
        self.joke_foreground_color = kwargs.get(
            "joke_foreground_color", self.joke_foreground_color
        )
        self.joke_text_color = kwargs.get("joke_text_color", self.joke_text_color)
        self.icanhazdad_joke_url = kwargs.get(
            "icanhazdad_joke_url", self.icanhazdad_joke_url
        )
        self.reddit_joke_url = kwargs.get("reddit_joke_url", self.reddit_joke_url)
        self.blurtype = kwargs.get("blurtype", self.blurtype)
        self.blank_color = kwargs.get("blank_color", self.blank_color)
        self.clear_color = kwargs.get("clear_color", self.clear_color)
        self.default_color = kwargs.get("default_color", self.default_color)
        self.key_color = kwargs.get("key_color", self.key_color)
        self.text_color = kwargs.get("text_color", self.text_color)
        self.wrong_color = kwargs.get("wrong_color", self.wrong_color)
        self.verifying_color = kwargs.get("verifying_color", self.verifying_color)
