class AppSettingsApplications:
    icons: dict[str, str] = {}

    def __init__(self, **kwargs):
        self.icons = kwargs.get("icons", self.icons)
