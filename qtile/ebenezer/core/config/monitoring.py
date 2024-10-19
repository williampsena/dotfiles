class AppSettingsMonitoring:
    default_color: str = ""
    high_color: str = ""
    medium_color: str = ""
    threshold_medium: int = 75
    threshold_high: int = 90
    burn: bool = False

    def __init__(self, **kwargs):
        self.default_color = kwargs.get("default_color", self.default_color)
        self.high_color = kwargs.get("high_color", self.high_color)
        self.medium_color = kwargs.get("medium_color", self.medium_color)
        self.threshold_medium = kwargs.get("threshold_medium", self.threshold_medium)
        self.threshold_high = kwargs.get("threshold_high", self.threshold_high)
        self.burn = kwargs.get("burn", "no") == "yes"
