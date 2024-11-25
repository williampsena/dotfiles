from local.core.config.settings import AppSettings
from libqtile import widget
from libqtile.log_utils import logger


class FontIconTaskList(widget.TaskList):
    def get_taskname(self, window):
        state = ""
        markup_str = self.markup_normal

        if (
            self.markup_minimized
            or self.markup_maximized
            or self.markup_floating
            or self.markup_focused
            or self.markup_focused_floating
        ):
            enforce_markup = True
        else:
            enforce_markup = False

        if window is None:
            pass
        elif window.minimized:
            state = self.txt_minimized
            markup_str = self.markup_minimized
        elif window.maximized:
            state = self.txt_maximized
            markup_str = self.markup_maximized
        elif window is window.group.current_window:
            if window.floating:
                state = self.txt_floating
                markup_str = self.markup_focused_floating or self.markup_floating
            else:
                markup_str = self.markup_focused
        elif window.floating:
            state = self.txt_floating
            markup_str = self.markup_floating

        window_location = (
            f"[{window.group.windows.index(window) + self.window_name_location_offset}] "
            if self.window_name_location
            else ""
        )

        window_name = window_location + window.name if window and window.name else "?"
        wm_class = window.get_wm_class()
        window_classname = wm_class[0] if wm_class else "Unknown"

        if callable(self.parse_text):
            try:
                window_name = self.parse_text(window_name, window_classname)
            except:  # noqa: E722
                logger.exception("parse_text function failed:")

        # Emulate default widget behavior if markup_str is None
        if enforce_markup and markup_str is None:
            markup_str = f"{state}{{}}"

        if markup_str is not None:
            self.markup = True
            window_name = pangocffi.markup_escape_text(window_name)
            return markup_str.format(window_name)

        return f"{state}{window_name}"


def _parse_window_name(name: str):
    return name.lower().replace(" ", "_")


def _icon_replacement_parse_text(settings: AppSettings):
    def _fetch_icon(
        apps: dict[str, str],
        fallback_icon: str,
        window_name: str,
        window_classname: str,
    ) -> str | None:
        parsed_window_name = _parse_window_name(window_name)
        parsed_window_classname = _parse_window_name(window_classname)

        return next(
            (
                v
                for k, v in apps.items()
                if (k in parsed_window_name) or (k in parsed_window_classname)
            ),
            fallback_icon,
        )

    def _inner(window_name: str, window_classname: str) -> str:
        fallback_icon = settings.applications.icons.get("window", "")
        icon = _fetch_icon(
            settings.applications.icons,
            fallback_icon,
            window_name,
            window_classname,
        )
        name = window_name[:15]

        # Return the formatted icon and name
        return f"{icon.strip()}   {name.strip()}" if icon else name

    return _inner


def build_task_list_widget(settings: AppSettings, kwargs: dict):
    task_list_args = {
        "icon_size": 0,
        "margin_y": 4,
        "margin_x": 0,
        "padding": 0,
        "highlight_method": "border",
        "border": settings.colors.fg_normal,
        "borderwidth": 0,
        "parse_text": _icon_replacement_parse_text(settings),
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
    }

    return FontIconTaskList(**task_list_args)
