def burn_text(text, position="left") -> str:
    if position == "left":
        return f"🔥 {text}"

    return f"{text} 🔥"
