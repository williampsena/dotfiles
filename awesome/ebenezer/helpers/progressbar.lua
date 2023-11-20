local function build_progressbar(level, step)
    local icon = ""
    local bar = ""

    if not step then step = 20 end

    level = level / step

    for i = 1, level do bar = bar .. icon end

    return bar
end

return {build_progressbar = build_progressbar}
