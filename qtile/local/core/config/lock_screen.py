class AppSettingsLockScreen:
    command = ""
    timeout = 10
    font = ""
    font_size = 17
    joke_font_path = ""
    joke_font_size = 17
    joke_providers = "reddit"
    joke_foreground_color = "#fff"
    joke_text_color = "#000"
    icanhazdad_joke_url = ""
    reddit_joke_url = "https://www.reddit.com/r/ProgrammerDadJokes.json"
    blurtype = "0x5"

    def __init__(self, **kwargs):
        self.command = kwargs.get("command", self.command)
        self.timeout = kwargs.get("timeout", str(self.timeout))
        self.font = kwargs.get("font", self.font)
        self.font_size = int(kwargs.get("font_size", str(self.font_size)))
        self.joke_font_path = kwargs.get("joke_font_path", self.joke_font_path)
        self.joke_font_size = int(
            kwargs.get("joke_font_size", str(self.joke_font_size))
        )
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
