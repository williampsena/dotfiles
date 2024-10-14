
class AppSettingsFonts:
    font: str = ""
    font_regular: str = ""
    font_light: str = ""
    font_strong: str = ""
    font_strong_bold: str = ""
    font_size: int = 10
    font_icon: str = ""
    font_icon_size: int = 10

    def __init__(self, **kwargs):
        self.font = kwargs.get("font", self.font)
        self.font_regular = kwargs.get("font_regular", self.font_regular)
        self.font_light = kwargs.get("font_light", self.font_light)
        self.font_strong = kwargs.get("font_strong", self.font_strong)
        self.font_strong_bold = kwargs.get("font_strong_bold", self.font_strong_bold)
        self.font_size = int(kwargs.get("font_size", str(self.font_size)))
        self.font_icon = kwargs.get("font_icon", self.font_icon)
        self.font_icon_size = int(kwargs.get("font_icon_size", str(self.font_icon_size)))

