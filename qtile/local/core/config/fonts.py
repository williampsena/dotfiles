class AppSettingsFonts:
    font: str = ""
    font_regular: str = ""
    font_light: str = ""
    font_strong: str = ""
    font_strong_bold: str = ""
    font_size: int = 10
    font_icon: str = ""
    font_icon_size: int = 10
    font_arrow: str = ""
    font_arrow_size: int = 10
    rofi_font: str = ""
    rofi_font_size: int = 10
    font_notification: str = ""
    font_notification_size: int = 10

    def __init__(self, **kwargs):
        self.font = kwargs.get("font", self.font)
        self.font_regular = kwargs.get("font_regular", self.font_regular)
        self.font_light = kwargs.get("font_light", self.font_light)
        self.font_strong = kwargs.get("font_strong", self.font_strong)
        self.font_strong_bold = kwargs.get("font_strong_bold", self.font_strong_bold)
        self.font_size = int(kwargs.get("font_size", str(self.font_size)))
        self.font_icon = kwargs.get("font_icon", self.font_icon)
        self.font_icon_size = int(
            kwargs.get("font_icon_size", str(self.font_icon_size))
        )
        self.font_arrow = kwargs.get("font_arrow", self.font_arrow)
        self.font_arrow_size = int(
            kwargs.get("font_arrow_size", str(self.font_arrow_size))
        )
        self.rofi_font = kwargs.get("rofi_font", self.font)
        self.rofi_font_size = int(kwargs.get("rofi_font_size", str(self.font_size)))
        self.font_notification = kwargs.get("font_notification", self.font)
        self.font_notification_size = int(
            kwargs.get("font_notification_size", str(self.font_size))
        )
